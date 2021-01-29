#! /bin/sh

touch .env
echo "VUE_APP_DATA_URL="$VUE_APP_DATA_URL >> .env
echo "VUE_APP_RAPID_KEY="$VUE_APP_RAPID_KEY >> .env

http-server dist --port 80
