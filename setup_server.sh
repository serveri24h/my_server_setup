########################################
####            SETUP               ####
########################################

## First update and uprade apt and download git
##       -> then clone this repo

#update package manager
apt install build-essential -y
apt install htop -y


########################################
####            USERS               ####
########################################

#make adminuser
adduser admin
usermod -a -G sudo admin


#Prohibit root login
python tools/prohibit_root_login.py
systemctl restart sshd

#Change user
su admin





