from transformers import AutoTokenizer, AutoModel
import torch

def generate_embeddings(text):
    """
    Generates embeddings for the given text using a pre-trained model.
    """
    # Load pre-trained model and tokenizer
    model_name = "bert-base-uncased"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)

    # Tokenize input text
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    # Generate embeddings
    with torch.no_grad():
        outputs = model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1)  # Mean pooling

    return embeddings.numpy()

if __name__ == "__main__":
    # Example text
    text = "Optimize the trip for fuel efficiency."

    # Generate embeddings
    embeddings = generate_embeddings(text)
    print("Generated Embeddings:")
    print(embeddings)
