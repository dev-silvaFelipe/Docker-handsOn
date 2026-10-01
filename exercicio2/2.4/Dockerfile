FROM node:18 AS builder
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .

FROM node:18-alpine
WORKDIR /app

COPY --from=builder /app/index.js .

CMD ["node", "index.js"]