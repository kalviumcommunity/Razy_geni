from transformers import pipeline, AutoTokenizer

def zero_shot_prompt(task_description, input_text, temperature=1.0):
    """
    Demonstrates zero-shot prompting with temperature control.
    """
    # Load a pre-trained text generation model and tokenizer
    model = pipeline("text2text-generation", model="t5-small")
    tokenizer = AutoTokenizer.from_pretrained("t5-small")

    # Create the zero-shot prompt
    prompt = f"Task: {task_description}\nInput: {input_text}\nOutput:"

    # Tokenize the prompt and log the token count
    tokens = tokenizer(prompt, return_tensors="pt")
    token_count = len(tokens["input_ids"][0])
    print(f"Number of tokens used: {token_count}")

    # Generate the model's response with temperature control
    response = model(prompt, temperature=temperature)[0]["generated_text"]
    return response

if __name__ == "__main__":
    # Example task and input
    task_description = "Summarize the following text."
    input_text = "The Car AI Agent optimizes trips, generates maintenance plans, and analyzes fuel consumption."

    # Perform zero-shot prompting with temperature control
    output = zero_shot_prompt(task_description, input_text, temperature=0.7)
    print("Zero-Shot Prompting Output with Temperature:")
    print(output)
