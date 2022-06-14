#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':

    value = []
    ky = []

    for line in sys.stdin:
        ky.append(line.split("\t")[0])
        value.append(int(line.split("\t")[1]))

    ky_value = zip(ky, value)

    ky_value_2 = sorted(ky_value,key=lambda x:x[1])

    for ky, value in ky_value_2:
      sys.stdout.write("{},{}\n".format(ky, value))
