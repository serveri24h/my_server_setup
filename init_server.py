import getpass, sys, os
from fabric import Connection, Config

LOG_PATH = '/home/server-logs.txt'
TOOL_FOLDER = '.server-tools'
WDIR = '/MAIN/BetterCode/my_server_setup'
PUB_KEY = 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJT4WhimeQ2XzwAgzn8WYKedR5ndB2+qo34Fq5HbI1Pe severi.vapalahti@gmail.com'

def init_connection(addr, user='root'):
    password = getpass.getpass("Enter the root password: ")
    try:
        return Connection(host=f"{user}@{addr}", connect_kwargs={"password": f"{password}"})
    except Exception as e:
        print("Failed with exception", e)
        return None

def init_server(c):
    print("--- Initiating server ---")
    logs = c.run('apt update && apt upgrade -y', hide=True)
    logs = c.run('apt install build-essential -y', hide=True)
    logs = c.run('apt install git -y', hide=True)
    logs = c.run('apt install htop -y', hide=True)
    logs = c.run('apt install expect -y', hide=True)

def setup_firewall(c):
    print("--- Firewall Setup ---")
    logs = c.run('apt install ufw -y', hide=True)
    logs = c.run('ufw default allow outgoing', hide=True)
    logs = c.run('ufw default deny incoming', hide=True)
    logs = c.run('ufw allow ssh', hide=True)
    logs = c.run('ufw allow http/tcp', hide=True)
    logs = c.run("""
        expect -c 'spawn sudo ufw enable;
            expect "Proceed with operation (y|n)?";
            send "y\r";
            interact;'
    """, hide=True)

def setup_user(c):
    print("--- User Setup ---")
    #print("Creating a new user...")
    #user_password = getpass.getpass("Enter the password for new user: ")
    # expected sentence = "New password:"
    logs = c.run('useradd -d /home/admin -m -s /bin/bash admin && passwd admin')
    logs = c.run('usermod -a -G sudo admin', hide=True)

def secure_login(c):
    ("--- Securing the login ---")
    tool_path = f"/home/admin/{TOOL_FOLDER}"
    try:
        logs = c.run('mkdir /home/admin/.ssh', hide=True)
    except Exception as e:
        logs = e
    logs = c.run(f'echo "{PUB_KEY}" >> /home/admin/.ssh/authorized_keys', hide=True)
    try:
        logs = c.run(f'mkdir "{tool_path}"', hide=True)
    except Exception as e:
        logs = e
    c.put(f'{WDIR}/tools/edit_sshd_config.py', remote=tool_path, preserve_mode=True)
    c.put(f'{WDIR}/scripts/install_tools.sh', remote=tool_path, preserve_mode=True)
    c.put(f'{WDIR}/scripts/update_static.sh', remote=tool_path, preserve_mode=True)
    logs = c.run(f'python3 "{tool_path}/edit_sshd_config.py" root_log', hide=True)
    logs = c.run(f'python3 "{tool_path}/edit_sshd_config.py" pswd_log', hide=True)
    logs = c.run('systemctl restart sshd', hide=True)

def login_to_server(ip):
    os.system(f"""
        expect -c 'spawn ssh admin@{ip};
            expect "connecting (yes/no)?";
            send "yes\r";
            interact;'
    """)

def main():
    if len(sys.argv) == 2:
        ip_addr = sys.argv[1]
        with init_connection(ip_addr) as conn:
            # INIT SERVER
            init_server(conn)
            
            # SETUP FIREWALL
            setup_firewall(conn)

            # SETUP USER
            setup_user(conn)
            secure_login(conn)
        
        # LOGIN
        login_to_server(ip_addr)
    else:
        print("tait")


if __name__=='__main__':
    main()
