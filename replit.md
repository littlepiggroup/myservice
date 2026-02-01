# MyService API

## Overview
A simple FastAPI service that provides basic API endpoints for health checks and system information.

## Project Structure
- `main.py` - Main FastAPI application with endpoints
- `requirements.txt` - Python dependencies
- `fly.toml` - Fly.io deployment configuration (original import)

## Endpoints
- `GET /` - Returns basic service info and status
- `GET /health` - Health check endpoint
- `GET /info` - System information (Python version, hostname, port)

## Running Locally
The server runs on port 5000 using uvicorn:
```
python main.py
```

## Dependencies
- FastAPI >= 0.104.0
- Uvicorn >= 0.24.0

## Recent Changes
- 2026-02-01: Imported from GitHub and configured for Replit environment (port 5000)
