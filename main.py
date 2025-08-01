
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return{"hello":"world"}
@app.get("/gay")
def read_root():
    return{"gay":"world"} 