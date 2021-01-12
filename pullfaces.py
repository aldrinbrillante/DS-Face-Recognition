#####################################################################
#                      Pull Faces Goal:
# pull faces out of image and save them as sperate image and/or show
#####################################################################

#implement pillow library, which is an imaging library
from PIL import Image
import face_recognition

image = face_recognition.load_image_file('./img/groups/group1.png')
face_locations = face_recognition.face_locations(image)

for face_location in face_locations:
    # top right bottom and left position from face location
    top, right, bottom, left = face_location

    #face image variable
    face_image = image[top:bottom, left:right] # face image in the form of an array to get the actual image from pillow library
    pil_image = Image.fromarray(face_image) #using from array method

    #show the images
    # pil_image.show()
    
    #save the images
    pil_image.save(f'{top}.jpg')