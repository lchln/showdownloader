import sys
import json


def main(path1, path2):
    d = csvtodict(path1)
    d2 = csvtodict(path2)
    combinedict(d, d2)
    dicttojson(d, path1)


def csvtodict(filepath):
    with open(filepath, newline='', encoding='utf-8-sig') as json_file:
        dbdict = {}
        data = json.load(json_file)
        for key in data:
            print(len(data[key]))
        return dbdict
    return -1


def dicttojson(d, filepath):
    exportpath = 'combined.json'
    print(exportpath)
    with open(exportpath, 'w') as outfile:
        json.dump(d, outfile)


def combinedict(maj_d, min_d):
    for maj_key in maj_d:
        for min_key in min_d:
            print()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
