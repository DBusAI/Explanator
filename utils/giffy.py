import os
import numpy as np
from PIL import Image

__all__= ['Giffy']

class Giffy():
    #np_images - list of numpy images arrays for gif preparation
    #file_name - saving file for next steps
    def __init__(self,file_name='temp.gif',np_images=[]):
        self.file = file_name
        self.pil_images=[]
        
        self._rm_file()
        self._prep_images(np_images)
        self._save_gif()
    def _rm_file(self):
        if os.path.isfile(self.file):
            os.remove(self.file)
    def _prep_images(self,np_images):
        for n in np_images:
            frame = Image.fromarray(np.uint8(n))
            self.pil_images.append(frame)
    def _save_gif(self):
        self.pil_images[0].save(self.file,
               save_all=True,
               append_images=self.pil_images[1:],
               duration=100,
               loop=0)
    def _repr_png_(self):
        """ iPython display hook support
        :returns: png version of the image as bytes
        """
        f = open(self.file, "rb")
        return f.read()