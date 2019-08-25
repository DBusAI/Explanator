# Explanator

Find optimal augmentations with help of albumentations

Two simple rows:

from explanator import Explanator
Explanator(transforms=[])

and all current transformations in albumentations with params will be printed:

Blur {'blur_limit': 7, 'always_apply': False, 'p': 0.5}

------------------------------------

VerticalFlip {'always_apply': False, 'p': 0.5}

.....

