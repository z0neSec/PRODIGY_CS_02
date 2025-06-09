from PIL import Image

def encrypt_image(input_path, output_path, key=100):
    img = Image.open(input_path)
    img = img.convert("RGB")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    img.save(output_path)
    print("Image encrypted and saved as", output_path)

def decrypt_image(input_path, output_path, key=100):
    img = Image.open(input_path)
    img = img.convert("RGB")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    img.save(output_path)
    print("Image decrypted and saved as", output_path)

print("Image Encryption Tool using Pixel Manipulation")
choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").upper()
in_path = input("Enter the input image path: ")
out_path = input("Enter the output image path: ")
key = int(input("Enter the encryption/decryption key (e.g. 100): "))

if choice == 'E':
    encrypt_image(in_path, out_path, key)
elif choice == 'D':
    decrypt_image(in_path, out_path, key)
else:
    print("Invalid choice.")
