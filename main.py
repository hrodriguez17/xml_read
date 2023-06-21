import re
from aoi_class import Aoi
from bs4 import BeautifulSoup as bs
from store_aoi import *
from store_tag import *
import gui
import lxml
import sys
print(sys.path)
print(sys.executable)

def get_routine(filepath):
    new_l = []
    newfile = f"{filepath[:-4]}_updated.L5X"
    print(newfile)
    with open(filepath) as f:
        for line in f:
            line = line.replace("<![CDATA[", "<CData>\n<![CDATA[")
            line = line.replace("]>", "]>\n</CData>")
            # print(line)
            new_l.append(line)

    with open("first1.L5X", "w") as output_file:
        for r in new_l:
            output_file.write(r)
            # output_file.write("\n")

    with open("first1.L5X", "r", encoding="utf-8") as file:
        content = file.read()

    return bs(content, 'lxml-xml')


def write_routine(routine, filepath):
    update_filepath = str(filepath[:-4])
    with open('first.L5X', 'w', encoding="utf-8") as f:
        f.write(str(routine))

    _extracted_from_write_routine_(">\n", ">", ">", ">\n")
    _extracted_from_write_routine_("<CData>\n", "<![CDATA[", "</CData>", "]]>")
    buffer = ""
    new_n = []
    with open("first.L5X") as f:
        for line in f:
            if "<![CDATA[" not in line and "]]>" in line:
                buffer = new_n.pop().strip()
                # print(buffer)
                new_n.append(buffer.strip())
            new_n.append(line)
    #
    # print(new_m)
    with open(f"{update_filepath}_updated.L5X", "w") as output_file:
        for r in new_n:
            output_file.write(r)


# TODO Rename this here and in `write_routine`
def _extracted_from_write_routine_(arg0, arg1, arg2, arg3):
    new_l = []
    with open("first.L5X") as f:
        for line in f:
            line = line.replace(arg0, arg1)
            line = line.replace(arg2, arg3)
            # # print(line)
            new_l.append(line)

    with open("first.L5X", "w") as output_file:
        for r in new_l:
            output_file.write(r)
            # output_file.write("\n")

def add_rung(routine, neutral_text):
    rung_number = find_end_rung(routine)
    rung_tag = routine.new_tag("Rung", Number=rung_number, Type="N")
    text_tag = routine.new_tag("Text")
    cdata_tag = routine.new_tag("CData")
    cdata_tag.append(neutral_text)
    text_tag.append(cdata_tag)
    rung_tag.append(text_tag)

    routine.RSLogix5000Content.Controller.Programs.Program.Routines.Routine.RLLContent.append(rung_tag)

    listy = list(
        routine.RSLogix5000Content.Controller.Programs.Program.Routines.find_all(
            'Rung'
        )
    )


def find_end_rung(routine):
    tags = routine.RSLogix5000Content.Controller.Programs.Program.Routines.Routine.RLLContent.find_all('Rung')
    # print(tags)
    sorted_tags = sorted(tags, key=lambda rung: int(rung['Number']))
    max_number = max(tags, key=lambda rung: int(rung['Number']))
    return int(max_number['Number']) + 1
    # print(sorted_tags)
    # print(max_number)

def create_tag(routine, rung_number, rung_info):
    rung_tag = routine.new_tag("Rung", Number=rung_number, Type="N")
    text_tag = routine.new_tag("Text")
    cdata_tag = routine.new_tag("CData")
    cdata_tag.append(str(rung_info[1]))
    comment_tag = routine.new_tag("Comment")
    comment_cdata_tag = routine.new_tag("CData")
    comment_cdata_tag.append(rung_info[2])
    comment_tag.append(comment_cdata_tag)
    text_tag.append(cdata_tag)
    rung_tag.append(comment_tag)
    rung_tag.append(text_tag)

    routine.RSLogix5000Content.Controller.Programs.Program.Routines.Routine.RLLContent.append(rung_tag)

def insert_rung(routine, rung_info):
    patterns = re.compile(rung_info[3])
    tag = routine.RSLogix5000Content.Controller.Programs.Program.Routines.Routine.RLLContent.find_all('CData', string=patterns)

    for taggy in tag:
        start_num = taggy.parent.parent['Number']
        increment_rungs(routine, start_num)
        create_tag(routine, int(start_num) + 1, rung_info)
        # print(tag[0].parent.parent)
    sort_rung(routine)

def sort_rung(routine):
    tags = routine.RSLogix5000Content.Controller.Programs.Program.Routines.Routine.RLLContent.find_all('Rung')
    sorted_tags = sorted(tags, key=lambda rung: int(rung['Number']))
    # for tag in routine.RSLogix5000Content.Controller.Programs.Program.Routines.Routine.RLLContent.find_all('Rung'):
        # tag.decompose()
    for sorted_tag in sorted_tags:
        routine.RSLogix5000Content.Controller.Programs.Program.Routines.Routine.RLLContent.append(sorted_tag)


