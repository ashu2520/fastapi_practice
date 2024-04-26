# from typing import Annotated
from fastapi import FastAPI, Query, Depends

app = FastAPI()

@app.get("/first")
def index():
    return "Hello World"

# Path Parameter: (/items/54)
@app.get("/items_1/{item_id}")
def index(item_id:int):
    return {"product_id":item_id}


# Query Parameter: (/items/?q=10)
@app.get("/items_2/")
def index(q:int=0):
    return {"product_id":q}


# Optional parameter
@app.get("/items_3/")
def read_item(item_id:int, q:str | None = None):
    if q:
        return {"item_id": item_id, "q":q}
    return {"item_id": item_id, "q":q}


# Parameter main agar koi pathe pass karna ho to...
@app.get("/items_4/{file_path:path}")
def index(file_path:str):
    return {"File_path": file_path}

# Request Body
# POST or PUT method ko hum browser pr test nhi kar sakte hai...
# Isko test karne ke liye hum "POSTMAN" client hai ya fir hum extension download kar sakte hai "request bin"
@app.post("/items_5")
def index():
    return "Hello World 12345"


# How we can use request body...
from pydantic import BaseModel
class Users(BaseModel):
    # Yaha pr humne User type ka datatype bana diya... 
    # Basically hum ye define kiye hai ki request body main kya jayega...
    id:int
    name:str
    password:str
    address: str | None = None
    
@app.post("/items_6")
def index(user:Users):
    # 'user' --> 'Users' type ka hoga...
    # {"id": 12, "name":"Ashu", "password":"Ashu@123", "address":"Mohali", "mi":"jhgav"} --> Ye 'request body' jo hum bhej rahe hai...
    # Ab kyunki "mi" humne 'User' main define nhi kiya hai to agar hum isko bhjete bhi hai, tab bhi DB isko catch nhi karega
    return user

# Request Body ke sath hum Path Parameter kaise bhejte hai...
@app.post("/items_7/{user_id}")
def index(user_id:int, user:Users):
    print('User_id', user_id)
    return user

#Query Parameter Validations
# Validations lagane ke liye hum 'fastapi' se 'Query' ko import karenge...
# Query function is used to access query parameter...
# There are some cases where Query
# from fastapi import Query 
@app.get("/items_8/")
def index(q:str=Query(None, max_length=5, min_length=2, regex="^jhj")):
    # Sting ka should start with 'jhj'
    return {"q": q}

# Agar Validation main sirf list ya list of string pass karwna hai to humein 'typing' ko import karna hoga
from typing import List
# class args(BaseModel):

class args(BaseModel):
    q:List[str]

@app.post("/items_9/")
def index(data:args):
    print(type(data))
    return{"data": data};

