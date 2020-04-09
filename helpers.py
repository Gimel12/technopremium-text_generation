import os
import json

from constants import MODEL_PATH_UNCONDITIONAL, MODEL_PATH_INFERENCE

def unconditional_generation():
    os.system(MODEL_PATH_UNCONDITIONAL)


def inference_generation():
    os.system(MODEL_PATH_INFERENCE)