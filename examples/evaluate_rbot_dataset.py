from pyrbgt import Evaluator
from rbot_dataset_handle import RBOTDatasetHandle

if __name__ == "__main__":
    dataset_path = "/home/fair-pitt/RBGT_PY/RBOT_dataset/"
    body_names = ["ape",  "bakingsoda", "benchviseblue", "broccolisoup", "cam",
                  "can",  "cat",        "clown",         "cube",         "driller",
                  "duck", "eggbox",     "glue",          "iron",         "koalacandy",
                  "lamp", "phone",      "squirrel"]
    sequance_names = ["a_regular", "b_dynamiclight", "c_noisy", "d_occlusion"]
    result_folders = ["regular", "dynamic_light", "noisy", "unmodelled_occlusions"]

    for i in range(3, 4):
        e = Evaluator(dataset_path, body_names, sequance_names[i], "/home/fair-pitt/RBGT_PY/output_results/"+result_folders[i], RBOTDatasetHandle)
        e.set_visualize_all_results(True)
        e.Evaluate()
