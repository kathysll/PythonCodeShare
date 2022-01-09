from PIL import Image  # python image library - Image Proxessing

import glob

#print(glob.glob("*.png"))

import os

directory = r"/Users/kathymulcahy/Files/Study/Python/PythonCode/ConvertImages"

for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        print(os.path.join(directory, filename))
        f = os.path.join(directory,filename)
        im = Image.open(f)
        rgb_im = im.convert('RGB')
        rgb_im.save(f.replace('png', 'jpg'), quality=95)
    else:
        continue

#based on So Answer: http://stackoverflow.com/a/43258974/5086335



#for file in glob.glob("*.png'"):
   

