class CustomerAgent:
    def __init__(self, customer_id, db_agent):
        self.customer_id = customer_id
        self.db_agent = db_agent

    def get_profile(self):
        return self.db_agent.fetch_customer_profile(self.customer_id)

    def update_profile(self, new_data):
        self.db_agent.update_customer_profile(self.customer_id, new_data)
