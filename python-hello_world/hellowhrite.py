import sys

def write():
    massage = "and that piece of art is useful - Dora Korpar, 2015-10-19"
    sys.stderr.write(massage +"\n")

    sys.exit(1)


if __name__ == "__main__":
    write()
