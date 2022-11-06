#### How to set up autoscaling with AMI

- On AWS console select launch templates
- create launch template
- name the template
- for OS selection use your saved AMI
- in advanced details -add script
```
#!/bin/bash
cd home/ubuntu/app - cd to location where app.js is to start app
npm start
```
- go to instance created and click on ip
- app should launch straight away


## Cloudwatch
To create an alarm go to the Cloud Watch tab
- Click on "All alarms" on the left under Alarms
- Click "Create Alarm"
- Under "Select metric" - Select EC2
Now in select metric:
- Select "By Auto Scaling Group"
- Search for your ASG and select the wanted alarm trigger (e.g. CPU utilisation)
- When selected all, click Select Metric and provide details
- Threshold value is a percentage set to required percentage
- Select "In alarm"
- Select or create an existing topic
- Name the alarm and add any extra message as this will be emailed to you
- Review all details and ensure all provided date is correct
- Create your alarm