FROM nginx:latest
COPY ./index.html /usr/share/nginx/html/index.html
COPY ./commitphoto.jpg /usr/share/nginx/html/Commit/
COPY ./app.py /python/
COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/nginx.conf
RUN apt update
RUN apt install python3 -y
RUN apt install pip -y
RUN pip install mysql-connector-python --break-system-packages
RUN pip install flask --break-system-packages
EXPOSE 80
EXPOSE 8080
CMD nginx && python3 /python/app.py
