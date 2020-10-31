
import numpy as np
import face_recognition

# * ---------- Encode the nameless picture --------- *
# Load picture
face_picture = face_recognition.load_image_file("assets/img/user-one.jpg")
# Detect faces
face_locations = face_recognition.face_locations(face_picture)
# Encore faces
face_encodings = face_recognition.face_encodings(face_picture, face_locations)

# Loop in all detected faces
for face_encoding in face_encodings:
    # See if the face is a match for the known face (that we saved in the precedent step)
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    # name that we will give if the employee is not in the system
    name = "Unknown"
    # check the known face with the smallest distance to the new face
    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    # Take the best one
    best_match_index = np.argmin(face_distances)
    # if we have a match:
    if matches[best_match_index]:
        # Give the detected face the name of the employee that match
        name = known_face_names[best_match_index]

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

