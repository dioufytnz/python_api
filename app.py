# main.py

from fastapi import FastAPI

app = FastAPI()


@app.get("/api/{index}/{user}/{device}/{kpi}")
async def root(index, user, device, kpi):
    return {"message": index + "*" + user + "*" + device + "*" + kpi}
