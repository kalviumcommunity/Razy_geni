import jsonschema

def validate_json(data, schema):
    """
    Validates JSON data against the provided schema.
    """
    try:
        jsonschema.validate(instance=data, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as e:
        print(f"Validation error: {e.message}")
        return False
