from fastapi import FastAPI
import hanja

app = FastAPI()

@app.get("/")
async def root():
    text = "한글 테스트"
    result = hanja.translate(text, 'substitution')

    return {"message": "Hello World!!", "value": result}