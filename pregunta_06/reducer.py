#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    max = 0
    min = 1000

    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:
            if max <= val:
                max = val
            if min >= val:
                min = val
        else:

            if curkey is not None:

                sys.stdout.write("{}\t{}\t{}\n".format(curkey, max, min))
