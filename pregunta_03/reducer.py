#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':

    value = []
    ky = []

    for line in sys.stdin:

        value.append(line.split("\t")[1])
        ky.append(line.split("\t")[0])

    ky_value = zip(ky, int(value))
    
    ky_value.sort(key=lambda x:x[1])
    
    for ky, value in ky_value:
      sys.stdout.write("{},{}\n".format(ky, value))
