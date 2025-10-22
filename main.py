from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import httpx
from datetime import datetime
import os
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logging.info("API is starting...")

# FastAPI app
app = FastAPI()

# Add CORS middleware (allow frontend calls)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Change to specific origins if needed
    allow_methods=["GET"],
    allow_headers=["*"]
)

# Environment variables
EMAIL = os.getenv("EMAIL")
NAME = os.getenv("NAME")
STACK = os.getenv("STACK")

# Cat facts API
CAT_API_URL = "https://catfact.ninja/fact"

@app.get("/me")
async def get_profile():
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.get(CAT_API_URL)
            response.raise_for_status()
            data = response.json()
            cat_fact = data.get("fact", "Cats are mysterious creatures 🐱")
    except Exception:
        cat_fact = "Unable to fetch cat fact at the moment. 😿"

    logging.info("Profile endpoint accessed")  # Log each request

    return JSONResponse(
        content={
            "status": "success",
            "user": {
                "email": EMAIL,
                "name": NAME,
                "stack": STACK
            },
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "fact": cat_fact
        }
    )
