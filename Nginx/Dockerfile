FROM nginx:latest

RUN apt-get update && apt-get install -y openssl && apt-get clean

RUN mkdir -p /etc/nginx/ssl && \
    openssl req -x509 -nodes -days 365 \
    -newkey rsa:2048 \
    -keyout /etc/nginx/ssl/privkey.pem \
    -out /etc/nginx/ssl/fullchain.pem \
    -subj "/CN=adios_caries_api"

COPY ./nginx.conf /etc/nginx/nginx.conf
