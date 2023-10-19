FROM nginx:1.25-alpine
EXPOSE 80
WORKDIR /var/www

# Copy website contents into workdir
ADD ./public /var/www/
ADD ./docker.production/vhost.conf /etc/nginx/conf.d/default.conf
