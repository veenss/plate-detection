from PIL import Image
import os

def resize_images(input_folder, output_folder, target_size=(1024, 1280)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            with Image.open(input_path) as img:
                # Calculate the aspect ratio
                aspect_ratio = img.width / img.height

                # Resize the image while maintaining the aspect ratio
                img.thumbnail((target_size[1] * aspect_ratio, target_size[1]))

                # Create a blank background
                background = Image.new("RGB", target_size, (255, 255, 255))

                # Paste the thumbnail on the background
                offset = ((target_size[0] - img.width) // 2, (target_size[1] - img.height) // 2)
                background.paste(img, offset)

                #optional for rotate image
                background = img.rotate(-90, expand=True)

                # Save the resized image
                background.save(output_path)
        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    input_folder = "path/your/folder"
    output_folder = "path/your/folder"

    target_size = (1024, 1280)

    resize_images(input_folder, output_folder, target_size)
