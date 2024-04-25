# Use NGINX as base image
FROM nginx:latest

# Remove the default NGINX index.html
RUN rm -rf /usr/share/nginx/html/*

# Create a dummy HTML file
RUN echo "<html><body><h1>Hello, World!</h1><p>This is a dummy text.</p></body></html>" > /usr/share/nginx/html/index.html

# Expose port 80 to the outside world
EXPOSE 80

# Command to start NGINX server
CMD ["nginx", "-g", "daemon off;"]
