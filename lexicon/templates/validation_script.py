# Validation Script

import sys
def validate_lexicon(file_path):
    errors = []
    with open(file_path, 'r') as f:
        for line in f:
            if "Etymology" not in line:
                errors.append(f"Missing etymology: { line.strip() }")
        return errors

if __name__ == "__main__":
    file_path = sys.argv[1]
    errors = validate_lexicon(file_path)
    if errors:
        for error in errors:
            print(error)
        sys9"

    print("Validation passed.")
