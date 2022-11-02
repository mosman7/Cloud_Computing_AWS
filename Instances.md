# How to set up an EC2 instrance

- copy file with key into .ssh folder
- chmod 400 eng130.pem - change permissions to make it readable
- Log in to the AWS web console
- Go to EC2 dashboard and select instances
- Click on Launch instance
 ![Instance](https://user-images.githubusercontent.com/115226294/199481086-d1234258-f807-496e-9e89-e76b964a121d.png)

- Here you will be instructed to name the instance
- Set the OS to Ubuntu 18.04
- set the key pair to eng130
- select the security group or create a new one depending on
- leave storage at 8gb and launch the instance

# Connect to the instance VM

- select the instance in question and click connect at the top
- navigate to the ssh tab and copy the link at the bottom
- open git bash and cd into the location where the key is (eng130.pem)
- paste the link in there
- The instance is now connected

# How to automate EC2 instances
To automate EC2 instances, you have to either add a script in the text
- When customizing network configuration, if you scroll all the way to the bottom.
- You will see, userdata, in that text box.
- You will be able to add your bash scripts or you can choose As file and add your script.
- My bash script looked like this:
```
#!/bin/bash

sudo apt-get update -y
sudo apt-get upgrade -y

sudo apt install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx

curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install nodejs -y

sudo npm install pm2 -g
npm install
npm start
```
# Copy files from Localhost to VM
- if file is zipped make sure to unzip first
- in .ssh folder run :
`scp -i access.pem -r ~/Documents/directory1 ubuntu@0.0.0.0:/home/ubuntu/`
- In my case i did `scp -i eng130.pem -r /C:/Users/moham/eng130_virtualisation/app/ ubuntu@ec2-52-214-111-95.eu-west-1.compute.amazonaws.com`
- ssh back into vm and do `ls`
- imported files should be present
