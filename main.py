import os
from dotenv import load_dotenv
from app.bot import KruBooBot
from app.config import AppConfig

def main():
    # Load environment variables dari file .env
    load_dotenv()
    
    print(f"Memulai {AppConfig.APP_NAME}...")
    
    # Inisialisasi bot
    bot = KruBooBot()
    
    print("Bot siap! Ketik 'keluar' untuk berhenti.")
    while True:
        user_input = input("\nAnda: ")
        if user_input.lower() in ['keluar', 'exit', 'quit']:
            print("KruBoo: Sampai jumpa!")
            break
            
        print("KruBoo: ", end="", flush=True)
        for chunk in bot.get_response_stream(user_input):
            print(chunk, end="", flush=True)
        print()

if __name__ == "__main__":
    main()
