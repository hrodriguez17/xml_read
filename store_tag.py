import json
from tag_class import Tag
import xlsxwriter



def save_tag_dict(tag_dict):
    current_tag_dict = read_tag_dict()
    new_tag_dict = list(set(tag_dict.keys())) + current_tag_dict
    current_tag_dict = list(set(new_tag_dict))
    print('Save_Tag_Dict', current_tag_dict)
    with open("tags/tag_storage.json", "w") as f:
        json.dump(current_tag_dict, f)
def save_tag_dict_names(tag_dict):
    current_tag_dict = read_tag_name()
    new_tag_dict = list(set(tag_dict.keys())) + current_tag_dict
    current_tag_dict = list(set(new_tag_dict))
    for item in current_tag_dict:
        item = item + "\n"
    print('Save_Tag_Name', current_tag_dict)
    with open("tags/tag_name_storage.json", "w") as f:
        json.dump(current_tag_dict, f)

    my_list = current_tag_dict
    workbook = xlsxwriter.Workbook('my_list.xlsx')
    worksheet = workbook.add_worksheet()

    for i, item in enumerate(my_list):
        worksheet.write(i, 0, item)

    workbook.close()

def read_tag_dict():
    with open('tags/tag_storage.json', 'r') as f:
        data = json.load(f)
    return data

def read_tag_name():
    with open('tags/tag_name_storage.json', 'r') as f:
        data = json.load(f)
    return data

def dump_tag_instructions(tag_dict):

    for key, value in tag_dict.items():
        value_str = str(value)
        # print("Value", value_str)
        with open(f'tags/{key}.json', "w") as f:
            json.dump(value_str, f)

def read_tag_instructions(tag_dict):
    data = {}
    for key in tag_dict:
        with open(f"tags/{key}.json", "rb") as f:
            data[key] = json.load(f)
    return data

def create_tag_dict(routine):
    instructions = routine.RSLogix5000Content.Controller.Tags.find_all(
        'Tag')
    tag_dict = {}
    for tag in instructions:
        new_tag = Tag(tag)
        tag_dict[new_tag.get_datatype()] = new_tag.get_tree()
    try:
        del tag_dict['None']
    except Exception as e:
        print(f"Possible no none: {e}")
    return tag_dict

def create_tag_dict_name(routine):
    instructions = routine.RSLogix5000Content.Controller.Tags.find_all(
        'Tag')
    tag_dict = {}
    for tag in instructions:
        new_tag = Tag(tag)
        tag_dict[new_tag.get_name()] = new_tag.get_tree()
    try:
        del tag_dict['None']
    except Exception as e:
        print(f"Possible no none: {e}")
    return tag_dict


