# Personal website
This project contains my [personal web site](https://giovanniaguirre.me)

## Deployment steps
1. Clone this repo
2. Setup your .env file:
   ```bash
   cd website/website
   cp .env.example .env
   vim .env
   ```
3. Add your own values for each key at `.env` file

### For development:
Deploy/Run through docker:
```bash
cd docker
docker-compose up -d
``` 

A docker container will be started with the application shared as a
volume, so every time you do a change in source code it will be immediately
shown in running app.

Now go to [localhost:8000](http://localhost:8000)

*Note: For development use `DEBUG=True` on your `.env` file in order
to allow that django handles the statics paths. In production it should
be handled through your web server*

### For production
The production environment serves the application through
[Gunicorn](https://gunicorn.org) and [Nginx](https://www.nginx.com/)

The app runs on docker so you simply need to:
```bash
cd docker.production
docker-compose up -d
```

This will create two containers, one with gunicorn and another with
nginx, all setup files are located on `docker.production` directory

## Deploy through kubernetes
I use kubernetes to deploy the website to the cloud. All setup files are
located at `k8config` folder

To deploy a new version of website the required steps are:
1. Build a new version of docker image(s)
2. Upload generated image to your registry
3. Update corresponding kubernetes files to use the new image
4. Apply changes on your container through `kubectl apply -f <updated-file.yaml>`
