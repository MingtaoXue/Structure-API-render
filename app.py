from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# 根路径：用于验证服务是否正常运行
@app.get("/")
def root():
    return {"message": "API is working"}

# 请求模型
class StructureRequest(BaseModel):
    user_input: str

# 核心接口：/predict
@app.post("/predict")
async def predict(request: StructureRequest):
    input_text = request.user_input.strip()

    # 简单的模拟逻辑
    if "薛明涛" in input_text:
        result = f"已识别关键词：{input_text}。这是结构动力系统模型的反馈接口。"
    else:
        result = f"未识别到关键字，但已收到输入：{input_text}。"

    return result

# 如果你在本地运行测试
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
