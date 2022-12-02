build_folder="build"

if [ "$EUID" == 0 ]; then
    if [ "$1" != "" ]; then
        build_folder=$1
    fi
    rm -r /var/www/html/*
    cp -r "$build_folder/*" /var/www/html/
    nginx -s reload
        
else
    echo " This script needs to be run with sudo privilidges"
    echo " run: sudo bash $0 <path/to/build/folder>"
fi