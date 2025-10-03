def my_callback(message):
    print(f"Callback received message: {message}")

def process_data(data, callback):
    for item in data:
        # Process the item
        result = item * 2
        # Call the callback function and pass the result
        callback(f"Processed item: {result}")

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    process_data(data, my_callback)