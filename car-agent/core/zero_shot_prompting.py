from transformers import pipeline

def zero_shot_prompt(task_description, input_text):
    """
    Demonstrates zero-shot prompting by asking the model to perform a task without examples.
    """
    # Load a pre-trained text generation model
    model = pipeline("text2text-generation", model="t5-small")

    # Create the zero-shot prompt
    prompt = f"Task: {task_description}\nInput: {input_text}\nOutput:"

    # Generate the model's response
    response = model(prompt)[0]["generated_text"]
    return response

if __name__ == "__main__":
    # Example task and input
    task_description = "Summarize the following text."
    input_text = "The Car AI Agent optimizes trips, generates maintenance plans, and analyzes fuel consumption."

    # Perform zero-shot prompting
    output = zero_shot_prompt(task_description, input_text)
    print("Zero-Shot Prompting Output:")
    print(output)
