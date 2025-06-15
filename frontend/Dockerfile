# frontend/Dockerfile

# ---- Estágio de Build ----
FROM node:22-alpine AS builder
# Usamos a versão 22 do Node (LTS ativa que você mencionou) com Alpine para uma imagem de build menor.

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia package.json e package-lock.json (ou yarn.lock se você usar yarn)
COPY package*.json ./

# Instala as dependências do projeto
RUN npm install

# Copia o restante dos arquivos da aplicação para o diretório de trabalho
COPY . .

# Constrói a aplicação para produção
# O Vite coloca os arquivos de build na pasta 'dist' por padrão
RUN npm run build

# ---- Estágio de Serviço (Runtime) ----
FROM nginx:1.27-alpine
# Usamos uma imagem Nginx Alpine, que é bem leve.

# Copia os arquivos estáticos construídos do estágio 'builder' para o diretório padrão do Nginx
COPY --from=builder /app/dist /usr/share/nginx/html

# (Opcional, mas recomendado) Remove a configuração padrão do Nginx
RUN rm /etc/nginx/conf.d/default.conf

# Copia uma configuração customizada do Nginx (vamos criar este arquivo em seguida)
COPY nginx.conf /etc/nginx/conf.d

# Expõe a porta 80 (porta padrão do Nginx)
EXPOSE 80

# Comando para iniciar o Nginx em primeiro plano
CMD ["nginx", "-g", "daemon off;"]