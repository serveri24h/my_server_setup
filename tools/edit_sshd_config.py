import sys

file_name = "/etc/ssh/sshd_config"


commands = {
    'root_log': "PermitRootLogin",
    'pswd_log': "PasswordAuthentication"
}




def change_atribute(row_name):
    edit_flag = False
    with open(file_name, "r") as f:
        data = f.readlines()

    for i,line in enumerate(data):
        if row_name in line:
            data[i] = row_name+" no\n"
            edit_flag = True

    if not edit_flag or data==None:
        print("Couldn't change root login")
    else:
        with open(file_name, "w") as f:
            f.writelines(data)
            print("Root-Login prohibited")

if __name__ == '__main___':
    x = sys.argv
    if len(x) == 1 and x[0] in commands.keys():
        change_atribute(commands[x[0]])
    else:
        print("Failed arguments...")