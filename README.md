# Explanator

Find optimal augmentations with help of albumentations

Two simple rows:

from explanator import Explanator
Explanator(transforms=[])

and ...

Blur {'blur_limit': 7, 'always_apply': False, 'p': 0.5}
--------------------------------------------------
VerticalFlip {'always_apply': False, 'p': 0.5}
--------------------------------------------------
HorizontalFlip {'always_apply': False, 'p': 0.5}
--------------------------------------------------
Flip {'always_apply': False, 'p': 0.5}
--------------------------------------------------
Normalize {'mean': (0.485, 0.456, 0.406), 'std': (0.229, 0.224, 0.225), 'max_pixel_value': 255.0, 'always_apply': False, 'p': 1.0}
--------------------------------------------------
Transpose {'always_apply': False, 'p': 0.5}
--------------------------------------------------
RandomCrop {'always_apply': False, 'p': 1.0}
--------------------------------------------------
RandomGamma {'gamma_limit': (80, 120), 'always_apply': False, 'p': 0.5}
--------------------------------------------------
RandomRotate90 {'always_apply': False, 'p': 0.5}
--------------------------------------------------
Rotate {'limit': 90, 'interpolation': 1, 'border_mode': 4, 'value': None, 'always_apply': False, 'p': 0.5}
--------------------------------------------------
ShiftScaleRotate {'shift_limit': 0.0625, 'scale_limit': 0.1, 'rotate_limit': 45, 'interpolation': 1, 'border_mode': 4, 'value': None, 'always_apply': False, 'p': 0.5}
--------------------------------------------------
CenterCrop {'always_apply': False, 'p': 1.0}
--------------------------------------------------
OpticalDistortion {'distort_limit': 0.05, 'shift_limit': 0.05, 'interpolation': 1, 'border_mode': 4, 'value': None, 'always_apply': False, 'p': 0.5}
--------------------------------------------------
GridDistortion {'num_steps': 5, 'distort_limit': 0.3, 'interpolation': 1, 'border_mode': 4, 'value': None, 'always_apply': False, 'p': 0.5}
--------------------------------------------------
ElasticTransform {'alpha': 1, 'sigma': 50, 'alpha_affine': 50, 'interpolation': 1, 'border_mode': 4, 'value': None, 'always_apply': False, 'approximate': False, 'p': 0.5}
--------------------------------------------------
HueSaturationValue {'hue_shift_limit': 20, 'sat_shift_limit': 30, 'val_shift_limit': 20, 'always_apply': False, 'p': 0.5}
--------------------------------------------------
PadIfNeeded {'min_height': 1024, 'min_width': 1024, 'border_mode': 4, 'value': None, 'always_apply': False, 'p': 1.0}
--------------------------------------------------
RGBShift {'r_shift_limit': 20, 'g_shift_limit': 20, 'b_shift_limit': 20, 'always_apply': False, 'p': 0.5}
--------------------------------------------------
RandomBrightness {'limit': 0.2, 'always_apply': False, 'p': 0.5}
--------------------------------------------------
RandomContrast {'limit': 0.2, 'always_apply': False, 'p': 0.5}
--------------------------------------------------
MotionBlur {'blur_limit': 7, 'always_apply': False, 'p': 0.5}
--------------------------------------------------
MedianBlur {'blur_limit': 7, 'always_apply': False, 'p': 0.5}
--------------------------------------------------
GaussianBlur {'blur_limit': 7, 'always_apply': False, 'p': 0.5}
--------------------------------------------------
GaussNoise {'var_limit': (10.0, 50.0), 'always_apply': False, 'p': 0.5}
--------------------------------------------------
CLAHE {'clip_limit': 4.0, 'tile_grid_size': (8, 8), 'always_apply': False, 'p': 0.5}
--------------------------------------------------
ChannelShuffle {'always_apply': False, 'p': 0.5}
--------------------------------------------------
InvertImg {'always_apply': False, 'p': 0.5}
--------------------------------------------------
ToGray {'always_apply': False, 'p': 0.5}
--------------------------------------------------
JpegCompression {'quality_lower': 99, 'quality_upper': 100, 'always_apply': False, 'p': 0.5}
--------------------------------------------------
Cutout {'num_holes': 8, 'max_h_size': 8, 'max_w_size': 8, 'fill_value': 0, 'always_apply': False, 'p': 0.5}
--------------------------------------------------
CoarseDropout {'max_holes': 8, 'max_height': 8, 'max_width': 8, 'min_holes': None, 'min_height': None, 'min_width': None, 'fill_value': 0, 'always_apply': False, 'p': 0.5}
--------------------------------------------------
ToFloat {'max_value': None, 'always_apply': False, 'p': 1.0}
--------------------------------------------------
FromFloat {'dtype': 'uint16', 'max_value': None, 'always_apply': False, 'p': 1.0}
--------------------------------------------------
Crop {'x_min': 0, 'y_min': 0, 'x_max': 1024, 'y_max': 1024, 'always_apply': False, 'p': 1.0}
--------------------------------------------------
RandomScale {'scale_limit': 0.1, 'interpolation': 1, 'always_apply': False, 'p': 0.5}
--------------------------------------------------
LongestMaxSize {'max_size': 1024, 'interpolation': 1, 'always_apply': False, 'p': 1}
--------------------------------------------------
SmallestMaxSize {'max_size': 1024, 'interpolation': 1, 'always_apply': False, 'p': 1}
--------------------------------------------------
Resize {'interpolation': 1, 'always_apply': False, 'p': 1}
--------------------------------------------------
RandomSizedCrop {'w2h_ratio': 1.0, 'interpolation': 1, 'always_apply': False, 'p': 1.0}
--------------------------------------------------
RandomBrightnessContrast {'brightness_limit': 0.2, 'contrast_limit': 0.2, 'always_apply': False, 'p': 0.5}
--------------------------------------------------
RandomCropNearBBox {'max_part_shift': 0.3, 'always_apply': False, 'p': 1.0}
--------------------------------------------------
RandomSizedBBoxSafeCrop {'erosion_rate': 0.0, 'interpolation': 1, 'always_apply': False, 'p': 1.0}
--------------------------------------------------
RandomSnow {'snow_point_lower': 0.1, 'snow_point_upper': 0.3, 'brightness_coeff': 2.5, 'always_apply': False, 'p': 0.5}
--------------------------------------------------
RandomRain {'slant_lower': -10, 'slant_upper': 10, 'drop_length': 20, 'drop_width': 1, 'drop_color': (200, 200, 200), 'blur_value': 7, 'brightness_coefficient': 0.7, 'rain_type': None, 'always_apply': False, 'p': 0.5}
--------------------------------------------------
RandomFog {'fog_coef_lower': 0.3, 'fog_coef_upper': 1, 'alpha_coef': 0.08, 'always_apply': False, 'p': 0.5}
--------------------------------------------------
RandomSunFlare {'flare_roi': (0, 0, 1, 0.5), 'angle_lower': 0, 'angle_upper': 1, 'num_flare_circles_lower': 6, 'num_flare_circles_upper': 10, 'src_radius': 400, 'src_color': (255, 255, 255), 'always_apply': False, 'p': 0.5}
--------------------------------------------------
RandomShadow {'shadow_roi': (0, 0.5, 1, 1), 'num_shadows_lower': 1, 'num_shadows_upper': 2, 'shadow_dimension': 5, 'always_apply': False, 'p': 0.5}
--------------------------------------------------
Lambda {'image': None, 'mask': None, 'keypoint': None, 'bbox': None, 'name': None, 'always_apply': False, 'p': 1.0}
--------------------------------------------------
ChannelDropout {'channel_drop_range': (1, 1), 'fill_value': 0, 'always_apply': False, 'p': 0.5}
--------------------------------------------------
