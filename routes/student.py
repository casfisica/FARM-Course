#import staments

from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import studentEntity, listOfStudentEntity
from bson import ObjectId

#create router for student
student_router = APIRouter()

@student_router.get('/HelloWorld')
async def Hello():
    return {'hello world'}


#Get all students
@student_router.get('/students')
async def find_all_students():
    return listOfStudentEntity(connection.local.student.find())

#create a student
@student_router.post('/students')
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntity(connection.local.student.find())

#Updete a student
@student_router.put('/students/{studentId}')
async def update_student(studentId, student:Student):
    #find the student and update it
    connection.local.student.find_one_and_update(
        {"_id": ObjectId(studentId)},
        {"$set": dict(student)}
    )
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))

#Delete a student
@student_router.delete('/students/{studentId}')
async def delete_student(studentId):
    #Find a objet, delete and return it
    return studentEntity(connection.local.student.find_one_and_delete({"_id": ObjectId(studentId)}))

#Get a student by id
@student_router.get('/students/{studentId}')
async def find_student_by_id(studentId):
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))

