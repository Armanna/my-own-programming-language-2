import sys
import re

print(sys.argv[1])

operators = "+-*:()%"

objects = {}




f = open(sys.argv[1])
for line in f:
    tokens = line.split()
    try:
        if tokens[0] == 'ativ' and len(tokens) == 4:
            try:
                value = int(tokens[3])
                if isinstance(value, int):
                    objects[tokens[1]] = value
                    continue
                else:
                    print("TRACEBACK SXAL")
                    print("Lav ches? 'ativ' tipy yndunum e miayn amboxj tiv / integer")
                    print("Dzi pchi. Tazuc run tur cragiry")
                    exit()
            except: 
                print("TRACEBACK SXAL")
                print("Lav ches? 'ativ' tipy yndunum e miayn amboxj tiv / integer")
                print("Dzi pchi. Tazuc run tur cragiry")
                exit()
        if tokens[0] == 'ttiv' and len(tokens) == 4:
            try:
                value = float(tokens[3])
                if isinstance(value, float):
                    objects[tokens[1]] = value
                    continue
                else:
                    print("TRACEBACK SXAL")
                    print("Lav ches? 'ttiv' tipy yndunum e miayn tasnordakan tiv / float")
                    print("Dzi pchi. Tazuc run tur cragiry")
                    exit()
            except:
                print("TRACEBACK SXAL")
                print("Lav ches? 'ativ' tipy yndunum e miayn amboxj tiv / integer")
                print("Dzi pchi. Tazuc run tur cragiry")
                exit()

        if tokens[0] == 'bar':
            if re.match("^''...''$",tokens[3:]):
                objects[tokens[1]] = tokens[3:]
                continue
            else:
                print("TRACEBACK SXAL")
                print("Lav ches? 'bar' tipy yndunum e miayn tar, bar kam mi toxani text chakertneri mej / string")
                print("Dzi pchi. Tazuc run tur cragiry")
                exit()
        if re.match('^tpel(...)$', tokens[0]):
            if tokens[0][5:-1] in objects.keys():
                print(objects[tokens[0][5:-1]])
            else:
                print("TRACEBACK SXAL")
                print("Yani ches jogum eli vor tenc popoxakan chunes haytararac, ushadir")

        if (tokens[0] == 'ativ' or tokens[0] == 'ttiv') and len(tokens) > 4:
            try:
                s = ''
                for i in tokens[3:]:
                    s = s + ' ' + i
                value = eval(s)
                objects[tokens[1]] = value
                continue

            except:
                print("TRACEBACK SXAL")
                print("Mi ban ni to es arel aper. Tazuc nayi )")
                exit()                





            

    except:
        print("Verj. Shnorhavor, cragird aranc SXAL ashxatec.")


