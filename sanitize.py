import os
import argparse

__author__ = 'yazan'

def main(args):
    for i, filename in enumerate(os.listdir(args.dir)):
        print "Scanning {}".format(args.dir)
        if filename.endswith(".mp3") or filename.endswith(".flac"):
            new_file = filename
            if args.replace:
                for repl in args.replace.split(','):
                    a, b = tuple(repl.split(':'))
                    new_file = new_file.replace(a, b)
            if args._delete:
                for d in args._delete.split(','):
                    new_file = new_file.replace(d, "")
            if new_file.startswith("-"):
                new_file = new_file[1:]
            new_full_path = os.path.join(args.dir, new_file)
            full_path = os.path.join(args.dir, filename)
            os.rename(full_path, new_full_path)
            print "Modified: {} => {}".format(filename, new_file)

    print "Sucessfully moodified {} files.".format(i)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser(description='Mp3 and FLAC filename fixer')

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("dir", help="File directory, full path")

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-d", "--delete", action="store", dest="_delete", help="Strings to delete, separated by comma. E.g.: Frank,Sinatra,delete,this,message")

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-r", "--replace", action="store", dest="replace", help="Strings to replace, separated by comma, match:replace separated by colon. E.g.: change:to,ALBUM:album,replace:Replace")
    args = parser.parse_args()
    main(args)
