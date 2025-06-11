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

@app.get("/privacy")
def privacy_policy():
    return {
        "privacy": "We respect your privacy. This service does not collect, store, or share any personal user data. All API calls are processed anonymously. For further inquiries, contact us at structure.api@example.com."
    }

from fastapi.responses import FileResponse

@app.get("/.well-known/ai-plugin.json")
def serve_plugin_manifest():
    return FileResponse(".well-known/ai-plugin.json", media_type="application/json")

from fastapi.staticfiles import StaticFiles
import os

if not os.path.exists(".well-known"):
    os.makedirs(".well-known")

app.mount("/.well-known", StaticFiles(directory=".well-known"), name="well-known")
