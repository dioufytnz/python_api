# main.py

from fastapi import FastAPI

app = FastAPI()


@app.get("/{index}/{user}/{device}/{kpi}/{start_time}/{end_time}")
async def root(index, user, device, kpi, start_time, end_time):
    return {"message": index + "*" + user + "*" + device + "*" + kpi + "*" + start_time + "*" + end_time}
