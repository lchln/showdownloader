import os
import json
import fnmatch
from working_files import downloader


class Rename:
    def rename_folder(self, data_path, download_path, file_path, tit, sea):
        d = self.loadfile(data_path, tit)

        for input_name in os.listdir(download_path):
            if fnmatch.fnmatch(input_name.upper(), '*S??E??*'):

                dot_loc = input_name.rfind('.')
                file_ext = input_name[dot_loc:len(input_name)]

                e_loc_start = input_name.upper().find('S')
                while input_name[e_loc_start + 3].upper() != 'E':
                    e_loc_start = input_name.upper().find('S', e_loc_start + 1)

                episode_id = input_name[e_loc_start:e_loc_start + 6].upper()

                title = tit
                title += ' - ' + episode_id + ' - '
                title += d[episode_id]['Title'].replace(':', ' -').rstrip()

                output_name = file_path + '/' + title + file_ext
                input_name = download_path + '/' + input_name

                print(output_name, input_name)
                os.rename(input_name, output_name)

    def loadfile(self, data_path, tit):
        with open(data_path + downloader.td[tit]) as json_file:
            return json.load(json_file)
