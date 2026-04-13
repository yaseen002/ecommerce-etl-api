# ecommerce-etl-api
An automated ETL pipeline that scrapes e-commerce data using BeautifulSoup, cleans unstructured records with Pandas, and exposes the processed data via a FastAPI REST API with PostgreSQL storage.

# E-commerce ETL API

## Overview
ETL pipeline + REST API that scrapes product data, loads it into PostgreSQL, and exposes it via FastAPI.

## Tech Stack
- FastAPI
- PostgreSQL (Docker)
- SQLAlchemy
- Alembic
- Docker & Docker Compose

## Features
- ETL pipeline (extract, transform, load)
- REST API for product data
- Database migrations using Alembic
- Containerized deployment

## Run with Docker
docker-compose up --build

## Run locally
uvicorn src.main:app --reload

## Run ETL pipeline
python run_pipeline.py

sudo apt install libpq-dev python3-dev build-essential