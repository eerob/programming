"""
Merge all mp4 files in a directory into a single mp4 file

Each input file should be named in ascending order in the order you want

The name of the directoy that holds the files will be the name of the output mp4 file

Usage: python add_metadata.py /path/to/mp4/file direcotory/

If directory path has spaces use single quotes to escape ex:
/Users/rob/Movies/To_Convert/PRG001/'Christmas at Grams (2007-12-26)'
Full terminal command
python merge_mp4.py /Users/rob/Movies/To_Convert/PRG001/'Christmas at Grams (2007-12-26)'

In order to run this script, you must have ffmpeg installed. On MAC, you can 
do so by using brew (install brew first). brew install ffmpeg

Sources:
http://superuser.com/questions/349518/how-to-use-ffmpeg-to-add-metadata-to-an-aac-file-without-reencoding
http://jonhall.info/how_to/create_id3_tags_using_ffmpeg

"""

import sys
import os
import os.path as op
import subprocess


if __name__ == '__main__':
    DIR_PATH = sys.argv[1]
    mp4_files = os.listdir(DIR_PATH)
    mp4_files.sort()
    DIR_NAME = os.path.basename(os.path.normpath(DIR_PATH))
    # print(mp4_files)

    with open('file_list.txt', 'w', encoding='utf-8') as f:
        for file in mp4_files:
            if file.endswith('.mp4'):
                f.write('file ' + "'" + DIR_PATH + '/' + file + "'" + '\n')

    cmd = [
        'ffmpeg',
        '-f', 'concat',
        '-safe', '0',
        '-i', 'file_list.txt',
        '-c', 'copy',   # copy, dont' reencode
        DIR_NAME + '.mp4',
    ]
    print(' '.join(cmd))
    subprocess.call(cmd)
