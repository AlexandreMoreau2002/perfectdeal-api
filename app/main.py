from fastapi import FastAPI, Response

app = FastAPI(title="PerfectDeal API", version="1.0")

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(content="", media_type="image/x-icon")