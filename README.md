# Python Api Test

## Implementação de um API utilizando Python

- Python
- Flask
- MariaDB
- Docker/Docker Compose
- Nginx
- uwsgi

## Instalação

### **Copie esse repositorio**
```
git clone https://github.com/juliocmartins/simple-flask-api.git
```
### **No diretorio raiz execute o docker-compose para subir os serviços**
``` 
docker-compose up -d --build
```
### **Poupular banco de dados com as informações**

```
docker exec app_flask python manage.py seed
```
### **Acesse o Endpoint de check**
```
http://localhost/helthcheck
```

## Endpoints

---
### **Listar todos os pokemons cadastrados**
```
GET
http://localhost/pokemons
```
---
### **Pegar um pokemon pelo Id cadastrado**
```
GET
http://localhost/pokemons/<int:id>
```
---
### **Listar todos os treinadores cadastrados**
```
GET
http://localhost/trainers
```
---
### **Pegar um treinador e seu time pelo Id cadastrado**
```
GET
http://localhost/trainers/<int:id>/
```
---
### **Cadastrar um novo treinador**
```
POST
http://localhost/trainers
```
---
### **Atualizar um treinador pelo Id cadastrado**
```
PUT
http://localhost/trainers/<int:id>
```
---
### **Excluir um treinador pelo Id cadastrado**
```
DELETE
http://localhost/trainers/<int:id>
```
---
### **Cadastrar um time para um trainador cadastrado**
```
POST
http://localhost/trainers/<int:id>/team
```
---
### **Atualizar um time de um trainador cadastrado**
```
PUT
http://localhost/trainers/<int:id>/team
```
---
### **Deletar um time de um trainador cadastrado**
```
DELETE
http://localhost/trainers/<int:id>/team
```

# Justificativa

### Python
Uma linguagem que venho aprendendo nos ultimos meses, procuro consolidar o conhecimento, trazendo a bagagem de outras linguagens

### Flask
Por ser um mivro framework nos obriga a fazer muita coisa manualmente. Assim para um apredizado inicial é ideal para fortalecer e fixar o conhecimento ao longo do estudo.

### MariaDB 
Um dos bancos usandos em larga escala, foi escolhido para persisitir os dados da API e representar um acesso de banco externo.

### Docker
Ao usar os serviços da aplicação separados podemos usar uma estrutura escalavel e de facil manutenção