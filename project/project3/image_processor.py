import os
from PIL import Image

def process_images(input_dir, output_dir, operation, **kwargs):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            img_path = os.path.join(input_dir, filename)
            img = Image.open(img_path)

            if operation == "resize":
                width, height = kwargs.get("size", (200, 200))
                img = img.resize((width, height))
            elif operation == "grayscale":
                img = img.convert("L")
            elif operation == "rotate":
                angle = kwargs.get("angle", 90)
                img = img.rotate(angle)

            save_path = os.path.join(output_dir, filename)
            img.save(save_path)
            print(f"Processed: {filename}")

def main():
    input_dir = input("Enter input folder path: ")
    output_dir = input("Enter output folder path: ")

    print("\nChoose an operation:")
    print("1. Resize")
    print("2. Grayscale")
    print("3. Rotate")
    choice = input("Enter choice: ")

    if choice == "1":
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        process_images(input_dir, output_dir, "resize", size=(width, height))
    elif choice == "2":
        process_images(input_dir, output_dir, "grayscale")
    elif choice == "3":
        angle = int(input("Enter rotation angle: "))
        process_images(input_dir, output_dir, "rotate", angle=angle)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
