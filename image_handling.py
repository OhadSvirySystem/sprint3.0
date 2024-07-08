from PIL import Image
import io

image_path = r'C:\Users\TLP-001\PycharmProjects\sprint3.0\top_secret\top_image.jpg'
# Compressing
image = Image.open(image_path)
byte_array = io.BytesIO()
image.save(byte_array, format='JPEG')
compressed_data = byte_array.getvalue()
print("Compressed Data:", compressed_data)
print("Compressed Data Size (bytes):", len(compressed_data))

# Decompressing
byte_array = io.BytesIO(compressed_data)
decompressed_image = Image.open(byte_array)
decompressed_image.show()