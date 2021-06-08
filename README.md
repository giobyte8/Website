# Personal website

This is my personal [website](https://giovanniaguirre.me), which is
created using 'hugo' static site generator and javascript

## Setup

1. Clone this repo
2. Create `.env` file
    1. Copy template with: `cp env.example .env`
    2. Replace `.env` variables values with your own
3. source `.env` file with: `source .env`

## Local development

> Make sure to source `.env` file before develop

1. Install hugo.
2. From project root, execute: `hugo server -D`
3. Check terminal output and add some awesome content

## Production build

> Make sure to source `.env` file before run production
> build

Run `hugo` command from project root:
```bash
hugo
```

This will generate `public` directory containing website
ready for deployment on production

## Production deploy (Docker)

> Note: Make sure to build for production before create docker
> container

1. Upgrade image tag in `docker.production/docker-compose.yml`
2. Use docker compose to start website container: `docker-compose up -d`
    - This will build image, tag it with new version and will start
      the container
