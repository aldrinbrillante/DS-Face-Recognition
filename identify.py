###################################################################################################
#                                 Identify Faces Goal:
# identify faces and draw a bx around them with their names. If known face, labeled 'unknown'
###################################################################################################


###################################################################################################
#      Faces Used for Program (Will Change Names on Finalized Commit for privacy purposes):
# Aldrin Brillante
# Megan
# Sid
# Yin
# Liz
# Jay
# Chris
# Hani
###################################################################################################

import face_recognition
from PIL import Image, ImageDraw #needed to draw on top of an image

#Aldrin
image_of_aldrin = face_recognition.load_image_file('./img/known/Aldrin Brillante.png')
aldrin_face_encoding = face_recognition.face_encodings(image_of_aldrin)[0]

#Megan
image_of_megan = face_recognition.load_image_file('./img/known/megan.png')
megan_face_encoding = face_recognition.face_encodings(image_of_megan)[0]

#Sid
image_of_sid = face_recognition.load_image_file('./img/known/sid.png')
sid_face_encoding = face_recognition.face_encodings(image_of_sid)[0]

#Yin
image_of_yin = face_recognition.load_image_file('./img/known/yin.png')
yin_face_encoding = face_recognition.face_encodings(image_of_yin)[0]

#Liz
image_of_liz = face_recognition.load_image_file('./img/known/liz.png')
liz_face_encoding = face_recognition.face_encodings(image_of_liz)[0]

#Jay
image_of_jay = face_recognition.load_image_file('./img/known/jay.png')
jay_face_encoding = face_recognition.face_encodings(image_of_jay)[0]

#Chris
image_of_chris = face_recognition.load_image_file('./img/known/chris.png')
chris_face_encoding = face_recognition.face_encodings(image_of_chris)[0]

#Hani
image_of_hani = face_recognition.load_image_file('./img/known/hani.png')
hani_face_encoding = face_recognition.face_encodings(image_of_hani)[0]

#  Create arrays of encodings and names
known_face_encodings = [
  aldrin_face_encoding,
  megan_face_encoding,
  sid_face_encoding,
  yin_face_encoding,
  liz_face_encoding,
  jay_face_encoding,
  chris_face_encoding,
  hani_face_encoding
]

known_face_names = [
  "Aldrin Brillante",
  "Megan",
  "Sid",
  "Yin",
  "Liz",
  "Jay",
  "Chris",
  "Hani"
]

# Load test image to find faces in
test_image = face_recognition.load_image_file('./img/groups/group1.png')
# test_image = face_recognition.load_image_file('./img/groups/random-group.png')

####BEWARE OF THIS RUN SEMI RIGHT####
# test_image = face_recognition.load_image_file('./img/groups/su-funny.png')


# Find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Convert to PIL format
pil_image = Image.fromarray(test_image)

# Create a ImageDraw instance
draw = ImageDraw.Draw(pil_image)


# Loop through faces in test image
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
  matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

  name = "Unknown Person"

  # If match
  if True in matches:
    first_match_index = matches.index(True)
    name = known_face_names[first_match_index]
  
  # Draw box
  draw.rectangle(((left, top), (right, bottom)), outline=(255,255,0))

  # Draw label
  text_width, text_height = draw.textsize(name)
  draw.rectangle(((left,bottom - text_height - 10), (right, bottom)), fill=(255,255,0), outline=(255,255,0))
  draw.text((left + 6, bottom - text_height - 5), name, fill=(0,0,0))

del draw

# Display image
pil_image.show()

# Save image
pil_image.save('identify.jpg')

