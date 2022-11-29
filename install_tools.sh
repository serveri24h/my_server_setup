#########################################
###            TOOLS                  ###
#########################################

if [ "$EUID" == 0 ]; then
    #install rust
    echo "Install rust? (y/N)"
    read install_rust
    if [ "$install_rust" == "y" ]; then
        curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    fi

    #install node.js
    echo "Install node? (y/N)"
    read install_node
    if [ "$install_node" == "y" ]; then
        curl -fsSL https://deb.nodesource.com/setup_19.x | bash - &&\
        apt-get install -y nodejs
    fi

    #install docker
    echo "Install docker? (y/N)"
    read install_docker
    if [ "$install_docker" == "y" ]; then

        # Add Docker’s official GPG key
        sudo mkdir -p /etc/apt/keyrings
        curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

        # Setup Repository
        echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
        $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
        sudo apt-get update

        #Install
        sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin -y
    fi

    #########################################
    ####         SERVER SETUP            ####
    #########################################

    echo "Setup server with nginx? (y/N)"
    read setup_server
    if [ "$setup_server" == "y" ]; then
        curl -fsSL https://deb.nodesource.com/setup_19.x | bash - &&\
        apt-get install -y nodejs

        #make folder for the project
        mkdir -p /var/www/mydomain.com
        chmod 755 -R /var/www/mydomain.com

        #install rsync
        apt install rsync

        # install, setup and start nginx
        apt install nginx -y
        echo "server {
            listen 80;
            listen [::]:80;

            root /var/www/mydomain.com; 
                index index.html index.htm;

        }
        " > /etc/nginx/conf.d/myapp.conf
        systemctl restart nginx
    fi
else
    echo " This script needs to be run with sudo privilidges"
