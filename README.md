# vqa-e2e
End to end visual question and answering application

## Docker Commands

Building docker 

`docker build -t vqa-e2e .`

Running docker

`docker run -p 8501:8501 -p 8000:8000 vqa-e2e`

Running docker interactive, **//** is important to turn off GitBash's automatic path conversion

`docker run -it --rm vqa-e2e //bin/bash`

Streamlit App
> localhost:8501

FastAPI
> localhost:8000/docs

## Kubernetes

Save the Docker image locally

`docker save vqa-e2e:latest -o image.tar`

Use Minikube's docker daemon via minikube ssh to load the image.
This command will SSH into the Minikube VM and execute the docker load command to load the Docker image from the image.tar file.

`minikube ssh -- docker load -i image.tar`

Create a Kubernetes deployment using the loaded Docker image.

`kubectl apply -f deployment.yaml`
