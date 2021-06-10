from typing import Optional

from fastapi import FastAPI, Request, Response, Depends, Form

from pydantic import BaseModel
import s3_tranferfile
import os


class Tranferfile(BaseModel):
    bucket_name: str
    aws_access_key_id: str
    aws_secret_access_key: str
    endpoint_url: str
    key_file: str
    name_file: str
    use_ssl: bool = False
    # description: Optional[str] = None
    # price: float
    # tax: Optional[float] = None


app = FastAPI()


@app.get("/")
async def index(request: Request):
    return "hello world"


@app.post("/tranferfile")
async def create_s3(tranferfile: Tranferfile):
    s3_tranferfile.multipart_download_boto3(tranferfile.name_file, tranferfile.key_file)
    return tranferfile

# run app:
# uvicorn app:app --host 35.35.35.10 --port 9098 --reload

# if __name__ == "__app__":
#     uvicorn.run(app, host="35.35.35.10", port=9098)
