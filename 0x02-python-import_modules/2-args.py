#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    if argc - 1 > 1:
        print("{} arguments:".format(argc - 1))
        for i in range(1, argc):
            print("{}: {}".format(i, sys.argv[i]))
    elif argc - 1 == 1:
        print("{} argument:".format(argc - 1))
        print("{}: {}".format(argc - 1, sys.argv[argc - 1]))
    else:
        print("{} arguments".format(argc - 1))
