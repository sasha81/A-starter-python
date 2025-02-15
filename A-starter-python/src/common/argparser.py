import argparse

def getParser():

    parser = argparse.ArgumentParser(description="Just an example",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-m", "--mode", type=str, default='dev',help="run mode: dev/tests/prod")
    # parser.add_argument("-v", "--verbose", action="store_true", help="increase verbosity")
    # parser.add_argument("-B", "--block-size", help="checksum blocksize")
    # parser.add_argument("--ignore-existing", action="store_true", help="skip files that exist")
    # parser.add_argument("--exclude", help="files to exclude")
    # parser.add_argument("src", help="Source location")
    # parser.add_argument("dest", help="Destination location")
    return parser