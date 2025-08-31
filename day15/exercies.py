import pandas as pd
from PIL import Image


print("=== Dataset Analysis ===")


data = {
    "Name": ["Ali", "Sara", "Omar", "Lina", "Hassan"],
    "Math": [88, 92, 79, 85, 95],
    "Science": [90, 85, 76, 89, 91],
    "English": [78, 88, 85, 92, 87]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)
print("\nWith Average Column:\n", df)


top_student = df.loc[df["Average"].idxmax()]
print("\nTop Student:\n", top_student)


print("\n=== Image Processing ===")
try:
    img = Image.open("example.jpg")  
    grayscale = img.convert("L")   
    grayscale.save("grayscale.jpg")
    print("✅ Grayscale image saved as 'grayscale.jpg'")
except FileNotFoundError:
    print("Please place an image named 'example.jpg' in the same folder to run this part.")
