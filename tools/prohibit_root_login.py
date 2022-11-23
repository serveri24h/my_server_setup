
file_name = "/etc/ssh/sshd_config"
edit_flag = False

with open(file_name, "r") as f:
    data = f.readlines()

for i,line in enumerate(data):
    if line[:15] == "PermitRootLogin":
        data[i] = "PermitRootLogin no\n"
        edit_flag = True

if not edit_flag and data!=None:
    print("Couldn't change root login")
else:
    with open(file_name, "w") as f:
        f.writelines(data)
        print("Root-Login prohibited")