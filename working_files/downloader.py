import sys
import json
import os

td = {
    'Twin Peaks': '/TwinPeaks.json',
}


class Downloader:
    def download_files(self, base, data_path, tit, sea, ep_l):
        key_l = []
        link_l = []

        file_path = self.get_file_path(base, tit)
        file_path = file_path.replace(' ', '\ ') + '/Downloads'

        os.system('mkdir -p ' + file_path)
        os.system('pwd')

        d = self.loadfile(data_path + td[tit])

        for i in range(len(ep_l)):
            key_l.append('S' + sea + 'E' + ep_l[i])

        for k in key_l:
            link_l.append(d.get(k)['Link'])
        print('Downloading ' + str(len(link_l)) + ' files...')
        self.download_links(file_path, link_l)

    def loadfile(self, in_path):
        with open(in_path) as json_file:
            return json.load(json_file)

    def download_links(self, fp, ll):
        for i, l in enumerate(ll):
            print(' - Downloading into', fp)
            os.system('megadl --path=' + fp + ' ' + l)

    def get_file_path(self, *args):
        base = args[0] + '/Movies/' + args[1]

        if len(args) == 2: return (base)

        sea = args[2]
        return (base + '/Season ' + str(int(sea)))
