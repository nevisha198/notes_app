FROM ubuntu:latest

RUN apt-get update && \
     apt install -y nginx

COPY nginx.conf /etc/nginx/sites-available/default
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
