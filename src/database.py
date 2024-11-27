from supabase_client import get_supabase_client

class Database:
    def __init__(self):
        self.supabase = get_supabase_client()

    def add_payment(self, payment_data):
        response = self.supabase.table('payments').insert(payment_data).execute()
        return response

    def get_payments(self):
        response = self.supabase.table('payments').select('*').execute()
        return response.data