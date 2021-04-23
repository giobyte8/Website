# Personal website

> Current development was moved to 'jekyllmigration' branch

This project contains my [personal web site](https://giovanniaguirre.me)

1. [Required setup steps](#Required-setup-steps)
2. [Run/Deployment](#Run/Deployment)
    * [Run on docker (Development)](#Run-on-docker-(Development))
    * [Run on docker (Production)](#Run-on-docker-(Production))
    * [Run on kubernetes](#Deploy-on-kubernetes)

## Required setup steps
1. Clone this repo
2. Setup your .env file:
   ```bash
   cd website/website
   cp .env.example .env
   vim .env
   ```
3. Add your own values for each key at `.env` file

In python 2, you can generate a key by running following commmand on your terminal:
```bash
python -c 'import random; print "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])'
```

In python 3 use:
```bash
python -c 'import random; print("".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]))'
```

## Run/Deployment
The project is configured to allow deployment on local environment through docker (For development), docker production, kubernetes and google app engine

### Run on docker (Development)

From project root:
```bash
cd docker
docker-compose up -d
``` 

A docker container will be started with the application shared as a volume, so every time you do a change in source code it will be immediately shown in running app.

Now go to [localhost:8000](http://localhost:8000)

*Note: For development, use `DEBUG=True` on your `.env` file in order to allow that django handles the statics paths. In production it should be handled through your web server*

### Run on docker (Production)
The production environment serves the application through
[Gunicorn](https://gunicorn.org) and [Nginx](https://www.nginx.com/)

From project root:
```bash
cd docker.production
docker-compose up -d
```

This will create two containers, one with gunicorn and another with nginx, all setup files are located on `docker.production` directory.

The application files and statics are copied into the images during build phase, so images need to be rebuilt and redeployed to reflect latest changes

### Deploy on kubernetes
The kubernetes config files are located at `k8config` folder

To deploy a new version of website the required steps are:
1. Build a new version of docker image(s):
    1. Update the images field value in the corresponding `docker-compose.yml` file to upgrade the image name
    2. Run `docker-compose build` in the path where the `docker-compose.yml` file exists
2. Upload generated image to your registry
3. Update corresponding kubernetes files to use the new image
    1. Update the `django-deployment.yml` file
    2. Update the `nginx-deployment.yml` file (If applies)
4. Apply changes on your cluster through `kubectl apply -f <updated-file.yaml>`

### Deploy to GAE
To deploy on google app engine standard environment, the setup is specified in the `app.yaml`. This file contains the entry point and the statics setup to deploy the application in GAE

Also, the `.gcloudignore` file contains a list of files that we won't to be uploaded to google cloud.

Ensure to setup the google cloud sdk and setup the project.
Setup the entrypoint field in the app.yaml and run `gcloud app deploy` in the path where the `app.yaml` file is located
