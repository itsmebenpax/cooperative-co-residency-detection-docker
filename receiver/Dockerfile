FROM gcc
FROM python
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN gcc -o app main.c
CMD ["./script.py"]
