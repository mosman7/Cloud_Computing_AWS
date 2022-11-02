# Connect app to mongodb

## Step 1
- Launch 2 ec2 instances - 1 for app, 1 for db
- in db security, create an inbound rule allowing access to the mongodb port 27017 and make the source the ip of the app

## Step 2
- in gitbash ssh into db vm
- Run the update/upgrade commands `sudo apt-get update -y` && `sudo apt-get upgrade -y`
- now we need to install mongodb
- `sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv D68FA50FEA312927`
- `echo "deb https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list`
- Run the update/upgrade commands `sudo apt-get update -y` && `sudo apt-get upgrade -y`
- `sudo apt-get install -y mongodb-org=3.2.20 mongodb-org-server=3.2.20 mongodb-org-shell=3.2.20 mongodb-org-mongos=3.2.20 mongodb-org-tools=3.2.20`
- if mongo is is set up correctly these will be successful
- `sudo systemctl restart mongod`
- `sudo systemctl enable mongod`
- Check to see if it is running `sudo systemctl status mongod`

## Step 3
- Change the mongod.conf file
- cd into etc folder `cd /etc`
- `sudo nano mongod.conf`
- edit the bindIp as below and ensure port is 27017 
- - `port: 27017`. `bindIp: 0.0.0.0`
- restart mongodb `sudo systemctl restart mongodb`
- enable mongodb `sudo systemctl enable mongodb`

## Step 4
- ssh into app vm
- Create a environment variable called db_host
- `export DB_HOST=mongodb://0.0.0.0:27017/posts` - input db ip address where 0.0.0.0
- printenv DB_HOST to see if this has saved
- `npm install`
- `npm start`
- launch app ip in web browser with /posts - db should now be connected
- to get data run `node seeds/seed.js`