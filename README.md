HNG Stage 0 — Dynamic Profile Endpoint

A FastAPI endpoint /me that returns your profile info and a dynamic cat fact from Cat Facts API
.

Features

GET /me returns JSON:

{
  "status": "success",
  "user": { "email": "...", "name": "...", "stack": "..." },
  "timestamp": "...",
  "fact": "..."
}


Dynamic UTC timestamp in ISO 8601 format

Fetches a new cat fact on every request

Handles API failures gracefully

CORS enabled and basic logging added

Setup

Clone repo:

git clone <repo-url>
cd hng-stage0-backend


Create & activate virtual environment:

python -m venv venv
source venv/Scripts/activate  # Git Bash/Windows


Install dependencies:

pip install -r requirements.txt


Add .env:

EMAIL=your_email@example.com
NAME=Your Full Name
STACK=Python/FastAPI


Run locally:

uvicorn main:app --reload


Access: http://127.0.0.1:8000/me

Deployment

Supports Railway / Heroku / PXXL App

Set environment variables in platform settings

Endpoint ready to test live

Dependencies

fastapi, uvicorn, httpx, python-dotenv

Author: Collinsthegreat
