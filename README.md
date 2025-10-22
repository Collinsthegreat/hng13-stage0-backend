# HNG Stage 0 Backend — Dynamic Profile Endpoint

A FastAPI endpoint `/me` that returns profile info and a dynamic cat fact.

## Live Endpoint
https://hng13-stage0-backend-production-5902.up.railway.app/me

## Setup
1. Clone repo:
```bash
git clone https://github.com/Collinsthegreat/hng13-stage0-backend.git
cd hng13-stage0-backend

python -m venv venv
source venv/Scripts/activate  # Windows Git Bash

pip install -r requirements.txt

Add .env for EMAIL, NAME, STACK

Run locally:

uvicorn main:app --reload

Author

Abuchi Collins