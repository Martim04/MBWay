import tkinter as tk
from tkinter import messagebox
from database import Database
from payment import Payment

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Pagamento MBWay")
        self.db = Database()

        self.amount_label = tk.Label(root, text="Valor:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        self.phone_label = tk.Label(root, text="Número de Telefone:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()

        self.submit_button = tk.Button(root, text="Pagar", command=self.submit_payment)
        self.submit_button.pack()

    def submit_payment(self):
        amount = float(self.amount_entry.get())
        phone_number = self.phone_entry.get()
        payment = Payment(amount, phone_number)
        payment_response = payment.process_payment()

        # Salvar no banco de dados
        self.db.add_payment(payment_response)

        messagebox.showinfo("Pagamento", f"Pagamento de {amount}€ para {phone_number} realizado com sucesso!")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()