import csv
import sys
import json


class CSVTools:
    def main(self):
        d = self.csvtodict('edmdata.csv')
        self.dicttojson(d, edmdata.csv)

    def csvtodict(self, filepath):
        with open(filepath, newline='', encoding='utf-8-sig') as csvdb:
            dbdata = csv.reader(csvdb, delimiter=',')
            headings = dbdata.__next__()
            d = {}
            for row in dbdata:
                d_tmp = {}
                for i, h in enumerate(headings[1:]):
                    i += 1
                    d_tmp[h] = row[i].rstrip()
                d[row[0]] = d_tmp
            return d
        return -1

    def dicttojson(self, d, filepath):
        exportpath = filepath[:len(filepath) - 4] + ".json"
        with open(exportpath, 'w') as outfile:
            json.dump(d, outfile)


if __name__ == '__main__':
    # main('TwinPeaksData.csv')
    ct = CSVTools()
    ct.main()
