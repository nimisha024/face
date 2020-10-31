# Import the library
import face_recognition

# Select an image to teach to the machine how to recognize

# * ---------- User 1 ---------- *
# Load the image 
user_one_face = face_recognition.load_image_file("assets/img/user-one.jpg")
# Encode the face parametres
user_one_face_encoding = face_recognition.face_encodings(user_one_face)[0]

# * ---------- User 2 ---------- *
# Load the image 
user_two_face = face_recognition.load_image_file("assets/img/user-two.jpg")
# Encode the face parametres
user_two_face_encoding = face_recognition.face_encodings(user_two_face)[0]


# Create a list of known face encodings and their names
known_face_encodings = [
    user_one_face_encoding,
    user_two_face_encoding
]

# Create list of the name matching with the position of the known_face_encodings
known_face_names = [
    "User One",
    "User Two"
]
