#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

#Install Nginx if it not already installed
apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'


mkdir -p /data/

mkdir -p /data/web_static/

#Create the folder /data/web_static/releases/test/
mkdir -p /data/web_static/releases/test/

#Create the folder /data/web_static/shared/
mkdir -p /data/web_static/shared/

# Create a fake HTML file /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

#Symbolic link to /data/web_static/releases/test/
ln -sf /data/web_static/releases/test /data/web_static/current

#Give ownership of the /data/ folder to the ubuntu user AND group
chown -R ubuntu:ubuntu /data/

sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default

#Restart nginx
service nginx restart
exit 0
