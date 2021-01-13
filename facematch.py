#####################################################################
#                      Face Match Goal:
# comparing images to see if a specific person is in that image
#####################################################################

import face_recognition

image_of_aldrin = face_recognition.load_image_file('./img/known/Aldrin Brillante.png')
#face encoding method used for image
aldrin_face_encoding = face_recognition.face_encodings(image_of_aldrin)[0]
# unknown_image = face_recognition.load_image_file('./img/unknown/aldrin-1.png')
unknown_image = face_recognition.load_image_file('./img/unknown/chris-1.png')
# unknown_image = face_recognition.load_image_file('./img/unknown/aldrin-side-1.png')

unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]


# Compare faces
results = face_recognition.compare_faces([aldrin_face_encoding], unknown_face_encoding)

if results[0]:
    print('This is Aldrin Brillante')
else:
    print('This is NOT Aldrin Brillante')

