import cv2

# Read the image
image = cv2.imread(r"C:\Users\lenin\OneDrive\Pictures\Screenshots\Satellite terrain.png")

# Get image resolution
height, width, channels = image.shape

print("Image Width :", width)
print("Image Height:", height)
print("Channels    :", channels)
print("Resolution  :", width * height, "pixels")

# Display image
cv2.imshow(r"C:\Users\lenin\OneDrive\Pictures\Screenshots\Satellite terrain.png", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


input("Press enter to exit...")