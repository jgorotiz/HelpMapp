FROM python:3-buster
# Instalar utilidades
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log
# Crear directorios para la app
RUN mkdir -p /opt/app
# Copiar requirements en app
COPY requirements.txt start-server.sh /opt/app/
COPY . /opt/app/helpmapp
WORKDIR /opt/app
RUN pip install -r requirements.txt
RUN cd helpmapp && python manage.py collectstatic --clear --no-input
RUN chown -R www-data:www-data /opt/app
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]