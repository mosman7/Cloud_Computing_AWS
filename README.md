# Cloud Computing
### What is it?
Cloud computing is the delivery of computing services - including servers, storage, databases, networking, software, analytics, and intelligence - over the Internet. It offers faster innovation, flexible resources, and economies of scale. You typically pay only for cloud services you use, helping to lower operating costs, run infrastructure more efficiently, and scale as businesses need change.

Cloud computing is on-demand delivery of IT resources over the internet with pay-as-you-go pricing. Instead of buying, owning, and maintaining physical data centers and servers, you can access technology services, such as computing power, storage, and databases, on an as-needed basis from a cloud provider like Amazon Web Services (AWS).

### What are its benefits?

![benefits](https://thinkitsolutions.com/wp-content/uploads/2019/02/Benefits-of-Cloud-Computing.png)

Agility
- The cloud gives you easy access to a broad range of technologies so that you can innovate faster and build nearly anything that you can imagine. You can quickly spin up resources as you need them–from infrastructure services, such as compute, storage, and databases, to Internet of Things, machine learning, data lakes and analytics, and much more.
Deploy technology services in a matter of minutes

Elasticity
- With cloud computing, you don't have to over provision resources up.
Instead, you can provision the amount of resources that you actually need, scale the resources up or down to instantly grow or shrink capacity

Cost
- The cloud allows you to trade fixed expenses (such as data centers and physical servers) for variable expenses, and only pay for IT as you consume it. Variable expenses are much lower than what you would pay to do it yourself.
Deploy globally
With the cloud, you can expand to a new geographic regions and deploy within minutes, just with a few clicks.


### PAAS, SAAS, IAAS

![](https://www.volico.com/wp-content/uploads/2017/08/IaaS-Saas-and-PaaS.jpg)

Three main types of cloud computing include Infrastructure as a Service, Platform as a Service, and Software as a Service. Each type of cloud computing provides different levels of control, flexibilty, and management so that you can select the right set of services for your needs.

Infrastructure as a Service (IaaS)
- Infrastructure as a service, is on-demand access to cloud-hosted physical and virtual servers, storage and networking - the backend IT infrastructure for running applications and workloads in the cloud.

Platform as a Service (PaaS)
- Platform as a service, is on-demand access to a complete, ready-to-use, cloud-hosted platform for developing, running, maintaining and managing applications.

Software as a Service (SaaS)
- Software as a service, is on-demand access to ready-to-use, cloud-hosted application software.

![IAAS](https://www.redhat.com/cms/managed-files/iaas-paas-saas-diagram3-1638x1046.png)

### Cap-Ex VS Op-Ex

Capital expenditures (CapEx) are a company's major, long-term expenses, while operating expenses (OpEx) are a company's day-to-day expenses.

![Cap-ex](https://blog.comindware.com/wp-content/uploads/2018/12/capex-vs-opex.png)

### Amazon Machine Image (AMI)
An Amazon Machine Image (AMI) provides the information required to launch an instance. You must specify an AMI when you launch an instance. You can launch multiple instances from a single AMI when you need multiple instances with the same configuration. You can use different AMIs to launch instances when you need instances with different configurations.

### Disaster Recovery
AWS provides a range of disaster recovery stratgies to help you recover from a disaster. These can be broadly divided into four categories:
- low cost and low complexity, such as Amazon S3 to store backups
- low high and high complexity, such as having a standby environment in different active regions
- Active Sites, such as an AWS Region to host the workload and serve traffic.
- Passive Sites, such as a different AWS Region is used for recovery. The passive site does not actively serve traffic until a failover event is triggered.

### S3

S3 is an object storage service that stores data as objects within buckets. An object is a file and any metadata that describes the file. A bucket is a container for objects.

To store your data in Amazon S3, you first create a bucket and specify a bucket name and AWS Region. Then, you upload your data to that bucket as objects in Amazon S3. Each object has a key (or key name), which is the unique identifier for the object within the bucket.


#### Autoscaling
- Autoscaling automaticlly adjusts the amount of computational resources based on the server load
- autoscaling policy - decides what to do to distribute traffic - scale up, down, in or out
    - it scales in and out - adding more instances
    - it scales up and down - adding more resources
Benefits:
- Better fault tolerance. Amazon EC2 Auto Scaling can detect when an instance is unhealthy, terminate it, and launch an instance to replace it. 
- Better availability. Amazon EC2 Auto Scaling helps ensure that your application always has the right amount of capacity to handle the current traffic demand.
- Better cost management. Amazon EC2 Auto Scaling can dynamically increase and decrease capacity as needed. Because you pay for the EC2 instances you use, you save money by launching instances when they are needed and terminating them when they aren't.


#### Load Balancing
- Load Balancing distributes traffice between ec2 instances so that no one instance gets overwhelmed
Benefits:
- Using a load balancer increases the availability and fault tolerance of your applications.
- You can add and remove compute resources from your load balancer as your needs change, without disrupting the overall flow of requests to your applications.
- You can configure health checks, which monitor the health of the compute resources, so that the load balancer sends requests only to the healthy ones. 