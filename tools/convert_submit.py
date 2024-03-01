import json
import os

# please specify your path here
folder = '/home/bo.yang5/BEVFormer/test/bevformer_base'
files = os.listdir(folder)

all_dict = {}
for file in files:
    path = os.path.join(folder, file, "pts_bbox", "results_nusc.json")
    with open(path, 'r') as f:
        data = json.load(f)
    all_dict[file] = data
    
with open('/home/bo.yang5/BEVFormer/pred1.json', 'w') as f:
    json.dump(all_dict, f)
    a = 1