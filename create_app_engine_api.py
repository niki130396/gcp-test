from fastapi import FastAPI


app = FastAPI()


@app.get("/people")
def get_people():
    return {"people": []}
