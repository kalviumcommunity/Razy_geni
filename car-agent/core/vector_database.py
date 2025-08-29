import faiss
import numpy as np
from embeddings import generate_embeddings

def create_vector_database():
    """
    Creates a vector database and adds sample embeddings.
    """
    # Initialize FAISS index
    dimension = 768  # Example embedding dimension
    index = faiss.IndexFlatL2(dimension)

    # Generate and add sample embeddings
    texts = [
        "Optimize the trip for fuel efficiency.",
        "Generate a maintenance plan.",
        "Analyze fuel consumption trends.",
        "Schedule a trip for Saturday.",
        "Provide safe driving tips."
    ]
    embeddings = np.array([generate_embeddings(text).flatten() for text in texts])
    index.add(embeddings)

    return index, texts

def search_vector_database(index, query_embedding, texts, top_k=3):
    """
    Searches the vector database for the most similar embeddings.
    """
    distances, indices = index.search(query_embedding, top_k)
    results = [(texts[i], distances[0][j]) for j, i in enumerate(indices[0])]
    return results

if __name__ == "__main__":
    # Create vector database
    index, texts = create_vector_database()

    # Generate query embedding
    query = "Plan a trip for maximum fuel efficiency."
    query_embedding = np.array([generate_embeddings(query).flatten()])

    # Search the database
    results = search_vector_database(index, query_embedding, texts)
    print("Search Results:")
    for text, distance in results:
        print(f"Text: {text}, Distance: {distance}")
