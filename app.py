from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def welcome():
    return "Hello World!, v2"

