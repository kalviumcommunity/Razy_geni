import json
from transformers import pipeline

def judge_prompt(input_text, model_output, expected_output):
    """
    Judge prompt to compare model output with expected results.
    """
    return f"Input: {input_text}\nModel Output: {model_output}\nExpected Output: {expected_output}\nDoes the model output match the expected output?"

def evaluate_pipeline(dataset_path):
    """
    Evaluates the model using the dataset and judge prompt.
    """
    # Load dataset
    with open(dataset_path, "r") as file:
        dataset = json.load(file)

    # Load a pre-trained model pipeline (e.g., text generation)
    model = pipeline("text2text-generation", model="t5-small")

    # Evaluate each sample
    for sample in dataset:
        input_text = sample["input"]
        expected_output = sample["expected_output"]

        # Generate model output
        model_output = model(input_text)[0]["generated_text"]

        # Use judge prompt
        evaluation = judge_prompt(input_text, model_output, expected_output)
        print(evaluation)

if __name__ == "__main__":
    dataset_path = "car-agent/data/evaluation_dataset.json"
    evaluate_pipeline(dataset_path)
