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
            if row_name=='root_log':
                print("Root-Login prohibited")
            elif row_name=='pswd_log':
                print("Password-Login prohibited")

if __name__ == '__main__':
    x = sys.argv
    if len(x) == 2 and x[1] in commands.keys():
        try:
            change_atribute(commands[x[1]])
        except Exception as e:
            print("Something failed with error: ", e)
    else:
        print("Failed arguments...")