def increment_rungs(routine, starting_point):
    tags = routine.RSLogix5000Content.Controller.Programs.Program.Routines.Routine.RLLContent.find_all('Rung')
    new_rungs = [tag for tag in tags if int(tag['Number'])>int(starting_point)]
    for rung in new_rungs:
        rung['Number'] = int(rung['Number']) + 1

    # print(new_rungs)
def dump_files(active_routine):
    aoi_dict = create_aoi_dict(active_routine)
    save_aoi_dict(aoi_dict)
    dump_aoi_instructions(aoi_dict)
    tag_dict = create_tag_dict(active_routine)
    save_tag_dict(tag_dict)
    dump_tag_instructions(tag_dict)
    tag_names = create_tag_dict_name(active_routine)
    save_tag_dict_names(tag_names)



# active_routine = get_routine('PID_0075_Valves_Routine_RLL.L5X')
# print(active_routine.prettify())
# print(active_routine.prettify())
# nt = "[EQU(R_0200,0) EQU(M_0200,0) NEQ(Y_0200,0) OTE(Notify_0200.1) ,EQU(M_0200,0) NEQ(R_0200,0)OTE(Notify_0200.2) ,NEQ(M_0200,0) OTE(Notify_0200.3) ];"
# add_rung(active_routine, nt)
# print(active_routine.RSLogix5000Content.Controller.Programs.Program.Routines.Routine.RLLContent)
# pattern = re.compile('P_AIn')
# tagss = active_routine.RSLogix5000Content.Controller.Programs.Program.Routines.Routine.RLLContent.find_all('CData', string=pattern)
# print(tagss)
# aoi = active_routine.RSLogix5000Content.Controller.AddOnInstructionDefinitions.find('AddOnInstructionDefinition', Name='AOI_ALARM_INDICATE')
# aoi2 = aoi.Parameters.findall('Parameter')
# pattern2 = re.compile('Out')
# aoi2 = aoi.Parameters.find_all('Parameter',Usage=pattern2, Visible='true')
# output = [parameter['Name'] for parameter in aoi2]



# data = read_aoi_dict()
# print("data", data)

# lt = read_aoi_dict()
# ty = read_aoi_instructions(lt)
# print(ty['AOI_ALARM_INDICATE'])
# aoi_new = Aoi(aoi)
# print("Name!", aoi_new.get_name())


# data = read_tag_dict()
# print("data", data)


# insert_rung(active_routine)

# write_routine(active_routine)














# max_number = max(tags, key=lambda rung: int(rung['Number']))
# max_number['Number'] = int(max_number['Number']) + 1
# print(sorted_tags)
# print(max_number)


# print((listy[14].Text))

        # output_file.write("\n")

# parser = etree.XMLParser(strip_cdata=False)

# rungs = soup.findAll('Rung', Number='13')
# print(rungs)
# print(soup.RSLogix5000Content.Controller.Programs.Program.Routines.find_all('Rung'))
# print(soup.contents)
# print(soup.prettify())
# print(soup.RSLogix5000Content.Controller.Programs.Program.Routines.Routine.RLLContent)

# print(list[14])


# from xml.dom.minidom import parse, parseString
# import xml.etree.ElementTree as ET
#
# # dom1 = parse('PID_0200_Routine_RLL.L5X')
# #
# # expertise_elements = dom1.getElementsByTagName("Rung")
# #
# # for element in expertise_elements:
# #     print("thing", element.firstChild.nodeValue)
#
# tree = ET.parse('PID_0200_Routine_RLL.L5X')
# root = tree.getroot()
# print(root)
# for lvl_one in root:
#     print(lvl_one.tag, lvl_one.attrib)
#     for lvl_two in lvl_one:
#         print(lvl_two.tag, lvl_two.attrib)
#         for lvl_three in lvl_two:
#             print(lvl_three.tag, lvl_three.attrib)
#             for lvl_four in lvl_three:
#                 print(lvl_four.tag, lvl_four.attrib)
#                 for lvl_five in lvl_four:
#                     print(lvl_five.tag, lvl_five.attrib)
#                     for lvl_six in lvl_five:
#                         print(lvl_six.tag, lvl_six.attrib)
#                         for lvl_seven in lvl_six:
#                             print(lvl_seven.tag, lvl_seven.attrib)
#                             for lvl_eight in lvl_seven:
#                                 print(lvl_eight.tag, lvl_eight.attrib, lvl_eight.text, lvl_eight.text)
#
# print('new spot')
# lowers = list(root.iter())
# # print("lower", lowers)
# elements = tree.findall("Number")
# print(elements)
# for tag in elements:
#     print("this is the test")
#     print(tag.text)
# parser = etree.XMLParser(strip_cdata=False)
# with open("PID_0200_Routine_RLL.L5X", "rb") as source:
#     tree = etree.parse(source, parser=parser)