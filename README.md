Requirements
1. Your solution MUST be containerized.
2. You must have a deployment template for your solution.
3. Our preference is for your solution to be written in Python or Node.js (in that order).
4. You should provide detailed instructions on how to launch your solution locally.
5. Please try not to spend well over 2 hours on this assessment.
6. If anything is unclear, please state your assumptions



Prerequisites

Install minikube on your local machine:
● https://minikube.sigs.k8s.io/docs/start/
● https://docs.okd.io/3.11/minishift/getting-started/installing.html





Minishift was not used for this implementation, due to its lack of support for Python 3.7, which is required for FastAPI. Minikube, however, is able to be used. 




# Build docker image

`docker image build -t api-server .`




This was ran on WSL 2 Ubuntu with Docker as the default driver. 

To start the cluster, use 

`minikube start --driver=docker`


or set Docker as your default driver with:

`minikube config set driver docker`





This was developed with Python3.8 and mkvirtualenv

Run the command 

`mkvirtualenv -p /usr/bin/python3.8 `



Also utilized the in-cluster Docker daemon (docker-env) for faster development/deployment. 

To do this, run:

`eval $(minikube docker-env)`





To spin up the Kubernetes deployment and service:

`kubectl apply -f src/api.yaml`




To view resources, run this command to see the dashboard:

`minikube dashboard`


 6400* minikube delete
 6401* minikube start

To make queries against the cluster locally, run:

`minikube tunnel`

Then run 

`kubectl get svc api-server-svc`

and use the external ip address when making HTTP
requests via curl or a tool like Postman 


