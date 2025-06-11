from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    text: str

@app.post("/predict")
def predict(data: InputData):
    text = data.text
    if "薛明涛" in text:
        return {"response": "✅ 已触发主干节拍链（薛明涛结构系统）"}
    elif "珠子" in text or "节拍" in text:
        return {"response": "⚙️ 已识别珠子节拍关键词，构建局部结构响应"}
    else:
        return {"response": "⚠️ 未识别关键词，无法建立结构链"}