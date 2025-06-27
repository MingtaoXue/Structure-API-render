from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# 确保 .well-known 和 openapi.json 可被访问
os.makedirs(".well-known", exist_ok=True)
app.mount("/.well-known", StaticFiles(directory=".well-known"), name="well-known")
app.mount("/", StaticFiles(directory=".", html=True), name="static")

# 根路径用于测试
@app.get("/")
def root():
    return {"message": "API is working"}

# 隐私政策
@app.get("/privacy")
def privacy():
    with open("./.well-known/privacy.md", "r", encoding="utf-8") as f:
        return {"privacy": f.read()}

# 输入数据模型
class InputData(BaseModel):
    user_input: str

# 核心预测接口
@app.post("/predict")
def predict(data: InputData):
    text = data.user_input
    if "薛明涛" in text:
        return {"response": "✅ 已识别关键结构：薛明涛"}
    elif "结构" in text:
        return {"response": "⚠️ 已识别结构关键词，但缺乏特定的判断值"}
    else:
        return {"response": "❌ 未识别到关键结构"}
