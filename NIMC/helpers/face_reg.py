import cv2
import face_recognition as frc
import pickle
import os


def extract_feature(image_path):
    # image_path = "frontend/src/assets/images/user/Remi.JPG"
    # image = cv2.imread(image_path)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = frc.load_image_file(image_path)
    boxes = frc.face_locations(image, model="hog")
    encodings = frc.face_encodings(image, boxes)
    return encodings


def recognize_face(image_path):
    casc_path_face = (
        os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
    )
    face_cascade = cv2.CascadeClassifier(casc_path_face)
    data = pickle.loads(open("face_enc", "rb").read())
    image = cv2.imread(image_path)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(60, 60),
        flags=cv2.CASCADE_SCALE_IMAGE,
    )
    encodings = frc.face_encodings(rgb)
    names = []
    for encoding in encodings:
        matches = frc.compare_faces(data["encodings"], encoding)
        name = "Unknown"
        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            for i in matchedIdxs:
                # Check the names at respective indexes we stored in matchedIdxs
                name = data["names"][i]
                # increase count for the name we got
                counts[name] = counts.get(name, 0) + 1
                # set name which has highest count
                name = max(counts, key=counts.get)
                # update the list of names
        names.append(name)
        # loop over the recognized faces
        for ((x, y, w, h), name) in zip(faces, names):
            # rescale the face coordinates
            # draw the predicted face name on the image
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(
                image, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2
            )
    print(names)
    cv2.imshow("Frame", image)
    cv2.waitKey(0)


# extract_feature("frontend/src/assets/images/user/Remi.JPG")
