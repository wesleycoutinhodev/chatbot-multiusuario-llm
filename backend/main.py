from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from datetime import datetime

app = FastAPI(
    title="Chatbot_TCA",
    description="API para chatbot com múltiplas sessões",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return{
        "message":"Chatbot Multiusuário API",
        "docs":"/docs",
        "health":"/health"
    }

@app.get("/health")
async def health_check():
    return {
        "status":"ok",
        "timestamp": datetime.now().isoformat(),
        "service":"chatbot_api"
    }