########################################
####            SETUP               ####
########################################

## First update and uprade apt and download git
##       -> then clone this repo

#Create log-file in home-folder
logfile="/home/setup-logs.txt"
touch $logfile

#update package manager
echo "(1) Initiating"
echo "####################
INITIAL SETUP
####################
" >> $logfile

apt install build-essential -y >> $logfile
apt install htop -y >> $logfile

########################################
####           FIREWALL             ####
########################################

echo "(2) Firewall setup"
echo "####################
FIREWALL SETUP
####################
" >> $logfile

apt install ufw -y  >> $logfile
ufw default allow outgoing  >> $logfile
ufw default deny incoming  >> $logfile
ufw allow ssh  >> $logfile
ufw allow http/tcp  >> $logfile
ufw enable


########################################
####            USERS               ####
########################################

echo "(3) User setup"
echo "####################
USER SETUP
####################
" >> $logfile

#make adminuser
adduser admin
usermod -a -G sudo admin >> $logfile


#Prohibit root login
python3 tools/edit_sshd_config.py root_log >> $logfile
systemctl restart sshd >> $logfile

#Change user
su admin





