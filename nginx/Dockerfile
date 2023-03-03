FROM nginx:alpine
RUN rm -rf /etc/nginx/conf.d/default.conf
#COPY nginx.conf /etc/nginx/conf.d/nginx.conf
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD ["nginx", "-g", "daemon off;"]