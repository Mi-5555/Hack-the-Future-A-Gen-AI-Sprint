from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class RecommenderAgent:
    def __init__(self, db_agent):
        self.db_agent = db_agent

    def recommend_products(self, customer_vector, product_vectors, top_n=5):
        similarities = cosine_similarity([customer_vector], product_vectors)
        top_indices = np.argsort(similarities[0])[::-1][:top_n]
        return top_indices.tolist()
