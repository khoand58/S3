from typing import Optional

from fastapi import FastAPI, Request, Response, Depends, Form

from pydantic import BaseModel
import s3_tranferfile
import os


class Tranferfile(BaseModel):
    bucket_name: str
    key_file: str
    name_file: str
    path_save: str


class Uploadfile(BaseModel):
    bucket_name: str
    key_file: str
    name_file: str
    type_file: str
    path_file_upload: str


app = FastAPI()


@app.get("/")
async def index(request: Request):
    return "hello world"


# "C:\Users\FPT\OneDrive\Desktop\S3\s3"

@app.post("/dowloadfile")
async def create_s3(tranferfile: Tranferfile):
    s3_tranferfile.multipart_download_boto3(bucket_name=tranferfile.bucket_name, name_file=tranferfile.name_file,
                                            key_file=tranferfile.key_file, path_save=tranferfile.path_save)
    return tranferfile


@app.post("/uploadfile")
async def uploadfile( uploadfile: Uploadfile):
    s3_tranferfile.multipart_upload_boto3(bucket_name=uploadfile.bucket_name, key_file=uploadfile.key_file,
                                          name_file=uploadfile.name_file, type_file=uploadfile.type_file,
                                          path_upload=uploadfile.path_file_upload)
    return uploadfile

# run app:
# uvicorn app:app --host 35.35.35.10 --port 9098 --reload

# if __name__ == "__app__":
#     uvicorn.run(app, host="35.35.35.10", port=9098)
