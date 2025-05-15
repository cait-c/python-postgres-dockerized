# 🐳 Python + PostgreSQL App

A minimal Dockerized Python script with a PostgreSQL database (viewable in PGAdmin) for seeding and performing basic CRUD operations using SQLAlchemy — no API, just simple code execution.

## Repo Structure

```
python-postgres-dockerized/
├── docker-compose.yml
├── init.sql
├── app/
│ ├── Dockerfile
│ ├── main.py
│ └── requirements.txt
```

## 🚀 Quick Start

From the root of the repo:
`docker-compose up --build`

## 🧑‍💻 PGAdmin Connection Instructions

To connect to the Postgres database using PGAdmin:

Host: localhost
Port: 5432
Username: myuser
Password: mypassword
Database: mydb
