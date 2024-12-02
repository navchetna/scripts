# Full Stack Project (level 2)

This is a full-stack project that is a blog site. It has a backend written in python using FastAPI, a frontend written in TS using React, and a database written in mysql.

## Prerequisites

- Docker
- Node.js
- Python3


```
cd full-stack/L2;
```


## Database

This is the database of the full-stack app. It is a mysql database running as a docker container.

### Setup

```
cd db;
docker compose -f docker-compose.yaml up
```

## Backend

This is the backend of the full-stack app written in python leveraging FastAPI.
It is capable of performing CRUD operations on the blog data.
Here, the data is stored in mysql database running as docker container.

### Setup

```
cd backend;
pip install -r requirements.txt;
prisma generate --schema=/handlers/database/schema.prisma 
prisma db push --schema=/handlers/database/schema.prisma 
python3 main.py;
```

## Frontend

This is the frontend of the full-stack project. It is a TS application that uses that renders a blog site.
It has default blogs that are embedded in UI.

### Setup

```
cd frontend;
npm install;
npm run dev;
```

<i>Navigate to [localhost:3000](http://localhost:3000) to view the frontend.</i>
