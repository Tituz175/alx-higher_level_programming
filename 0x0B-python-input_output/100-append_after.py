#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    print(search_string)
    with open(filename, "r+", encoding="utf-8") as f:
        for line in f:
            if search_string in line:
                print(f.tell())
                # print(line, end="")
        
                # f.write(new_string)
        # if (search_string in f.readline()):
        #     print(f.readline())
