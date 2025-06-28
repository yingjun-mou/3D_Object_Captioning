import open3d as o3d
import os

# Load 3D Model File (e.g. .ply)
script_dir = os.path.dirname(os.path.abspath(__file__))
obj_path = '\\'.join(script_dir.split('\\')[:-1]) +'\data\Chair.ply'
# Read the point cloud file
if os.path.isfile(obj_path):
    pcd = o3d.io.read_point_cloud(obj_path)
    # Visualize for validation
    o3d.visualization.draw_geometries([pcd])
