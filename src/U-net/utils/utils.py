import argparse
import os


def get_args():
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument(
        '-c', '--config',
        metavar='C',
        default='None',
        help='The Configuration file')
    args = argparser.parse_args()
    return args

def get_files(path, extensions=(".jpeg", ".png", ".tif", ".tiff")):
    """
    Returns list of files which match extensions
    """
    files = []
    for f in os.listdir(path):
        filename, file_extension = os.path.splitext(f)
        if file_extension in extensions:
            files.append(os.path.join(path, f))
    files.sort()
    return files