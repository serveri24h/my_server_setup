if [ "$EUID" == 0 ]; then

    # first make sure that you have the public key in the server
    # On local computer run:
    # (sudo) ssh-copy-id <user@addres>

    python3 tools/edit_sshd_config.py pswd_log
    systemctl restart ssh
else
    echo " This script needs to be run with sudo privilidges."
fi