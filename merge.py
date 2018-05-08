import shutil
import glob

with open('merge', 'wb') as outfile:
    for filename in glob.glob('nikhil*'):
        if filename == 'merge':
            # don't want to copy the output into the output
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)