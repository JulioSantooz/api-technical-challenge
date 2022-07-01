from fastapi import FastAPI, Request

app = FastAPI()

#------------------------------------------
# DOC

@app.get("/")
async def root():
    return {"message": "Hello World"}

#------------------------------------------

#------------------------------------------
# USER FLOW

# User endPoint Create
@app.post("/user")
async def user_create(body: object):
    name = body
    return {"Create User": f"Hello"}

# User endPoint update
@app.put("/user")
async def user_update(request: Request):
    return {"Update User": f"Hello "}

# User endPoint list
@app.get("/user")
async def user_delete(request: Request):
    return {"Delete User": f"Hello "}

#------------------------------------------

#------------------------------------------
# DEFAULT FLOW

# Default
@app.post("/default")
async def default_create(body: object):
    name = body
    return {"Create User": f"Hello"}

# Default endPoint update
@app.put("/default")
async def default_update(request: Request):
    return {"Update User": f"Hello "}

# Default endPoint list
@app.get("/default")
async def default_delete(request: Request):
    return {"Delete User": f"Hello "}

#------------------------------------------

#------------------------------------------
# AUTHOR FLOW

# Author
@app.post("/user/author")
async def author_create(body: object):
    name = body
    return {"Create User": f"Hello"}

# Author endPoint update
@app.put("/user/author")
async def author_update(request: Request):
    return {"Update User": f"Hello "}

#------------------------------------------

#------------------------------------------
# PAPER FLOW

# Paper
@app.post("/user/paper")
async def paper_create(body: object):
    name = body
    return {"Create User": f"Hello"}

# Paper endPoint update
@app.put("/user/paper")
async def paper_update(request: Request):
    return {"Update User": f"Hello "}

#------------------------------------------



