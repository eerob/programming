"""
Add metadata to all the .mp4 files within the given directory, based on the file
names of the input files.

Each input file should use the following format for their filename:

[name]  [(release date)]

Note the release date must have parenthesis around it and be in the formate (YYYY-MM-DD)

Usage: python add_metadata.py /path/to/mp4/files/

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
    dirname = sys.argv[1]
    mp4_files = (f for f in os.listdir(dirname) if f.endswith('.mp4'))

    for mp4_file in mp4_files:
        input_path = op.join(dirname, mp4_file)
        name, release_date = op.splitext(mp4_file)[0].split('(')
        release_date = release_date.strip(')')
        output_path = op.join(dirname+'/output', '%s(%s).mp4' % (name, release_date)) # put the new files in a folder in the current directory called output, you must make the folder called output the program won't create it

        cmd = [
            'ffmpeg',
            '-i', input_path,
            '-c', 'copy',   # copy, dont' reencode
            '-metadata', 'title=' + name,   # ffmpeg only lets you use certain metadata tags. this is supposed to be the list, but I had to use date instead of year https://wiki.multimedia.cx/index.php/FFmpeg_Metadata
            '-metadata', 'date=' + release_date,
            output_path,
        ]
        print(' '.join(cmd))
        subprocess.call(cmd)
