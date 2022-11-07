steps
1. create a VPC 10.0.0.0/16
2. create an internet gateway
    - attach the internet gateway to out VPC
3. create a public subnet 10.0.1.0/24
4. create a route table
    - add routes to connect to internet gateway  0.0.0.0/0
    - associate route table to public subnet
5. Launch new ec2
6. create a new sg

launch node app using VPC

launch ec2 instance with app ami
connect to vpc and public subnet
launch app

launch ec2 instance with db ami
connect to vpc and create private subnet
create sg - allowing port 22 for my ip and 27017 for public subnet cidr
launch instance

go to route table
connect to internet gateway 0.0.0.0
associate route table to private subnet
check status of db

## Setting up a VPC
#### Step 1 - Create a VPC
On the AWS console, go to VPC
`Create VPC`
Add your name tag, input IPV4 CIDR block and create VPC
vpc1

#### Step 2 - Create an Internet Gateway
On the VPC dashboard, select `Internet Gateway`
Add your name tag and click `Create Internet Gateway`
Once created, click `Action` and link to VPC created in step 1

#### Step 3 -  Create a subnet
On the VPC dashboard, select `Subnets`
`Create Subnet`
Select your VPC from step 1 and create either Public or private subnet
name your subnet
add your IPV4 CIDR block
create

#### Step 4 - Create a Route table
On the VPC dashboard, select Route Tables
`Create Route Table`
Link to VPC
Once created, click on te route table and click subnet associations
This is where you associate the routes to the Internet gateway
click edit routes
Add new route
`Destination 0.0.0.0/0`, `Target - Internet Gateway` - Save changes
Edit subnet associations
Add the subnet you have just created
VPC 2&3

##### For Pirvate subnets
- Do not connect to internet gateway
vpc 4

#### Step 5 - Launch your EC2 instance inside the VPC subnet
Launch EC2
Select appropriate AMI
At network click edit and select your VPC and subnet
Add script in user data to rune node app
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
VPC 5

##### In the DB security group
Allow the following ports:
Source for port 27017 must be the public subnet CIDR
VPC 6

#### Step 6 Connect to app
SSH into app instance
cd into app folder
create a environment variable
`export DB_HOST=mongodb://10.0.23.20:27017/posts`
IP must be the private IPV4 address of DB EC2 instance
check if variable has been saved `printenv DB_HOST`
Now seed the database `node seeds/seed.js`
`npm start`
