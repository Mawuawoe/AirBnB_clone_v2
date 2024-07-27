#!/usr/bin/env bash
# A Bash script that sets up web servers for the deployment of web_static

# shellcheck disable=SC1004

# Function to create a directory if it doesn't exist
create_directory() {
    local dir=$1
    if [ ! -d "$dir" ]; then
        echo "Creating directory: $dir"
        mkdir -p "$dir"
    else
        echo "Directory already exists: $dir"
    fi
}

# Check if Nginx is already installed
if ! command -v nginx &> /dev/null; then
    echo "Nginx is not installed. Installing Nginx..."

    # Update the package list
    sudo apt update

    # Install Nginx
    sudo apt install -y nginx

    # Start Nginx service
    sudo systemctl start nginx

    # Enable Nginx to start on boot
    sudo systemctl enable nginx

    echo "Nginx installation completed."
else
    echo "Nginx is already installed."
fi

# Create the necessary directories
create_directory "/data/"
create_directory "/data/web_static/"
create_directory "/data/web_static/releases/"
create_directory "/data/web_static/shared/"
create_directory "/data/web_static/releases/test/"

# Create a fake HTML file with simple content
echo "Creating fake HTML file: /data/web_static/releases/test/index.html"
cat <<EOL > /data/web_static/releases/test/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOL

# Create a symbolic link, removing existing one if necessary
if [ -L "/data/web_static/current" ]; then
    echo "Removing existing symbolic link: /data/web_static/current"
    rm -f /data/web_static/current
fi

echo "Creating new symbolic link: /data/web_static/current -> /data/web_static/releases/test/"
ln -s /data/web_static/releases/test/ /data/web_static/current

# Change ownership of the /data/ folder to ubuntu user and group
echo "Changing ownership of /data/ to ubuntu user and group"
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve /data/web_static/current/ under/hbnb_static as an alias
NGINX_CONF="/etc/nginx/sites-enabled/default"



if grep -q "location /hbnb_static" $NGINX_CONF; then
    echo "Updating existing Nginx configuration for /hbnb_static"
    sudo sed -i '/location \/hbnb_static {/,/}/c\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' $NGINX_CONF
else
    echo "Adding new Nginx configuration for /hbnb_static"
    sudo sed -i '/listen 80 default_server/ a\
    \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' $NGINX_CONF
fi

# Restart Nginx to apply changes
echo "Restarting Nginx"
sudo service nginx restart

echo "Setup completed."
