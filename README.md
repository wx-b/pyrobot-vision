# PyRobot Vision Module

## Model-based Approach: A Sparse Gaussian Approach to Region-Based 6DoF Object Tracking
Manuel Stoiber, Martin Pfanne, Klaus H. Strobl, Rudolph Triebel, and Alin Albu-Schäffer  
Best Paper Award, ACCV 2020: [paper](https://openaccess.thecvf.com/content/ACCV2020/papers/Stoiber_A_Sparse_Gaussian_Approach_to_Region-Based_6DoF_Object_Tracking_ACCV_2020_paper.pdf), [supplementary](https://openaccess.thecvf.com/content/ACCV2020/supplemental/Stoiber_A_Sparse_Gaussian_ACCV_2020_supplemental.zip)

### Installation
```
cd rbgt_pybind
pip install .
cd ../pyrbgt
pip install .
```

### Usage
A minimal example is provided in `examples/multi_obj_tracking_example.py`. In order to use this tracker, two components are needed:

- a yaml file specifying:
  - path to object model
  - start pose of the object
- an image handle that:
  - stores camera intrinsics
  - return an image if called, and return None if the user wants to stop tracking

An example yaml config can be found at `rbot_two_models_tracking.yaml`; an example image handle object can be found at `rbot_dataset_handle.py`. The example is a replica of the experiments described in the original paper.

### Missing Pieces and WIP
- Renderer is not rendering properly with the viewer window at this point. This also affects extracting of mask information, and keypoints through UV map.
