import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Essential for Windows users to read EXR via OpenCV
os.environ["OPENCV_IO_ENABLE_OPENEXR"] = "1"

def load_depth_map(file_path):
    # Load the image with 'UNCHANGED' to keep 32-bit float data
    depth_map = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
    
    # Unity usually stores the depth in the Red channel
    # print(len(depth_map.shape))
    print(f"Red channel mean:   {np.mean(depth_map[:,:,2])}")
    print(f"Green channel mean: {np.mean(depth_map[:,:,1])}")
    print(f"Blue channel mean:  {np.mean(depth_map[:,:,0])}")

    if len(depth_map.shape) == 3:
        depth_map = depth_map[:, :, 2] # Extract the depth channel
        
    return depth_map

# Usage
depth_normalized = load_depth_map("depth_0001.exr")
near = 0.01
far = 2

#####
min_val = np.min(depth_normalized)
max_val = np.max(depth_normalized)
print(f"Minimum depth: {min_val}")
print(f"Maximum depth: {max_val}")

depth_reversed = 1 - depth_normalized
depth_camera_units = near + ( depth_reversed * (far - near)) # it is non-linear so this will not work....
total_scale = 0.1 * 0.0083
depth_meters = depth_camera_units / total_scale


plt.imshow(depth_normalized, cmap='plasma')  # 'magma' or 'viridis' work great for depth
plt.show()

# print(f"Uncorrected distance at center pixel: {depth[540, 675]} meters")
# conv_val = 200 / depth[540, 675]
# pix_left = depth[540, 400] * conv_val
# print(f"Corrected distance at pixel mid left is: {pix_left}")

# heat_map = depth * conv_val
# plt.imshow(heat_map, cmap='plasma')  # 'magma' or 'viridis' work great for depth
