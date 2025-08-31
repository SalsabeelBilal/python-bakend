import numpy as np
import pandas as pd
from PIL import Image, ImageFilter


print("=== NumPy Example ===")
arr = np.random.randint(1, 100, size=10)
print("Array:", arr)
print("Mean:", arr.mean())
print("Max:", arr.max())
print("Min:", arr.min())
print("Sorted:", np.sort(arr))


print("\n=== Pandas Example ===")
data = {
    "Name": ["Ali", "Sara", "Omar", "Lina", "Hassan"],
    "Age": [23, 29, 31, 22, 28],
    "Score": [85, 92, 78, 88, 95]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

print("\nAverage Age:", df["Age"].mean())
print("Highest Score:", df["Score"].max())

print("\nStudents with Score > 85:\n", df[df["Score"] > 85])

df["Passed"] = df["Score"] >= 80
print("\nWith Passed column:\n", df)


print("\n=== Pillow Example ===")
try:
    img = Image.open("example.jpg")  
    img.show()

    resized = img.resize((300, 300))
    resized.save("resized.jpg")

    cropped = img.crop((50, 50, 250, 250))
    cropped.save("cropped.jpg")

    rotated = img.rotate(45)
    rotated.save("rotated.jpg")

    blurred = img.filter(ImageFilter.BLUR)
    blurred.save("blurred.jpg")

    print("Image manipulations saved: resized.jpg, cropped.jpg, rotated.jpg, blurred.jpg")

except FileNotFoundError:
    print("Please place an image named 'example.jpg' in the same folder to run Pillow demo.")
