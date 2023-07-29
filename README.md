# FastAPI Template

Table of Contents
* [Description](#description)
* [Features](#features)
	* [Schema](#schema)
	* [Database](#database)
	* [API](#api)
		* [Versioning](#versioning)
	* [Config](#config)
		* [Environment Variables](#environment-variables)
		* [Settings](#settings)
	* [Logging](#logging)
* [Testing](#testing)



## Description

## Features
### Modules

Modules don't have any dependencies between them, they are independent.
New objects for dependencies are created in deps.py file.

```
app
├── core
│   ├── config.py
└── modules
    ├── api
		│   ├── v1
		│   │   ├── api.py
    │   ├── deps.py
    │   └── routes.py
    ├── db
		│   ├── deps.py
		│   └── session.py
		└── items
		    ├── deps.py
		    ├── service.py
		    ├── routes.py
		 		└── schemas.py
```


#### Dependencies (deps)
We use Dependency Injection, each module has file deps.py.
How to import module dependencies:

```mermaid


```
#### Schema

#### Database Module
##### Create Table
Create table query for PostgreSQL:

```sql
CREATE TABLE IF NOT EXISTS items (
	id SERIAL PRIMARY KEY,
	title VARCHAR(255) NOT NULL,
	description VARCHAR(255) NOT NULL
);
```
##### Insert Data
Insert data query for PostgreSQL:

```sql
INSERT INTO items (title, description) VALUES ('Item 1', 'Description 1');
```


### API
#### Versioning

### Config
#### Environment Variables
#### Settings

### Logging
### Testing

## Docker

Build image:
```bash
docker build . --tag gcr.io/fastapi-template-394307/fastapi-template
```

Run container:
```bash
docker run -p 5000:8080 gcr.io/fastapi-template-394307/fastapi-template

```


## Google Cloud Run Deployment
Deploy to Google Cloud Run:
```bash
gcloud builds submit --tag gcr.io/fastapi-template-394307/fastapi-template
```

```bash
gcloud run deploy --image gcr.io/fastapi-template-394307/fastapi-template --platform managed
```


## Performance Testing
### Locust
#### Installation
```bash
pip install locust
```
#### Run
```bash
locust -f locustfile.py
```
