import torch
import torch.nn as nn
import numpy as np
from complexity_metrics import get_gmacs_and_params, get_runtime
from toy_model import ToyHDRModel
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-wp", "--write_path", type=str, default="./", help="Path to write the readme.txt file")
args = parser.parse_args()
write_path=args.write_path

# Load a pytorch model
model = ToyHDRModel()
model.eval()

# Calculate MACs and Parameters
total_macs, total_params = get_gmacs_and_params(model, input_size=(1, 3, 6, 1060, 1900))
mean_runtime = get_runtime(model, input_size=(1, 3, 6, 1060, 1900))

print(total_macs)
print(total_params)
print(mean_runtime)

# Print model statistics to txt file
with open(write_path + 'readme.txt', 'w') as f:
    f.write("runtime per image [s] : " + str(mean_runtime))
    f.write('\n')
    f.write("number of operations [GMAcc] : " + str(total_macs))
    f.write('\n')
    f.write("number of parameters  : " + str(total_params))
    f.write('\n')
    f.write("Other description: Toy Model for demonstrating example code usage.")
# Expected output of the readme.txt for ToyHDRModel should be:
# runtime per image [s] : 0.013018618555068967
# number of operations [GMAcc] : 20.146042
# number of parameters  : 8243
# Other description: Toy Model for demonstrating example code usage.

print("You reached the end of the calculate_ops_example.py demo script. Good luck participating in the NTIRE 2022 HDR Challenge!")

