import os
import sys


class Unrar:
    def unrar_all_dir(self, download_path, file_path):
        for filename in os.listdir(download_path):
            if filename[filename.rfind('.'):] == '.rar':
                path = ((download_path + '/' + filename).replace(' ', '\\ '))
                os.system('unrar x -psoitgoes ' + path)
                os.system('rm ' + path)
                print('mv ' + filename + ' ' + file_path)
                os.system('mv *.mkv ' + download_path.replace(' ', '\\ '))
