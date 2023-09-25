import os

# Path to the folder containing the images
folder_path = "C:\\Users\\shent\\Downloads\\Python"

# Get the list of image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

# Sort the image files to ensure they are processed in order
image_files.sort()

# Prefix for the new names
prefix = "UTSA"  # Change this to your desired prefix

# Renaming counter
counter = 1

# Renaming loop
for image_file in image_files:
    old_path = os.path.join(folder_path, image_file)
    extension = os.path.splitext(image_file)[1]
    new_name = f"{prefix}_{counter:03d}{extension}"  # e.g., image_001.jpg
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)
    print(f"Renamed {image_file} to {new_name}")
    counter += 1
