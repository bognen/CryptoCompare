FROM node:lts-alpine

# устанавливаем простой HTTP-сервер для статики
RUN npm install -g http-server
WORKDIR /app
COPY package*.json ./

RUN npm install
COPY . .

RUN npm run build

EXPOSE 80

#CMD ["http-server", "dist", "--port", "80"]
CMD ["/app/script.sh"]
