import requests

# Substitua pelo seu ID real do Telegram (aquele que o bot vê quando você manda /start)
telegram_user_id = 7797067816  # ← coloque seu ID aqui

# Simulando um pagamento confirmado
payload = {
    "status": "confirmed",
    "amount": 20,
    "telegram_user_id": telegram_user_id
}

# Envia o POST para o Flask que está rodando no bot
response = requests.post("http://localhost:5000/payment_webhook", json=payload)

# Mostra o retorno
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")
