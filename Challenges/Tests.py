import os
os.chdir('D:/MyWorx/Courses/PAF Bootcamp/Challenges/Images/gear_images')

all_subdirs = [d for d in os.listdir(.) if os.path.isdir(d)]
print(all_subdirs)
for dirs in all_subdirs:
    print(dirs)
