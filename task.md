## Setting up a VPC
#### Step 1 - Create a VPC
- On the AWS console, go to VPC
- `Create VPC`
- Add your name tag, input IPV4 CIDR block and create VPC
![VPC 1](https://user-images.githubusercontent.com/115226294/200382298-8d6266de-4a71-40ca-98bf-5e47f867d412.png)

#### Step 2 - Create an Internet Gateway
- On the VPC dashboard, select `Internet Gateway`
- Add your name tag and click `Create Internet Gateway`
- Once created, click `Action` and link to VPC created in step 1

#### Step 3 -  Create a subnet
- On the VPC dashboard, select `Subnets`
- `Create Subnet`
- Select your VPC from step 1 and create either Public or private subnet
- Name your subnet
- Add your IPV4 CIDR block
create

#### Step 4 - Create a Route table
- On the VPC dashboard, select Route Tables
- `Create Route Table`
- Link to VPC
- Once created, click on te route table and click subnet associations
- This is where you associate the routes to the Internet gateway
- Click edit routes
- Add new route
- `Destination 0.0.0.0/0`, `Target - Internet Gateway` - Save changes
- Edit subnet associations
- Add the subnet you have just created
![VPC 2](https://user-images.githubusercontent.com/115226294/200382339-dbc0a0ae-4386-4087-a0ad-373c3bd15e5b.png)
![VPC 3](https://user-images.githubusercontent.com/115226294/200382340-5de34b29-44b4-4bb3-b606-7b14ef45a7c7.png)


##### For Pirvate subnets
- Do not connect to internet gateway
![VPC 4](https://user-images.githubusercontent.com/115226294/200382379-12164b6c-8f35-4bde-9678-1becf05b9efd.png)

#### Step 5 - Launch your EC2 instance inside the VPC subnet
- Launch EC2
- Select appropriate AMI
- At network click edit and select your VPC and subnet
- Add script in user data to rune node app
```
#!/bin/bash

sudo apt-get update -y
sudo apt-get upgrade -y

sudo apt-get install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
```
Launch instance
#### In the app security group
Allow the following ports:
![VPC 5](https://user-images.githubusercontent.com/115226294/200382411-618e5377-ed28-4f93-b9a2-f8088f047c4a.png)

##### In the DB security group
Allow the following ports:
- Source for port 27017 must be the public subnet CIDR
![vpc 6](https://user-images.githubusercontent.com/115226294/200382445-abb3c624-19a7-40f0-b8d0-fb220a8694b9.png)

#### Step 6 Connect to app
- SSH into app instance
- cd into app folder
- Create a environment variable
- `export DB_HOST=mongodb://10.0.23.20:27017/posts`
- IP must be the private IPV4 address of DB EC2 instance
- Check if variable has been saved `printenv DB_HOST`
- Now seed the database `node seeds/seed.js`
- `npm start`
