# Autoblog generation Workflow 

## We have 3 fases for Autoblog generation project 

Based on GPT-2 model, we create our own custom dataset to perform autoblog generation. 

Our end goal is to request from a topic to the model and receive an article that we can later publich in our website. 

With customs parameters also request information from the model and receive a template based on that request 

## Fases 

* 1- Collecting data daily from target websites 
* 2- Training that data to get our custom model 
* 3- Deploying the app to the end user 


# 1- Collecting the data

WILLIAM, PLEASE EXPLAIN THE PROCESS HERE

## Resources used 

Ubuntu VM is provisioned with: 

* 2 vCPU 
* 2 GB RAM 
* 20GB SSD 

This VM will be running 24/7 and the only job it will perform is to run the webscrapping to collect the DATA and once in a week it will copy de DATA to our data_storage server to an specific location. 


# 2- Training that data to get our custom model 

At this stage we will copy the data train the model gpt-2 with it, once training is finish it will create a checkpoint folder with the model inside, then we move the checkpoint folder to the models/ to get it ready for deployment. 

## Resources used 

Ubuntu VM is provisioned with: 

* 8 vCPU  
* 16 GB RAM 
* 200 GB SSD 
* 2x RTX 2080 Ti 

On this VM we need to use GPUs since for faster and better accuracy on training GPUs will really speed up the process. Currently the model when raining is being used 8GB of Vram on GPU but once it gets bigger it will use more memory. 


# 3- Deploying the app to the end user 

This is the final stage where we are going to test the new model deployed and build the docker container to upload the latest version of our app. 

IMPORTANT: The deployment container will include 2 containers that link together 

* gpt-dlbt container 
* API server container 

## Apps used for deployment 

* API server request 
* Front end app on Technopremium.com ( this will communicate with API server ) 
* Dockerhub ( final container will be uploaded to dockerhub for easy deployemnt ) 
* Dockerfile ( Hosted on Github to automate the build times for the container ) 

## Resources used 

Ubuntu VM is provisioned with: 

* 8 vCPU  
* 16 GB RAM 
* 200 GB SSD 
* 4x GTX 1060 6GB Vram ( This will allow us to run 4 prompts at the same time ) 

# Running training and deployment containers 

## Training container steps to launch 

Copy the dataset.txt collected from the step 1 and copy into '/home/william/gpt-2'

Launch the Tensorflow container 

```bash
sudo docker images 
sudo nvidia-docker run -v ~/gpt-2:/workspace/work/gpt-2 -it --shm-size=1g --ulimit memlock=-1  --ulimit stack=67108864 --rm 621fd859db333
```

Once inside the container we are going to navigate to '/workspace/work/gpt-2' and install few dependencies 

```bash 
pip3 install gpt_2_simple
```

Then start the training 
```bash 
python3 trainer.py 
```

Once the training has finished then look for a '/workspace/work/gpt-2/checkpoint' folder this is where the new model was saved. 


## Deploying container steps to launch 

Now that we have our new model we need to rebuild a container with this file, we just need to launch the Dockerfile and it will build the container with the new model on it. 

Once the container is created we can launch it for testing: 

```bash 
sudo nvidia-docker run -e NVIDIA_VISIBLE_DEVICES=1 -it --shm-size=1g --ulimit memlock=-1  --ulimit stack=67108864 gpt-dlbt:v_1.0 
``` 

Where -e NVIDIA_VISIBLE_DEVICES=1 will launch on an specific GPU, this allow multiple user to use the model at the same time allocating the model on different GPUs. 

After testing that all its working we need to upload the container to our dockerhub page to share it with the WORLD. 
