#You Need To Install PIL library if not already
from PIL import Image

#Enter the path of image with extension here 
path = r"C:\\" #C:\\User\Desktop\img.jpg
final_location = r"C:\\" #Enter The Location Where You Want The Final result 
file_name = r"\new.jpg" #Name Of o/p File


img = Image.open(path)

flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM) #Image.FLIP_LEFT_RIGHT


flipped_img.save(final_location+file_name)

print("All Done!")
