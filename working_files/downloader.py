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

        file_path = self.get_file_path(base, tit, sea)

        d = self.loadfile(data_path + td[tit])

        for i in range(len(ep_l)):
            key_l.append('S' + sea + 'E' + ep_l[i])

        print(key_l)

        for k in key_l:
            link_l.append(d.get(k)['Link'])
        print('Downloading ' + str(len(link_l)) + ' files...')
        self.download_links(file_path, link_l)

    def loadfile(self, in_path):
        with open(in_path) as json_file:
            return json.load(json_file)

    def download_links(self, file_path, link_l):
        for l in link_l:
            print(' - Downloading into',file_pathh)
            os.system('megadl --path=' + file_path.replace(' ', '\ ') +
                      '/Downloads' + '/ ' + l)

    def get_file_path(self, *args):
        base = args[0] + '/Movies/' + args[1]

        if len(args) == 2: return (base)

        sea = args[2]
        return (base + '/Season ' + str(int(sea)))
