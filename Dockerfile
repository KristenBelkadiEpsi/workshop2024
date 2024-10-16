FROM python:3.9
WORKDIR /app
COPY . /app
RUN apt-get update
RUN apt-get install libmariadb3 libmariadb-dev -y
RUN pip3 install . --use-feature=fast-deps
RUN mariadb start
EXPOSE 9090
CMD ["python", "app.py"]