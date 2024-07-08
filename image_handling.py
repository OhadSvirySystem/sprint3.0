from PIL import Image
import io

# Compressing
image = Image.open('black_white_image.png')
byte_array = io.BytesIO()
image.save(byte_array, format='PNG')
compressed_data = byte_array.getvalue()
print("Compressed Data:", compressed_data)

# Decompressing
byte_array = io.BytesIO(compressed_data)
decompressed_image = Image.open(byte_array)
decompressed_image.show()