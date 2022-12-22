#!/usr/bin/env bash
# Set up web servers for deployment of web static
apt-get -y update
apt-get -y install nginx
service nginx start
mkdir -p /data/web_static/shared /data/web_static/releases/test
echo "Hello World" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i "/listen 80 default_server;/ a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
service nginx restart
