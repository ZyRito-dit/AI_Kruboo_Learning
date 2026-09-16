from fastapi import FastAPI, HTTPException, File, UploadFile, Form
from fastapi.responses import StreamingResponse
from app.bot import KruBooBot
from app.config import AppConfig
import os
import shutil
from dotenv import load_dotenv

# Load env variables
load_dotenv()

app = FastAPI(
    title=AppConfig.APP_NAME,
    description="Backend API untuk KruBoo Chatbot menggunakan Gemini"
)

# Inisialisasi Bot
bot = KruBooBot()

@app.post("/api/chat")
async def chat_endpoint(message: str = Form(...), file: UploadFile = File(None)):
    """
    Endpoint untuk mengirim pesan dan menunggu sampai jawaban penuh selesai (tanpa streaming).
    Mendukung upload gambar dan dokumen.
    """
    if not bot.chat_session:
        raise HTTPException(status_code=500, detail="Gemini API Key belum disetting.")
    
    file_path = None
    file_ref = None
    try:
        if file:
            # Save file temporarily
            file_path = f"temp_{file.filename}"
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            
            # Upload to gemini
            file_ref = bot.client.files.upload(file=file_path)
            
        response_text = bot.send_message(message, file_ref)
        return {"response": response_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if file_path and os.path.exists(file_path):
            os.remove(file_path)

@app.post("/api/chat/stream")
async def chat_stream_endpoint(message: str = Form(...), file: UploadFile = File(None)):
    """
    Endpoint untuk mendapatkan balasan secara streaming.
    (Catatan: saat streaming dengan file, logika file path sementara harus ditangani dengan background task)
    Untuk saat ini, mari jadikan non-stream sebagai default.
    """
    raise HTTPException(status_code=501, detail="Streaming with files not fully implemented yet.")
