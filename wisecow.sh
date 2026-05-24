#!/bin/bash

PORT=4499

while true
do
    echo -e "HTTP/1.1 200 OK\r\n"

    fortune | cowsay | nc -l $PORT

done