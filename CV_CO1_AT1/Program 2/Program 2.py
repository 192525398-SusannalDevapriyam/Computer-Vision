import cv2

# Give the full path of your image here
image_path = r"C:\Users\lenin\OneDrive\Pictures\Screenshots\kk.jpg"
# Load the Haar Cascade classifier
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Read the image
image = cv2.imread(image_path)

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    input("Press Enter to exit...")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Print number of faces
print("Number of faces detected:", len(faces))

# Show output image
cv2.imshow("Face Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

input("Press Enter to exit...")
input("\nPress Enter to exit...")