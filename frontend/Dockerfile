FROM node:23

WORKDIR /app
COPY . /app/

RUN npm ci

EXPOSE 3000

CMD ["npm", "run", "dev"]