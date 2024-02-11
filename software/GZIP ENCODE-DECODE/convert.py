import gzip
import binascii

# Readable text to be converted to gzip format
readable_text = 'helloooooooooooooooooooooooooo How are you '

# Step 1: Encode text to UTF-8
utf8_bytes = readable_text.encode('utf-8')

# Step 2: Compress the UTF-8 encoded bytes using gzip
compressed_bytes = gzip.compress(utf8_bytes)

# Step 3: Convert compressed bytes to hexadecimal string
hex_str = binascii.hexlify(compressed_bytes).decode('utf-8')

print("Gzip format of the readable text:")
print(hex_str)
