# main.py
from fastapi import FastAPI
import os
import platform

app = FastAPI(title="MyService API")

# 获取端口设置（Replit使用5000）
PORT = int(os.getenv("PORT", 5000))

@app.get("/")
def read_root():
    """根路径，返回基础信息"""
    return {
        "message": "Hello from LittlePigGroup!",
        "service": "myservice",
        "status": "running",
        "region": os.getenv("FLY_REGION", "unknown"),  # Fly.io自动注入
        "machine_id": os.getenv("FLY_ALLOC_ID", "unknown")
    }

@app.get("/health")
def health_check():
    """健康检查端点，Fly.io会自动探测此路径"""
    return {"status": "healthy"}

@app.get("/info")
def system_info():
    """查看系统信息"""
    return {
        "python_version": platform.python_version(),
        "hostname": platform.node(),
        "port": PORT
    }

# 注意：Fly.io会通过 $PORT 环境变量启动应用，此处代码仅为本地运行备用。
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
