# import gzip
# import binascii

# # Read HTML content from index.html file
# with open('index.html', 'r', encoding='utf-8') as file:
#     html_content = file.read()

# # Step 1: Encode HTML content to UTF-8
# utf8_bytes = html_content.encode('utf-8')

# # Step 2: Compress the UTF-8 encoded bytes using gzip
# compressed_bytes = gzip.compress(utf8_bytes)

# # Step 3: Convert compressed bytes to hexadecimal string
# hex_str = binascii.hexlify(compressed_bytes).decode('utf-8')

# # Step 4: Save compressed data to a new file named index.txt
# with open('index.txt', 'w') as file:
#     file.write(hex_str)

# print("Compressed HTML content saved to index.txt file.")


import gzip
import binascii

# Read HTML content from index.html file
with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Step 1: Encode HTML content to UTF-8
utf8_bytes = html_content.encode('utf-8')

# Step 2: Compress the UTF-8 encoded bytes using gzip
compressed_bytes = gzip.compress(utf8_bytes)

# Step 3: Convert compressed bytes to hexadecimal string with spaces between bytes
hex_str = ' '.join([hex(byte)[2:].zfill(2) for byte in compressed_bytes])

# Step 4: Save compressed data to a new file named index.txt
with open('index.txt', 'w') as file:
    file.write(hex_str)

print("Compressed HTML content saved to index.txt file.")
