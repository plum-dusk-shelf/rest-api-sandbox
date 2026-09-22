from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Web"}

@app.get("/about")
async def about():
    return {"course": "Web Development"}

@app.get("/users")
async def users():
    return {"users": ["Alex", "Maria"]}

@app.get("/info")
async def info():
    return {"Theme": "Sport Club"}

@app.get("/club")
async def club():
    return [{
            "City": "Rostov-on-Don",
            "Players": 12,
            "Score": 811},


            {"City": "Khabarovsk",
            "Players": 13,
            "Score": 1040}
            ]
