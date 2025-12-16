from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "microsoft/DialoGPT-medium"  # Example model, can be changed to a larger one like Llama or GPT
tokenizer = None
model = None

def load_model():
    global tokenizer, model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    if torch.cuda.is_available():
        model = model.to('cuda')
    model.eval()

def generate_response(prompt: str) -> str:
    if tokenizer is None or model is None:
        return "Model not loaded"
    
    inputs = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors='pt')
    if torch.cuda.is_available():
        inputs = inputs.to('cuda')
    
    outputs = model.generate(inputs, max_length=100, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response