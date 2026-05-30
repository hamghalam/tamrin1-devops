from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Salam API"}


@app.post("/multiply")
def multiply(a: float, b: float):

    result = a * b

    return {
        "a": a,
        "b": b,
        "result": result
    }


@app.post("/division")
def division(a: float, b: float):

    result = a / b

    return {
        "a": a,
        "b": b,
        "result": result
    }
