# File name: main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create the main application
app = FastAPI()

# --- IMPORTANT: Add CORS Middleware ---
# This tells the server to accept requests from your
# primingparagon.org website. Without this, your 3D app
# will be blocked.
origins = [
    "https://primingparagon.org",
    "https://www.primingparagon.org"
    # You can also add "http://127.0.0.1:5500" for local testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods (GET, POST)
    allow_headers=["*"], # Allows all headers
)

# --- Your First API Endpoint ---
# This creates a "GET" endpoint at the root URL ("/")
@app.get("/")
def read_root():
    # This is the JSON message your API will send back
    return {"message": "Paradox AI backend is live."}

# We will add a "/chat" POST endpoint here later
