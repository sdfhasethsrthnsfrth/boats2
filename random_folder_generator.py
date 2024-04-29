import os

def get_random_bytes(num_bytes):
    with open('/dev/hwrng', 'rb') as f:
        random_bytes = f.read(num_bytes)
    return random_bytes.hex()

def create_directory(mount_point, directory_name):
    try:
        directory_path = os.path.join(mount_point, directory_name)
        os.makedirs(directory_path)
        return True
    except OSError as e:
        print("something went wrong, random directory wasn't created")
        return False
    
#example for testing
#mount_point = "/mnt/mooring"    
#random_folder = get_random_bytes(4)  # Get 4 random bytes
#create_directory(mount_point, random_folder) #make folder on drive