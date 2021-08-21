# Problem statement
A graphic designer sends you icons for a website, but the delivered final designs are in the wrong format, rotated 90 degress, and you cannot contact the designer to fix these. There are thousands of pictures and you have a deadline coming up.

# Goal
* Fix the images and place them to /opt/icons folder

# Images
* Downloading zip images
** curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=$11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" > /dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" -o images.zip && sudo rm -rf cookie
* Unzip files
** Unzip images.zip

# What I learn from this
* How to use PIL library to manipulate images

# Output 
 ![image](https://user-images.githubusercontent.com/14297774/130312685-0d6f3d58-2c71-48eb-874e-6c19359f4087.png)
