from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

# pip install "fastapi[standard]"
# fastapi dev main.py
