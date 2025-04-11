class ProductAgent:
    def __init__(self, db_agent):
        self.db_agent = db_agent

    def get_all_products(self):
        return self.db_agent.fetch_all_products()

    def get_product_details(self, product_id):
        return self.db_agent.fetch_product(product_id)
