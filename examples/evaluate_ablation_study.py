from evaluator import Evaluator

if __name__ == "__main__":
    dataset_path = "/home/fair-pitt/RBGT_PY/RBOT_dataset/"
    body_names = ["ape",  "bakingsoda", "benchviseblue", "broccolisoup", "cam",
                  "can",  "cat",        "clown",         "cube",         "driller",
                  "duck", "eggbox",     "glue",          "iron",         "koalacandy",
                  "lamp", "phone",      "squirrel"]

    result_folders = ["without_regularization", "with_linear_function", "without_approximation"]

    e0 = Evaluator(dataset_path, body_names, "c_noisy", False, "/home/fair-pitt/RBGT_PY/output_results/"+result_folders[0])
    e0.regional_modality.set_tikhonov_parameter_rotation(0)
    e0.regional_modality.set_tikhonov_parameter_translation(0)
    e0.set_visualize_all_results(False)
    e0.Evaluate()

    e1 = Evaluator(dataset_path, body_names, "c_noisy", False, "/home/fair-pitt/RBGT_PY/output_results/"+result_folders[1])
    e1.regional_modality.set_use_linear_function(True)
    e1.set_visualize_all_results(False)
    e1.Evaluate()

    e2 = Evaluator(dataset_path, body_names, "c_noisy", False, "/home/fair-pitt/RBGT_PY/output_results/"+result_folders[2])
    e2.regional_modality.set_probability_threshold(0)
    e2.regional_modality.set_use_const_variance(True)
    e2.set_visualize_all_results(False)
    e2.Evaluate()