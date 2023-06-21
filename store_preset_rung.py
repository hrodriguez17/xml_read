import json
from aoi_class import Aoi

def save_preset_rung_dict(preset_rung_dict, rung_comment, parameters):
    current_preset_rung_dict = read_preset_rung_dict()
    new_preset_rung_dict = list(preset_rung_dict.keys()) + current_preset_rung_dict
    current_preset_rung_dict = list(set(new_preset_rung_dict))
    print('Save_preset_rung_Dict', current_preset_rung_dict)
    dump_preset_rung_instructions(preset_rung_dict, rung_comment, parameters)
    with open("preset_rungs/preset_rung_storage.json", "w") as f:
        json.dump(current_preset_rung_dict, f)

def read_preset_rung_dict():
    with open('preset_rungs/preset_rung_storage.json', 'r') as f:
        try:
            data = json.load(f)
            return data
        except Exception as e:
            print(f"Error creating Preset Rung: {e}")
            return {'':''}


def dump_preset_rung_instructions(preset_rung_dict,rung_comment,parameters):

    for key, value in preset_rung_dict.items():
        value_str = str(value)
        # print("Value", value_str)
        with open(f'preset_rungs/{key.strip()}.json', "w") as f:
            json.dump(value_str, f)
        with open(f'preset_rungs/{key}_comments.json', "w") as f:
            json.dump(rung_comment, f)
        with open(f'preset_rungs/{key}_parameters.json', "w") as f:
            json.dump(parameters, f)

def read_preset_rung_instructions(preset_rung_dict):
    data = {}
    for key in preset_rung_dict:
        with open(f"preset_rungs/{key}.json", "rb") as f:
            data[key] = json.load(f)
    return data

def read_preset_rung_comments(preset_rung_name):
    with open(f"preset_rungs/{preset_rung_name}_comments.json", "rb") as f:
        data = json.load(f)
    return data

def read_preset_rung_parameters(preset_rung_name):
    with open(f"preset_rungs/{preset_rung_name}_parameters.json", "rb") as f:
        data = json.load(f)
    return data

def create_preset_rung_dict(preset_rung):
        pass