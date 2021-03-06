import numpy as np

from amap.config.config import get_config_ob


def get_atlas_pixel_sizes(atlas_config_path):
    config_obj = get_config_ob(atlas_config_path)
    atlas_conf = config_obj["atlas"]
    atlas_pixel_sizes = atlas_conf["pixel_size"]
    return atlas_pixel_sizes


def get_transformation_matrix(atlas_config):
    """
    From an atlas config, return transformation_matrix for proper nifti output
    :param atlas_config:
    :return: transformation_matrix
    """
    atlas_pixel_sizes = get_atlas_pixel_sizes(atlas_config)
    transformation_matrix = np.eye(4)
    for i, axis in enumerate(("x", "y", "z")):
        transformation_matrix[i, i] = atlas_pixel_sizes[axis]
    return transformation_matrix
