# E-Commerce ETL API (FastAPI + PostgreSQL + Docker + CI/CD)

## Project Overview

This project is a containerized ETL-style backend API built using FastAPI and PostgreSQL.
It demonstrates a production-style backend architecture including schema migrations, integration testing, Dockerized services, and automated CI validation using GitHub Actions.

The system extracts product data, transforms it into structured format, stores it in PostgreSQL, and exposes it through REST API endpoints.

---

## Tech Stack

Backend Framework:

* FastAPI

Database:

* PostgreSQL

ORM:

* SQLAlchemy

Migration Tool:

* Alembic

Testing:

* pytest
* httpx

Containerization:

* Docker
* Docker Compose

CI/CD:

* GitHub Actions

---

## Features

* Modular FastAPI backend architecture
* PostgreSQL database integration
* SQLAlchemy ORM models
* Alembic schema versioning
* Dockerized multi-service setup
* Integration testing with pytest
* Automated CI pipeline with PostgreSQL service container
* Docker image build validation inside CI

---

## Project Structure

```
src/
 ├── api/
 ├── database/
 ├── config/
 ├── scraper/
 ├── etl/
 └── main.py

tests/
alembic/
docker-compose.yml
Dockerfile
requirements.txt
```

---

## API Endpoints

Create product:

POST /products

Retrieve products:

GET /products

---

## Running Locally

Start services:

```
docker-compose up --build
```

Run migrations:

```
alembic upgrade head
```

Run tests:

```
pytest
```

Start API manually:

```
uvicorn src.main:app --reload
```

---

## CI Pipeline

The GitHub Actions workflow performs:

* dependency installation
* PostgreSQL service startup
* database readiness verification
* Alembic migrations execution
* FastAPI import validation
* integration testing
* Docker image build verification

This ensures the backend is reproducible and deployment-ready.

---

## Learning Outcomes

This project demonstrates:

* backend API design using FastAPI
* relational schema management with PostgreSQL
* migration workflows using Alembic
* containerized development with Docker
* multi-service orchestration using Docker Compose
* integration testing with pytest
* automated CI pipelines with GitHub Actions

---

## Future Improvements

Potential enhancements include:

* authentication layer (JWT)
* Redis caching
* async ETL scheduler
* deployment to cloud infrastructure
* health-check endpoint
* monitoring integration

---