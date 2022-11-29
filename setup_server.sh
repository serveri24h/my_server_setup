########################################
####            SETUP               ####
########################################

## First update and uprade apt and download git
##       -> then clone this repo

#update package manager
apt install build-essential -y
apt install htop -y

########################################
####           FIREWALL             ####
########################################

apt install ufw
ufw default allow outgoing
ufw default deny incoming
ufw allow ssh
ufw allow http/tcp
ufw enable -y


########################################
####            USERS               ####
########################################

#make adminuser
clear
adduser admin
usermod -a -G sudo admin


#Prohibit root login
python3 tools/prohibit_root_login.py
systemctl restart sshd

#Change user
su admin





