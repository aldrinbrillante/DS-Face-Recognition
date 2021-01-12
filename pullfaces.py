#####################################################################
#                      Pull Faces Goal:
# pull faces out of image and save them as sperate image and/or show
#####################################################################

#implement pillow library, which is an imaging library
from PIL import Image
import face_recognition

image = face_recognition.load_image_file('./img/groups/group1.jpg')
face_locations = face_recognition.face_locations(image)