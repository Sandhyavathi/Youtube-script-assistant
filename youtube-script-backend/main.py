from fastapi import FastAPI, Request
from pydantic import BaseModel
import cohere

app = FastAPI()

# Define the input structure
class ScriptRequest(BaseModel):
    topic: str
    tone: str
    audience: str
    format: str

# Initialize Cohere API
cohere_client = cohere.Client("q4aR7zJvfaFqThEzEaUSQcosgucEB5XdgU9el4xM")

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the YouTube Script Backend API!"}

# Other endpoints
@app.post("/generate-script/")
async def generate_script(request: ScriptRequest):
    prompt = f"""
    Create a YouTube video script. 
    Topic: {request.topic}
    Tone: {request.tone}
    Audience: {request.audience}
    Format: {request.format}
    """
    response = cohere_client.generate(
        model='command-xlarge-nightly',
        prompt=prompt,
        max_tokens=500,
    )
    return {"script": response.generations[0].text}
