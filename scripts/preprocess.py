import numpy as np
import open3d as o3d
import os


def uniform_sampling(pcd, n_samples=1024):
    points = np.asanyarray(pcd.points)
    if len(points) < n_samples:
        print(f'Point cloud has only {len(points)} points, less than the requested {n_samples}.')
    idx = np.random.choice(len(points), n_samples, replace=False)
    sampled_pcd = pcd.select_by_index(idx)
    return sampled_pcd


def main():
    # Load 3D Model File (e.g. .ply)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    obj_path = '\\'.join(script_dir.split('\\')[:-1]) +'\data\Chair.ply'
    # Read the point cloud file
    assert os.path.isfile(obj_path)
    pcd = o3d.io.read_point_cloud(obj_path)
    # Visualize for validation
    o3d.visualization.draw_geometries([pcd])

    # Standardization 
    # Convert point cloud to np array
    points = np.asarray(pcd.points)
    print('Original shape:', points.shape)

    # Sampling
    # Reduce the number of points (e.g. >100,000) down to 1024, which is the default input size for PointNet++
    sample_pcd = uniform_sampling(pcd, n_samples=1024)
    o3d.visualization.draw_geometries([sample_pcd])


if __name__== '__main__':
    main()





