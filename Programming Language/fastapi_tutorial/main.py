import uvicorn
from fastapi import FastAPI, Cookie

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/header")
def get_headers(x_token: str = Header(None, title="토큰")):
    return {"X-Token": x_token}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)