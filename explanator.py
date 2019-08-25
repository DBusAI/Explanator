import inspect
from pprint import pprint
from albumentations.augmentations import transforms as tfmsss
from albumentations.augmentations.transforms import *

__all__= ['Explanator']

class Explanator:
    def __init__(self,transforms=[],show_doc='',PrettyPrinter=False):
        if len(transforms)==0:
            for n,i in enumerate(tfmsss.__all__):
                transforms.append(globals()[i])
        for i in transforms:
            if PrettyPrinter==True:
                print(i.__name__,' -\n')
                pprint(self._get_default_args(i))
            else:
                print(i.__name__,self._get_default_args(i))
            if (type(show_doc)==bool)&(show_doc==True):
                print(i.__doc__)
            elif (i.__name__ in show_doc)|(i.__name__==show_doc):
                print(i.__doc__)
            print('-'*50)
    @staticmethod
    def _get_default_args(func):
        signature = inspect.signature(func)
        return {
            k: v.default
            for k, v in signature.parameters.items()
            if v.default is not inspect.Parameter.empty
        }