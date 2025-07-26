# Example Dockerfile for NGINX
FROM nginx:alpine
COPY ./index.html /usr/share/nginx/html/index.html