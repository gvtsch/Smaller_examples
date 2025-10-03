import re

def main():
    text = "Hello world, I am a developer. My email is test@example.com and my phone number is 12-345-6789."

    # Example 1: re.search() - Find the first occurrence
    match = re.search(r"developer", text)
    if match:
        print(f"Found: '{match.group()}' at position {match.start()} to {match.end()}")
        # match.group() returns the string found
        # match.start() returns the start index of the match 
        # match.end() returns the end index of the match
    else:
        print("Not found.")

    # Example 2: re.findall() - Find all occurrences of a pattern
    numbers = re.findall(r"\d+", text) # \d+ matches one or more digits
    print(f"All numbers: {numbers}")

    # Example 3: re.sub() - Replace patterns
    new_text = re.sub(r"Developer", 'Programmer', text)
    print(f"Text after replacement: {new_text}")

    # Example 4: Find email address (more complex pattern)
    # r"..."is a "raw string" so that backslashes do not have to be double-escaped
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    email_match = re.search(email_pattern, text)
    if email_match:
        print(f"Email found: {email_match.group()}")

    # Example 5: Find phone number (with groups)
    # (\d{2}) - Group 1: 2 digits
    # -? - Optional hyphen
    # (\d{3}) - Group 2: 3 digits
    # -? - Optional hyphen
    # (\d{4}) - Group 3: 4 digits
    phone_pattern = r"(\d{2})-?(\d{3})-?(\d{4})"
    phone_match = re.search(phone_pattern, text)
    if phone_match:
        print(f"Phone number found: {phone_match.group()}")
        print(f"Area code: {phone_match.group(1)}")
        print(f"Middle part: {phone_match.group(2)}")
        print(f"End part: {phone_match.group(3)}")
    
if __name__ == "__main__":
    main()