class Payment:
    def __init__(self, amount, phone_number):
        self.amount = amount
        self.phone_number = phone_number

    def process_payment(self):
        # Aqui você pode adicionar lógica para processar o pagamento
        return {
            "amount": self.amount,
            "phone_number": self.phone_number,
            "status": "success"
        }