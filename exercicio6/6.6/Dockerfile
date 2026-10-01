FROM alpine:latest

RUN addgroup -S meugrupo && adduser -S meusuario -G meugrupo

USER meusuario

CMD ["whoami"]