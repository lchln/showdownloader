"""

TODO: Documentation, Hiding Script OUtputs, Error Handling, COmments, Othr SHows

By: Lachlan Milne

"""
from working_files import downloader
from working_files import unrar
from working_files import rename
import sys
import os

tit = ''
sea = ''
ep_l = []


def main():
    rn = rename.Rename()
    dl = downloader.Downloader()
    un = unrar.Unrar()

    home_path = os.path.expanduser('~')
    data_path = home_path + '/Projects/showdownloader/working_files/data'
    file_path = dl.get_file_path(home_path, tit)
    season_path = dl.get_file_path(home_path, tit, sea)
    download_path = file_path + '/Downloads'

    dl.download_files(home_path, data_path, tit, sea, ep_l)
    un.unrar_all_dir(download_path, file_path)
    rn.rename_folder(data_path, download_path, season_path, tit, sea)


if __name__ == '__main__':
    try:
        tit = sys.argv[1]
    except:
        tit = input('Title: ')

    try:
        sea = sys.argv[2]
    except:
        sea = input('Season: ')

    try:
        ep = sys.argv[3]
    except:
        ep = input('Episode(s): ')

    ep_l = ep.split('-')

    try:
        if int(sea) < 10: sea = '0' + sea
        if int(ep_l[0]) < 10: ep_l[0] = '0' + ep_l[0]
        if int(ep_l[1]) < 10: ep_l[0] = '0' + ep_l[1]
    except:
        print()

    main()
