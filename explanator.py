import inspect
from pprint import pprint
from albumentations.augmentations import transforms as tfmsss
from albumentations.augmentations.transforms import *
from skimage.data import coffee
from ipywidgets import widgets
from matplotlib.pylab import plt

__all__= ['Explanator']

def get_default_args(func):
    signature = inspect.signature(func)
    return {
        k: v.default
        for k, v in signature.parameters.items()
        if v.default is not inspect.Parameter.empty
    }

class Explanator:
    def __init__(self,transforms=[],show_doc='',PrettyPrinter=False):
        if len(transforms)==0:
            for n,i in enumerate(tfmsss.__all__):
                transforms.append(globals()[i])
        for i in transforms:
            if PrettyPrinter==True:
                print(i.__name__,' -\n')
                pprint(get_default_args(i))
            else:
                print(i.__name__,get_default_args(i))
            if (type(show_doc)==bool)&(show_doc==True):
                print(i.__doc__)
            elif (i.__name__ in show_doc)|(i.__name__==show_doc):
                print(i.__doc__)
            print('-'*50)

class AlbuWidget:
    def __init__(self,tfms=Blur,debug=False,image=coffee()):
        self.image=image
        self.debug= debug
        self.tfms=tfms
        self.interact_wds={}
        k=get_default_args(tfms)
        if self.debug:
            print(k)
        ui = self.ui_prepare(k)
        out = widgets.interactive_output(self.f, self.interact_wds)
        display(ui, out)
    def f(self,**kwargs):
        kwargs['always_apply']=True
        print(kwargs)
        aug = self.tfms(**kwargs)
#         Just copy all images, next step will be for continious albus 
        image = aug(image=self.image.copy())['image']
        plt.figure(figsize=(10, 10))
        plt.imshow(image)
        plt.axis('off')
        plt.show()
    def ui_prepare(self,k):    
        for typ in k:
            if typ in ['always_apply','p']:
                continue
            if type(k[typ])==float:
                tmp = widgets.FloatSlider(min=0, max=1, step=0.05, continuous_update=False)
                self.interact_wds[typ]=tmp
            if type(k[typ])==bool:
                tmp = widgets.ToggleButton()
                self.interact_wds[typ]=tmp
            if type(k[typ])==int:
                tmp = widgets.IntSlider(min=1, max=50, step=1, continuous_update=False)
                self.interact_wds[typ]=tmp

        ui_lists=[]
        for w in self.interact_wds:
            ui_tmp= widgets.VBox([widgets.Label(w),self.interact_wds[w]])
            ui_lists.append(ui_tmp)
        ui = widgets.HBox(ui_lists)
        return ui
    def __repr__(self):
        return str(self.interact_wds)