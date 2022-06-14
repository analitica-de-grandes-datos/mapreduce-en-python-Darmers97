#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':

    value = []
    ky = []

    for line in sys.stdin:

        value.append(int(line.split("\n")[1]))
        ky.append(line.split("\n")[0])

    ky_value = zip(ky, value)
    
    ky_value.sort(key=lambda x:x[1])
    
    for ky, value in ky_value:
      sys.stdout.write("{},{}\n".format(ky, value))
