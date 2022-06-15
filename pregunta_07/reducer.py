#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':

    letter = []
    date = []
    num = []

    for line in sys.stdin:
        letter.append(line.split("\t")[0])
        date.append(line.split("\t")[1])
        num.(int(line.split("\t")[0]))

    ky_value = zip(letter, date, num)

    ky_value_2 = sorted(ky_value,key=lambda x:(x[0],x[2]))

    for ky, value in ky_value_2:
      sys.stdout.write("{} {} {}\n".format(letter, date, num))
