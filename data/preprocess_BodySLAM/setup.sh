# recommend checking the max_workers in classifies.py and other parallel processing scripts

# USAGE: 
# terminal root should be: /EndoGSLAM/data/preprocess_c3vd
# folder structure:
# - data/
#   - preprocss_c3vd/
#       - cecum_t1_a/
#           - a lot of unordered files 
#       - setup.sh
#       - the 5 functions below


python repair_first_scene.py # renames the color.png picture numbers to 4-digits by adding 0 (e.g.2 to 0002)
python classifies.py         # rearranges all the files of the zip to folder (e.g., color, depth, flow, etc.)
python undistort.py          # undistort the color and depth images using camera parameters. save originals as color_raw and depth_raw
python video.py              # creates a video from the undistorted images (color or depth), can make both videos
python resize.py             # overwrites the images in color and depth by resizing (does NOT use the created video material)


# cecum_t1_a folder structure after:
# - cecum_t1_a/
#   - color/
#   - color_raw/ 
#   - depth/
#   - depth_raw/ 
#   - flow/
#   - normals/
#   - occlusion/
#   - coverage_mesh.obj
#   - pose.txt