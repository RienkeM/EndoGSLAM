import os
import re
import shutil

def rename_files(raw_folder_path, new_folder_path):
    """
    VR-CAPS export has a different name of color and depth picture
    Also it starts counting from 0000 instead of 0001 so that should be changed
    Copy the raw data instead of overwriting
    """

    # Create the destination folder if it doesn't exist
    if os.path.exists(new_folder_path):
        print(f"Clearing existing folder: {new_folder_path}")
        shutil.rmtree(new_folder_path) # delete previous preprocessing attempts
    os.makedirs(new_folder_path)

    files = os.listdir(raw_folder_path)

    pattern = re.compile(r'^color_(\d+)\.png$')
    pattern2 = re.compile(r'^depth_(\d+)\.exr$')

    for filename in files:
        match_color = pattern.match(filename)
        match_depth = pattern2.match(filename)

        if match_color:
            frame_number = int(match_color.group(1)) + 1
            padded_number = str(frame_number).zfill(4)
            new_filename = f"{padded_number}_color.png"
        elif match_depth:
            frame_number = int(match_depth.group(1)) + 1
            padded_number = str(frame_number).zfill(4)
            new_filename = f"{padded_number}_depth.exr"
        else:
            continue

        src = os.path.join(raw_folder_path, filename)
        dst = os.path.join(new_folder_path, new_filename)
        shutil.copy2(src, dst) # copy content and move to new folder with new name
        print(f"Processed: {filename} -> {new_filename}")
        
raw_folder_path = 'VR_CAPS_raw'
new_folder_path = 'VR_CAPS'
rename_files(raw_folder_path, new_folder_path)
