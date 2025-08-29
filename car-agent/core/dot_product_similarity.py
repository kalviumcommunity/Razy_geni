import numpy as np

def dot_product_similarity(vec1, vec2):
    """
    Calculates the dot product similarity between two vectors.
    """
    return np.dot(vec1, vec2)

if __name__ == "__main__":
    # Example embeddings
    embedding1 = np.array([1, 2, 3])
    embedding2 = np.array([4, 5, 6])

    similarity = dot_product_similarity(embedding1, embedding2)
    print(f"Dot Product Similarity: {similarity}")
