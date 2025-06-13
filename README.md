<h1 align="center">🛒 Meu Site Vendas</h1>
<p align="center">
  Sistema de vendas online desenvolvido em Django.
</p>


---

## 🧠 Objetivo

Este projeto foi desenvolvido em dupla com o Felipe de Souza Carvalho para a disciplina **Desenvolvimento Web III** do curso de **Desenvolvimento de Software Multiplataforma**, com o intuito de aplicar conhecimentos em:

- Django (Python)
- Bootstrap 5
- Consumo de APIs externas (FakeStore e ViaCEP)
- Templates e herança de layout
- Controle de sessão e autenticação
- CRUD de usuários e produtos
- Gráficos com Chart.js

---

## 🚀 Como executar o projeto

--- Em todos os comandos se atentar a qual versão do python você tem instalada na sua máquina (python, python3 e py podem funcionar) ---

1. Crie um ambiente virtual:

   python -m venv ambienteVirtual<br>
   ambienteVirtual\Scripts\activate

2. Instale as dependências:
 
   python -m pip install django<br>
   python -m pip install pillow<br> 
   python -m pip install requests

3. Aplique as migrações:
  
   python manage.py makemigrations<br>
   python manage.py migrate
 

4. Crie um superusuário (opcional, para acessar o admin):
   
   python manage.py createsuperuser
   

5. Rode o servidor:
   
   python manage.py runserver
   

6. Acesse no navegador: `http://127.0.0.1:8000/`
