# https://qiita.com/ekzemplaro/items/6d95c62446d612c247f3

import motor.motor_asyncio
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
from typing import List
from bson import ObjectId

app = FastAPI()

url = "mongodb://localhost:28000/?readPreference=primary&ssl=false&directConnection=true"
client = motor.motor_asyncio.AsyncIOMotorClient(url)
database = client.college
collection = database.students


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class StudentModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)
    course: str = Field(...)
    gpa: float = Field(..., le=4.0)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "course": "Experiments, Science, and Fashion in Nanophotonics",
                "gpa": "3.0",
            }
        }


@app.get("/", response_model=List[StudentModel])
async def list_students():
    students = await collection.find().to_list(1000)
    return students


@app.get("/{id}")
async def show_student(id: str):
    if (student := await collection.find_one({"_id": id})) is not None:
        return student

    raise HTTPException(status_code=404, detail=f"Student {id} not found")
