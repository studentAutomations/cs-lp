import os

photo_path = 'https://github.com/studentAutomations/cs-lp/blob/main/cs-lp-nova-obavestenja.png'  


if os.path.exists(photo_path):
    os.remove(photo_path)  
