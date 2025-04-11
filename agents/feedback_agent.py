class FeedbackAgent:
    def __init__(self, db_agent):
        self.db_agent = db_agent

    def record_feedback(self, customer_id, product_id, feedback_score):
        self.db_agent.insert_feedback(customer_id, product_id, feedback_score)
