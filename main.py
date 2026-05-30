from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

# pip install "fastapi[standard]"


# # Install requirements
# python -m pip install --upgrade pip
# pip install "fastapi[standard]"

# # Run (Execute)
# fastapi dev main.py