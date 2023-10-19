# Website development
Website is created using [hugo](https://gohugo.io/) static site generator

## Local development

### Prerequisites

- `npm` ([asdf](https://asdf-vm.com/) is the recommended way)
- `hugo`
  ```shell
  brew install hugo

  # Verify install
  hugo version
  ```

### Setup

1. Clone repo, move to `dev` branch and install dependencies
   ```shell
   git clone git@github.com:giobyte8/Website.git
   git checkout -b dev
   npm install
   ```
2. Prepare `.env` file and source it
   ```shell
   cp template.env .env

   # Enter appropriate values and source file
   vim .env
   source .env
   ```
3. Run `hugo` in dev mode
   ```shell
   hugo server -D
   ```

Get dev website address from terminal and add some awesome content

## Production build
Use `hugo` command to generate a production ready static website site with
minified css and javascript

```bash
source .env && hugo -e production
```

Above command will generate website to `public/` folder, you can host such
website in any http web server such as nginx.

## Production deployment (Using docker)
A production ready docker image is provided to serve the website using `nginx`
server

1. Build website by following [prod build guide](#production-build)
2. Build and run container `docker compose up -d --build`

Now you can setup a reverse proxy to route your own domain requests
to website container.

## Production deployment (Digital ocean)
Digital Ocean app is configured in `do/` directory. It listens for
`push` to `master` branch to trigger website build and update.

1. Merge `dev` branch into `master`
2. Digital ocean will build and deploy new version
3. Visit [giovanniaguirre.me](https://giovanniaguirre.me)
