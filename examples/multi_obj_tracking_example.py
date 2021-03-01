from hydra.experimental import initialize, compose
from pyrbgt import RBGTTracker
from rbot_dataset_handle import RBOTDatasetHandle
import time

if __name__ == "__main__":
	initialize(".")
	config = compose("rbot_two_models_tracking.yaml")
	tracker = RBGTTracker(config.conf)
	image_handle = RBOTDatasetHandle("/home/fair-pitt/RBGT_PY/RBOT_dataset/", "ape", "d_occlusion")
	tracker.track(image_handle)
	for _ in range(100):
		print(tracker.output())
		time.sleep(0.025)