# Set up reverse proxy

### After connecting to the instance:
- in gitbash run `sudo apt-get update -y` and `sudo apt-get upgrade -y`
- install nginx `sudo apt install nginx`
- now to set up reverse proxy sudo into default file `sudo nano /etc/nginx/sites-available/default`
- And change location to:
```
    proxy_pass http://localhost:3000;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection 'upgrade';
    proxy_set_header Host $host;
    proxy_cache_bypass $http_upgrade;
```
- save and check if syntax is correct `sudo nginx -t`
- restart nginx `sudo systemctl restart nginx`