# How to set up an EC2 instrance

- Log in to the AWS web console
- Go to EC2 dashboard and select instances
- Click on Launch instance
- ![]("C:\Users\moham\Pictures\Instance.png")
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