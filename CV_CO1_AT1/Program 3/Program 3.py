import cv2

# Give the full image path here
image_path = r"C:\Users\lenin\OneDrive\Pictures\Screenshots\pixelated.png"

# Read the image
image = cv2.imread(image_path)

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    input("Press Enter to exit...")
    exit()

# Resize to a very small size
small = cv2.resize(image, (50, 50), interpolation=cv2.INTER_LINEAR)

# Enlarge it back to original size using nearest-neighbor interpolation
pixelated = cv2.resize(
    small,
    (image.shape[1], image.shape[0]),
    interpolation=cv2.INTER_NEAREST
)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Pixelated Image", pixelated)

cv2.waitKey(0)
cv2.destroyAllWindows()

input("Press Enter to exit...")