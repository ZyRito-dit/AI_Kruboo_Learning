from google import genai
from app.config import AppConfig

class KruBooBot:
    def __init__(self):
        # Konfigurasi Gemini API
        api_key = AppConfig.GEMINI_API_KEY
        if not api_key:
            print("Peringatan: GEMINI_API_KEY belum diatur di file .env!")
            self.client = None
        else:
            # SDK baru google-genai menggunakan koneksi HTTP yang lebih stabil
            self.client = genai.Client(api_key=api_key)
        
        from google.genai import types

        # Mulai sesi chat untuk menyimpan konteks/history obrolan
        if self.client:
            self.chat_session = self.client.chats.create(
                model='gemini-3.6-flash',
                config=types.GenerateContentConfig(
                    system_instruction=AppConfig.SYSTEM_PROMPT
                )
            )
        else:
            self.chat_session = None

    def send_message(self, user_message: str, file_ref=None):
        if not self.chat_session:
             return "Maaf, API Key Gemini belum diatur."
             
        try:
            content = [user_message]
            if file_ref:
                content.append(file_ref)
            response = self.chat_session.send_message(content)
            return response.text
        except Exception as e:
            return f"Terjadi kesalahan saat memanggil API Gemini: {str(e)}"

    def get_response_stream(self, user_message: str, file_ref=None):
        """
        Fungsi untuk memproses pesan user dan mengembalikan balasan secara streaming (chunk-by-chunk).
        """
        if not self.chat_session:
             yield "Maaf, API Key Gemini belum diatur. Silakan isi GEMINI_API_KEY di file .env"
             return
             
        try:
            content = [user_message]
            if file_ref:
                content.append(file_ref)
            response = self.chat_session.send_message_stream(content)
            for chunk in response:
                yield chunk.text
        except Exception as e:
            error_msg = str(e)
            if "503" in error_msg or "UNAVAILABLE" in error_msg:
                yield "\n\n(Aduh, server AI Google sedang penuh/sibuk nih. Coba kirim ulang pertanyaannya ya!)"
            else:
                yield f"\n\nTerjadi kesalahan saat memanggil API Gemini: {error_msg}"

