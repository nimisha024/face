import cv2

# Select the webcam of the computer (0 by default for laptop)
video_capture = cv2.VideoCapture(0)

# Aplly it until you stop the file's execution
while True:
    # Take every frame
    frame = video_capture.read()
    # Process every frame only one time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        # Initialize an array for the name of the detected users
        face_names = []

        # * ---------- Initialyse JSON to EXPORT --------- *
        json_to_export = {}
        # Loop in every faces detected
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            # check the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            # Take the best one
            best_match_index = np.argmin(face_distances)
            # If we have a match
            if matches[best_match_index]:
                # Save the name of the best match
                name = known_face_names[best_match_index]

                # * ---------- SAVE data to send to the API -------- *
                # Save the name
                json_to_export['name'] = name
                # Save the time
                json_to_export['hour'] = f'{time.localtime().tm_hour}:{time.localtime().tm_min}'
                # Save the date
                json_to_export[
                    'date'] = f'{time.localtime().tm_year}-{time.localtime().tm_mon}-{time.localtime().tm_mday}'
                # If you need to save a screenshot:
                json_to_export['picture_array'] = frame.tolist()

                # * ---------- SEND data to API --------- *
                # Make a POST request to the API
                r = requests.post(url='http://127.0.0.1:5000/receive_data', json=json_to_export)
                # Print to status of the request:
                print("Status: ", r.status_code)

        # Store the name in an array to display it later
        face_names.append(name)
        # To be sure that we process every frame only one time
        process_this_frame = not process_this_frame

        # * --------- Display the results ---------- *
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            # Define the font of the name
            font = cv2.FONT_HERSHEY_DUPLEX
            # Display the name
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()