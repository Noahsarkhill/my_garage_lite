
# Helper function for number input validation
def get_int(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))

            if min_value is not None and value < min_value:
                print("Value is too low")
                continue
            if max_value is not None and value > max_value:
                print("Value is too high")
                continue

            return value

        except ValueError:
            print("Not a valid entry")


# Helper function for text input validation
def get_valid_text(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("This field cannot be empty")
