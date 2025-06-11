from fastapi import FastAPI
from pydantic import BaseModel
import json

# 定义数据模型
class InputData(BaseModel):
    text: str

# 加载关键词映射
try:
    with open("keyword_map.json", "r", encoding="utf-8") as f:
        keyword_data = json.load(f)
        keyword_map = {
            kw: group["response"]
            for group in keyword_data["triggers"]
            for kw in group["keywords"]
        }
        default_response = keyword_data.get("default_response", "⚠️ 未识别关键词")
except Exception:
    keyword_map = {}
    default_response = "⚠️ 系统异常"

# 将路由注册给主程序
def register_predict_route(app: FastAPI):
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
            return {"response": default_response}
