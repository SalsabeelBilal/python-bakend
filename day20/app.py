from fastapi import FastAPI

# Create the FastAPI app
app = FastAPI()

# Hands-on: Hello, World! endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Exercise: Personalized greeting endpoint
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}
