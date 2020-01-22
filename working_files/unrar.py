import os
import sys

class Unrar:
    def unrar_all_dir(self, download_path, file_path):
        for filename in os.listdir(download_path):
            if filename[filename.rfind('.'):] == ".rar":
                path = (file_path + filename).replace(' ','"\\"')
                os.system('unrar x -psoitgoes ' + path)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print('Error: No Path Entered. Proceeding with run-path')
        main('.')
