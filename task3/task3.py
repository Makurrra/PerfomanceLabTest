import json
import copy
import sys

file_path1 = sys.argv[1]
file_path2 = sys.argv[2]

def readFiles(file_path1,file_path2):
    with open(file_path1, 'r') as values_file:
        vdata = json.load(values_file)

    with open(file_path2, 'r') as tests_file:
        jdata = json.load(tests_file)
    return vdata,jdata

def addValues(json_input, found_id_values):
    if isinstance(json_input, dict):
        for k, v in list(json_input.items()):
            if k == "id" and v in found_id_values:
                json_input["value"] = found_id_values[v]
            else:
                addValues(v, found_id_values)
    elif isinstance(json_input, list):
        for item in json_input:
            addValues(item, found_id_values)

def main():
    vdata, jdata = readFiles(sys.argv[1],sys.argv[2])
    found_id_values = {}
    for value in vdata["values"]:
        found_id_values[value["id"]] = value["value"]

    jdata_copy = copy.deepcopy(jdata)
    addValues(jdata_copy, found_id_values)

    with open(sys.argv[3], 'w') as report_file:
        json.dump(jdata_copy, report_file, indent=4)

main()