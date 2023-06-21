import json
from aoi_class import Aoi
import os

def save_aoi_dict(aoi_dict):
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("Files in %r: %s" % (cwd, files))
    current_aoi_dict = read_aoi_dict()
    new_aoi_dict = list(set(aoi_dict.keys())) + current_aoi_dict
    current_aoi_dict = list(set(new_aoi_dict))
    print('Save_AOI_Dict',current_aoi_dict)
    with open("add_on_definitions/aoi_storage.json'", "w") as f:
        json.dump(current_aoi_dict, f)

def read_aoi_dict():
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("Files in %r: %s" % (cwd, files))
    file_path = 'add_on_definitions/aoi_storage.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    else:
        print("File not found:", file_path)


def dump_aoi_instructions(aoi_dict):
    for key, value in aoi_dict.items():
        value_str = str(value)
        # print("Value", value_str)
        with open(f'add_on_definitions/{key}.json', "w") as f:
            json.dump(value_str, f)

def read_aoi_instructions(aoi_dict):
    data = {}
    for key in aoi_dict:
        with open(f"add_on_definitions/{key}.json", "rb") as f:
            data[key] = json.load(f)
    return data

def create_aoi_dict(routine):
    instructions = routine.RSLogix5000Content.Controller.AddOnInstructionDefinitions.find_all(
        'AddOnInstructionDefinition')
    aoi_dict = {}
    for aoi in instructions:
        new_aoi = Aoi(aoi)
        aoi_dict[new_aoi.get_name()] = new_aoi.get_tree()
    return aoi_dict