import numpy as np
import open3d as o3d
import os

_TEST_3D_FILE = '\data\Chair.ply'


def uniform_sampling(pcd, n_samples=1024):
    points = np.asanyarray(pcd.points)
    if len(points) < n_samples:
        print(f'Point cloud has only {len(points)} points, less than the requested {n_samples}.')
    idx = np.random.choice(len(points), n_samples, replace=False)
    sampled_pcd = pcd.select_by_index(idx)
    return sampled_pcd


def normalize_point_cloud(pcd):
    points = np.asarray(pcd.points)
    centroid = np.mean(points, axis=0)
    points -= centroid 
    furthest_distance = np.max(np.linalg.norm(points, axis=1))
    points /= furthest_distance
    pcd.points = o3d.utility.Vector3dVector(points)
    return pcd


def preprocess_point_cloud(file_path, n_samples=1024, visualize=True):
    # Load 3D Model File (e.g. .ply)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    obj_path = '\\'.join(script_dir.split('\\')[:-1]) + file_path
    # Read the point cloud file
    assert os.path.isfile(obj_path)
    pcd = o3d.io.read_point_cloud(obj_path)
    # Visualize for validation
    if visualize:
        o3d.visualization.draw_geometries([pcd])

    # Standardization 
    # Convert point cloud to np array
    points = np.asarray(pcd.points)
    print('Original shape:', points.shape)

    # Sampling
    # Reduce the number of points (e.g. >100,000) down to 1024, which is the default input size for PointNet++
    sampled_pcd = uniform_sampling(pcd, n_samples=n_samples)
    if visualize:
        o3d.visualization.draw_geometries([sampled_pcd])

    # Normalization
    # Make point clouds to be centered at origin and normalized to unit sphere.
    normalized_pcd = normalize_point_cloud(sampled_pcd)
    if visualize:
        o3d.visualization.draw_geometries([normalized_pcd])


def main():
    preprocess_point_cloud(
        file_path=_TEST_3D_FILE, n_samples=1024, visualize=True
    )


if __name__== '__main__':
    main()





