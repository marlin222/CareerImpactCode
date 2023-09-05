import cv2
import numpy as np

def denoise_image(image_path, kernel_size=3):
    # Load the image
    noisy_image = cv2.imread(image_path)

    # Apply the averaging filter to denoise the image
    denoised_image = cv2.blur(noisy_image, (kernel_size, kernel_size))

    return denoised_image

def main():
    input_image_path = 'data/noisy_image.jpg'
    output_image_path = 'results/denoised_image.jpg'

    denoised_image = denoise_image(input_image_path)

    cv2.imwrite(output_image_path, denoised_image)
    print("Denoised image saved:", output_image_path)

if __name__ == '__main__':
    main()
