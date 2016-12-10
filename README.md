# Segnet_web_scrapping
This code can be used to download classified images from the Segnet's official website.
Usage:
python Segnet_web_scrapping.py lower_limit upper_limit step input_dir_path output_dir_path
lower_limit = The lower limit of the name of the image.
upper_limit = The upper limit of the name of the image.
step = The number of images to skip with each step.
input_dir_path = The path to the directory where the images to be classified has been saved.
output_dir_path = The path to the directory where the classified images are to be saved.
Example:
python Segnet_web_scrapping.py 410 500 2 /home/user/Road_Segementation/Dataset/Data_Light_480p/ /home/user/Road_Segementation/Dataset/Segnet3/
