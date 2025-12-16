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

## Features

- Local AI model inference using Hugging Face Transformers (DialoGPT-medium)
- Web API for integration with calendar and email services
- GPU acceleration on NVIDIA hardware (requires CUDA)

## Requirements

- NVIDIA GPU with CUDA support (optional, runs on CPU)
- Python 3.8+
- CUDA 11.8+ (recommended for GPU)