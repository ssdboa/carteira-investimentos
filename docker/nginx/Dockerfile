# docker/nginx/Dockerfile

# Começamos com uma imagem oficial e leve do Nginx
FROM nginx:1.28-alpine

# Remove a configuração padrão do Nginx que vem na imagem
RUN rm /etc/nginx/conf.d/default.conf

# Copia nosso arquivo de configuração customizado para o local correto dentro do contêiner
COPY nginx.conf /etc/nginx/conf.d/
