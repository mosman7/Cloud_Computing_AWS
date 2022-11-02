# How to set up an EC2 instrance

- copy file with key into .ssh folder
- chmod 400 eng130.pem - change permissions to make it readable
- Log in to the AWS web console
- Go to EC2 dashboard and select instances
- Click on Launch instance
 ![Instance](https://user-images.githubusercontent.com/115226294/199481086-d1234258-f807-496e-9e89-e76b964a121d.png)
- Here you will be instructed to name the instance

![instance1](https://user-images.githubusercontent.com/115226294/199496361-0d508257-41f3-4114-8786-1cfac7f9c283.png)
- Set the OS to Ubuntu 18.04

  ![instance2](https://user-images.githubusercontent.com/115226294/199496819-9f1e7d41-5a2c-48f8-9da3-67c1923bb4cc.png)

- set the key pair to eng130

 ![instance3](https://user-images.githubusercontent.com/115226294/199496905-75b0eeb4-606b-4a3e-a6f1-2dc594fa0590.png)

- select the security group or create a new one depending on

 ![instance4](https://user-images.githubusercontent.com/115226294/199496934-87243cfa-b2aa-4c29-97de-d537fdd7328d.png)

- leave storage at 8gb and launch the instance

 ![instance5](https://user-images.githubusercontent.com/115226294/199496959-28b169fa-048d-4504-b629-4d95a2802df9.png)


# Connect to the instance VM

- select the instance in question and click connect at the top
- navigate to the ssh tab and copy the link at the bottom
- open git bash and cd into the location where the key is (eng130.pem)
- paste the link in there
- The instance is now connected
<<<<<<< HEAD

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
