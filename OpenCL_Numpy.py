import numpy as np
import pyopencl as cl
import pyopencl.array as cl_array
from pyopencl.elementwise import ElementwiseKernel

ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

# for each _rgb_ value in image, if not part of a pixel on the image
# border, sum the squares of the differences between it and the
# corresponding color values of each surrounding pixel, then add
# this to the corresponding output pixel's value

kernel_args = "int width, int len_min_width, float *image, float *contrast"
kernel_code = '''
contrast[i/3] = contrast[i/3] +
 (!(
     (i < width) ||
     (i > len_min_width) ||
     (i % width == 0) ||
     ((i+1) % width == 0) ||
     ((i+2) % width == 0) ||
     ((i+3) % width == 0) ||
     ((i-1) % width == 0) ||
     ((i-2) % width == 0)
   )
 )?
 (
     pown((image[i] - image[i-width]), 2) +
     pown((image[i] - image[i-width-3]), 2) +
     pown((image[i] - image[i-width+3]), 2) +
     pown((image[i] - image[i-3]), 2) +
     pown((image[i] - image[i+3]), 2) +
     pown((image[i] - image[i+width]), 2) +
     pown((image[i] - image[i+width-3]), 2) +
     pown((image[i] - image[i+width+3]), 2)
 ) : 0'''
contrast_kernel = ElementwiseKernel(ctx, kernel_args, kernel_code, "contrast")


import Image
im_flat = np.array(Image.open('Office_Background_A.tif').getdata(), np.float32)
im = im_flat.reshape([240,320])
contrast = np.zeros_like(im_flat, np.float32)
height,width = im.shape

# Sent arrays to gpu
im_gpu = cl_array.to_device(queue, im_flat)
contrast_gpu = cl_array.to_device(queue, contrast)

contrast_kernel(width*2, (im_flat.shape[0]-width-1), im_gpu, contrast_gpu)
contrast = contrast_gpu.get().astype(np.float32)
contrast = np.nan_to_num(contrast)






