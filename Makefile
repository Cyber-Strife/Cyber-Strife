# Makefile for Cyber Strife project

install:
    pip install -r requirements.txt
    npm install

start:
    flask run

test:
    pytest tests/

build:
    npm run build

deploy:
    python scripts/deploy.py
