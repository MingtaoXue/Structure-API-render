
from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class InputData(BaseModel):
    text: str

# 加载扩展关键词映射表
try:
    with open("keyword_map.json", "r", encoding="utf-8") as f:
        keyword_map = json.load(f)
except Exception:
    keyword_map = {}

@app.post("/predict")
def predict(data: InputData):
    text = data.text
    if "薛明涛" in text:
        return {"response": "✅ 已触发主干节拍链（薛明涛结构系统）"}
    elif "珠子" in text or "节拍" in text:
        return {"response": "⚙️ 已识别珠子节拍关键词，构建局部结构响应"}
    else:
        for keyword, response in keyword_map.items():
            if keyword in text:
                return {"response": f"📚 映射触发：{response}"}
        return {"response": "⚠️ 未识别关键词，无法建立结构链"}
