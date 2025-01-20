from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Register Route
class Register(BaseModel):
    username: str
    password: str

@app.post("/register")
def register(register: Register):
    from functions.auth import register as _register
    return _register(register.username, register.password)

# Login Route
class Login(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(login: Login):
    from functions.auth import login as _login
    return _login(login.username, login.password)


# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
