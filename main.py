# File name: main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os  # New: To read the API key from the environment
import google.generativeai as genai  # New: Google's AI library

# --- Configure the Gemini AI Model ---
# New: Read the API key from your server's environment variables
try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    # New: Initialize the model
    # Using gemini-1.5-flash as it's fast and excellent for chat
    model = genai.GenerativeModel('gemini-1.5-flash')
except KeyError:
    print("FATAL ERROR: GEMINI_API_KEY environment variable not set.")
    model = None
except Exception as e:
    print(f"Error configuring Google AI: {e}")
    model = None

# Create the main application
app = FastAPI()

# --- Add CORS Middleware ---
# This allows your websites to talk to this server
origins = [
   "https://primingparagon.org",
   "https://www.primingparagon.org",
   "http://palegoldenrid-nightinggale-250665.hostingersite.com",
   "https://palegoldenrid-nightinggale-250665.hostingersite.com",
   "http://127.0.0.1:5500",  # Added for local testing
   "http://localhost:5500"  # Added for local testing
]

app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)

# --- Define the data model for our chat ---
class ChatRequest(BaseModel):
   prompt: str

# --- Your Root Endpoint ---
@app.get("/")
def read_root():
   return {"message": "Paragon AI backend is live."}

# --- Your Chat Endpoint (NOW WITH AI!) ---
@app.post("/chat")
def handle_chat(request: ChatRequest):
   user_message = request.prompt

   if model is None:
       return {"reply": "Error: The AI model is not configured. Please check the server logs."}

   try:
       # --- AI Logic Starts Here ---
       # New: Send the user's message to the Gemini model
       response = model.generate_content(user_message)

       # New: Get the AI's text response
       ai_response = response.text
       # --- AI Logic Ends Here ---

   except Exception as e:
       # New: Handle any errors from the AI API
       print(f"Error during AI generation: {e}")
       ai_response = "Sorry, an error occurred while connecting to the AI. Please try again."

   # Send the response back as JSON
   return {"reply": ai_response}
