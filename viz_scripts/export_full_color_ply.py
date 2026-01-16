import numpy as np
import torch
import os

# --- SETTINGS ---
# Update this to your specific experiment folder
npz_path = "experiments/C3VD_base/cecum_t1_a_0801/params.npz"
output_path = "full_colored_reconstruction.ply"

def export_full_ply(npz_path, output_path):
    # 1. Load the data from the SLAM result
    if not os.path.exists(npz_path):
        print(f"Error: Could not find {npz_path}")
        return

    params_npz = np.load(npz_path, allow_pickle=True)
    means = params_npz['means3D']      # The global 3D coordinates
    raw_colors = params_npz['rgb_colors'] # The optimized color logits

    # 2. Convert Colors: Logits -> Sigmoid -> RGB [0-255]
    # This is necessary because the SLAM stores colors in logit space
    colors_tensor = torch.from_numpy(raw_colors)
    colors_sig = torch.sigmoid(colors_tensor).numpy()
    colors_uint8 = (np.clip(colors_sig, 0, 1) * 255).astype(np.uint8)

    # 3. Write the PLY file
    print(f"Exporting all {len(means)} Gaussians to {output_path}...")

    with open(output_path, 'wb') as f:
        f.write(b"ply\n")
        f.write(b"format ascii 1.0\n")
        f.write(f"element vertex {len(means)}\n".encode())
        f.write(b"property float x\n")
        f.write(b"property float y\n")
        f.write(b"property float z\n")
        f.write(b"property uchar red\n")
        f.write(b"property uchar green\n")
        f.write(b"property uchar blue\n")
        f.write(b"end_header\n")
        
        for i in range(len(means)):
            line = f"{means[i,0]} {means[i,1]} {means[i,2]} {colors_uint8[i,0]} {colors_uint8[i,1]} {colors_uint8[i,2]}\n"
            f.write(line.encode())

    print("Success! File saved.")

if __name__ == "__main__":
    export_full_ply(npz_path, output_path)