#!/bin/bash

# Instalar as dependências do frontend
cd frontend
npm install
cd ..

# Instalar as dependências do backend
cd api
pip install flask flask-cors unidecode

# Iniciar o backend
python app.py &
sleep 5
cd ..

# Iniciar o frontend
cd frontend
npm run dev
sleep 10
