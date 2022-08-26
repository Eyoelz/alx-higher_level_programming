#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    sys_length = len(sys.argv)
    for i in range (1, sys_length):
        result += sys.argv[i]
    print("{}".format(result))
