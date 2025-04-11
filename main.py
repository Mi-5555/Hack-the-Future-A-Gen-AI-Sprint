from agents.db_agent import DBAgent
from agents.customer_agent import CustomerAgent
from agents.product_agent import ProductAgent
from agents.recommender_agent import RecommenderAgent
from agents.feedback_agent import FeedbackAgent
from utils.preprocessing import normalize_data

def main():
    db = DBAgent()
    customer_agent = CustomerAgent(customer_id=1, db_agent=db)
    product_agent = ProductAgent(db_agent=db)
    recommender_agent = RecommenderAgent(db_agent=db)
    feedback_agent = FeedbackAgent(db_agent=db)

    customer_profile = customer_agent.get_profile()
    products = product_agent.get_all_products()

    customer_vector = normalize_data([x[2] for x in products])  # dummy example
    product_vectors = [normalize_data([x[2]]) for x in products]

    top_indices = recommender_agent.recommend_products(customer_vector, product_vectors)
    print("Recommended Product IDs:", [products[i][0] for i in top_indices])

    feedback_agent.record_feedback(customer_id=1, product_id=products[top_indices[0]][0], feedback_score=5)

if __name__ == "__main__":
    main()
