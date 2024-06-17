# Mask Detection using YOLOv8


https://github.com/Amandeepsinghn/mask_detection_2.0/assets/137553469/f841efd7-3093-470f-8a96-09af92abec3a





## Workflow

1) Update config.yaml 
2) Update secrets.yaml [Optional]
3) Update params.yaml
4) Update the entity
5) Update the configuration manager in src config 
6) Update the components 
7) Update the pipeline
8) Update the main.py 



## How to run?

STEPS:
Clone the repository
```bash
  https://github.com/Amandeepsinghn/Resume_Type.git
```
STEP 01- Create a conda environment after opening the repository
```bash
  conda create -n resume python=3.8 -y
```
```bash
  conda activate resume
```
STEP 02- install the requirements
```bash
  pip install -r requirements.txt
```
```bash
  # Finally run the following command
  python app.py
```

## AWS-CICD-Deployment-with-Github-Actions

1. Login to AWS console.

2. Create IAM user for deployment
```bash
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
```
3. Create ECR repo to store/save docker image
```bash
- Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/flight_price
```
4. Create EC2 machine (Ubuntu)

5. Open EC2 and Install docker in EC2 Machine:
```bash
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```
6. Configure EC2 as self-hosted runner:
```bash
setting>actions>runner>new self hosted runner> choose os> then run command one by one
```
7. Setup github secrets:
```bash
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app
