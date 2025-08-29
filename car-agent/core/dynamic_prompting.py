def generate_dynamic_prompt(task, context):
    """
    Generates a dynamic prompt based on the task and context.
    """
    prompt = f"You are an expert assistant. Your task is to {task}. Here is the context: {context}."
    return prompt

if __name__ == "__main__":
    # Example task and context
    task = "optimize a trip for fuel efficiency"
    context = "The trip is from Bangalore to Mysore, and the car is a Toyota Fortuner."

    dynamic_prompt = generate_dynamic_prompt(task, context)
    print("Generated Dynamic Prompt:")
    print(dynamic_prompt)
