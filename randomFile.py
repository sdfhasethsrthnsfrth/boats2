import os

def get_random_bytes(num_bytes):
    with open('/dev/random', 'rb') as f:
        random_bytes = f.read(num_bytes)
    return random_bytes

# Example usage
random_data = get_random_bytes(4)  # Get 4 random bytes
print("Random bytes:", random_data)