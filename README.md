# AI KruBoo Chatbot


## Struktur Direktori
  - `bot.py`: Logika chatbot AI (pemrosesan pesan, dll).
  - `config.py`: Pengaturan konfigurasi aplikasi.
- `main.py`: Entry point untuk menjalankan aplikasi.
- `requirements.txt`: Daftar dependensi Python.
- `.env.example`: Contoh file environment variables.

## Cara Menjalankan
1. Buat virtual environment (opsional tapi disarankan):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
2. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy file `.env.example` menjadi `.env` dan isi variabel yang dibutuhkan.
4. Menjalankan Chatbot di Terminal:
   ```bash
   python main.py
   ```

## Menjalankan Sebagai Backend API (Untuk Flutter)
Jika kamu ingin menggunakan proyek ini sebagai REST API yang dipanggil dari aplikasi Flutter/Mobile, kamu bisa menjalankan *server* lokalnya (mirip dengan perintah `php artisan serve` di Laravel) menggunakan perintah:
```bash
uvicorn api:app --host 0.0.0.0 --port 8004 --reload
```
Atau jika menggunakan Python langsung dari virtual environment:
```bash
.\venv\Scripts\uvicorn api:app --host 0.0.0.0 --port 8004 --reload
```

- Server akan berjalan di: `http://localhost:8004`
- Dokumentasi interaktif (Swagger UI) bisa diakses di: `http://localhost:8004/docs`

Kamu bisa menembak API tersebut dari Flutter menggunakan URL `http://<IP-LOCAL-KAMU>:8004/api/chat`.
