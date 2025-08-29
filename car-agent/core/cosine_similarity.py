import numpy as np

def cosine_similarity(vec1, vec2):
    """
    Calculates the cosine similarity between two vectors.
    """
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    return dot_product / (norm_vec1 * norm_vec2)

if __name__ == "__main__":
    # Example embeddings
    embedding1 = np.array([1, 2, 3])
    embedding2 = np.array([4, 5, 6])

    similarity = cosine_similarity(embedding1, embedding2)
    print(f"Cosine Similarity: {similarity}")
