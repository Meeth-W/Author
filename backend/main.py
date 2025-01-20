from fastapi import FastAPI, Depends, HTTPException, Header
from pydantic import BaseModel
from functions.auth import login, register, unregister, verify_user

app = FastAPI()

# Models
class RegisterRequest(BaseModel):
    username: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

# Routes
@app.post("/register")
def register_user(request: RegisterRequest):
    return register(request.username, request.password)

@app.post("/login")
def login_user(request: LoginRequest):
    return login(request.username, request.password)

@app.post("/unregister")
def unregister_user(username: str):
    return unregister(username)

@app.post("/get_response")
def get_response(prompt: str, token: str = Header(...)):
    result = verify_user(token)
    if not result['success']:
        raise HTTPException(status_code=401, detail=result['message'])
    return {"message": f"Response for {result['username']}: {prompt}"}

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
