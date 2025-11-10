# File name: main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel # Used to define the chat message structure

# Create the main application
app = FastAPI()

# --- IMPORTANT: Add CORS Middleware ---
# This tells the server to accept requests from your
# local testing address.
origins = [
    # "https://primingparagon.org",
    # "palegoldenrod-nightingale-250665.hostingersite.com"
    # --- UPDATED ---
    # We've commented out the "live" addresses and are
    # now only allowing the "temporary" local testing option.
    "http://127.0.0.1:5500" 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods (GET, POST)
    allow_headers=["*"], # Allows all headers
)

# --- Define the data model for our chat ---
# This tells FastAPI what the incoming message should look like
class ChatRequest(BaseModel):
    prompt: str

# --- Your Root Endpoint (No Change) ---
@app.get("/")
def read_root():
    return {"message": "Paragon AI backend is live."}

# --- NEW: Your Chat Endpoint ---
# This creates a "POST" endpoint that listens at /chat
@app.post("/chat")
def handle_chat(request: ChatRequest):
    # 'request.prompt' will contain the message from your 3D app
    user_message = request.prompt
    
    # --- TODO: AI Logic Goes Here ---
    # For now, we'll just send a simple response back
    
    ai_response = f"Backend received your message: '{user_message}'. Paragon AI is not yet connected to an LLM."
    
    # Send the response back as JSON
    return {"reply": ai_response}
