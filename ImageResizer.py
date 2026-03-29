from PIL import Image

def resize_image(file_path, size):
    try:
        with Image.open(file_path) as img:
            print(f"Original Size: {img.size}")
            img_resized = img.resize(size)
            img_resized.save(f"resized_{file_path}")
            print(f"Resized Size: {img_resized.size}")
    except Exception as e:
        print(f"Error resizing image: {e}")

file_path = input("Enter the image file path: ")
width = int(input("Enter the new width: "))
height = int(input("Enter the new height: "))

resize_image(file_path, (width, height))
