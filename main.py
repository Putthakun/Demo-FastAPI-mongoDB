import uvicorn
from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from bson.objectid import ObjectId



app = FastAPI()

#connect mongodb
client = MongoClient("mongodb+srv://putthakun01:BqSjmSWopTqgj4N0@cluster0.tlf4108.mongodb.net/")
db = client["Patient_information"]
collection = db["Patient_information"]

class Patient_information(BaseModel):
    name: str
    age: int
    gender: str
    number: str
    address : str
    drugallergy : str
    congenitaldisease : str




@app.get("/")
async def read_root():
    return {"message": "Welcome"}

#Create
@app.post(("/Patient_information"))
async def create_Patient_information(patient_information:Patient_information):
    result = collection.insert_one(patient_information.dict())
    return {
        "id" : str(result.inserted_id),
        "name" : patient_information.name,
        "age" : patient_information.age,
        "gender" : patient_information.gender,
        "number" : patient_information.number,
        "address" : patient_information.address,
        "drugallergy" : patient_information.drugallergy,
        "congenitaldisease" : patient_information.congenitaldisease,
        
    }
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

