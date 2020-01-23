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

    if int(sea) < 10: sea = '0' + sea

    ep_l = ep.split('-')

    if len(ep_l) == 1:
        epi_num = 1
    else:
        epi_num = int(ep_l[1]) - int(ep_l[0]) + 1

    ep_l_t = []
    for i in range(int(ep_l[0]), int(ep_l[0]) + epi_num):
        print(i)
        i_str = str(i)
        if i < 10:
            i_str = '0' + i_str
        ep_l_t.append(i_str)
    ep_l = ep_l_t

    main()
