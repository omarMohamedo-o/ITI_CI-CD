# Use the official Nginx base image
FROM nginx:latest

# Copy a custom index.html for a simple welcome page (optional)
COPY ./index.html /usr/share/nginx/html/index.html

# Expose port 80 for HTTP traffic
EXPOSE 80

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]