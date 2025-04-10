import os
import ccxt
from dotenv import load_dotenv

# Загружаем API ключи из .env (рекомендуется)
load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY", "your_api_key_here")
API_SECRET = os.getenv("BINANCE_API_SECRET", "your_api_secret_here")

def connect_to_binance():
    """Создаём объект Binance"""
    return ccxt.binance({
        'apiKey': API_KEY,
        'secret': API_SECRET
    })

def fetch_balances(exchange):
    """Получаем баланс аккаунта"""
    print("🔄 Получаю баланс...")
    balances = exchange.fetch_balance()
    total = balances['total']
    print("✅ Баланс получен!")
    return total

def print_balances(balances):
    """Выводим только монеты с ненулевым балансом"""
    print("\n📊 Текущий баланс:")
    for coin, amount in balances.items():
        if amount > 0:
            print(f"  {coin}: {amount}")

def main():
    print("🚀 Crypto Auditor запущен!")
    
    exchange = connect_to_binance()
    balances = fetch_balances(exchange)
    print_balances(balances)

if __name__ == "__main__":
    main()
