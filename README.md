below is all ai generated i didnt write this. will update as i add functionality

# Archibald - AI Assistant for Calendar and Email

This project sets up a local AI model on your NVIDIA 5070ti GPU to provide suggestions and work assistance by ingesting calendar and email data.

## Setup

1. Ensure you have Python 3.8+ installed.
2. Install CUDA toolkit if not already installed (for GPU support). Current setup runs on CPU.
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `python -m uvicorn src.app:app --reload`

## API

- GET / : Health check
- POST /generate : Generate response from prompt

API documentation available at http://127.0.0.1:8000/docs when running.

### Query Examples

To query the application, send a POST request to `/generate` with a JSON body containing the `prompt`.

Using PowerShell (Invoke-WebRequest):
```
Invoke-WebRequest -Uri "http://127.0.0.1:8000/generate" -Method POST -Body '{"prompt": "Summarize my day"}' -ContentType "application/json"
```

Using curl (in bash/cmd, if installed):
```
curl -X POST "http://127.0.0.1:8000/generate" -H "Content-Type: application/json" -d '{"prompt": "What are my upcoming meetings?"}'
```

## Features

- Local AI model inference using Hugging Face Transformers (DialoGPT-medium)
- Web API for integration with calendar and email services
- GPU acceleration on NVIDIA hardware (requires CUDA)

## Requirements

- NVIDIA GPU with CUDA support (optional, runs on CPU)
- Python 3.8+
- CUDA 11.8+ (recommended for GPU)
