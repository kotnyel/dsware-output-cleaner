# dsware putput cleaner by leni 2023 v0.1 beta

# file io and paramterter bypass
import sys
# regex
import re

print("#### lenIs dsware export pharser v0.1 beta ####")

#test data: C:\Users\H103667842\Desktop\PREPROD-case\20230130\172_16_64_40_pool_1

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
print(sys.argv[1])

if n!=1:
    print("Usage: dswarepharser.py filename")
    print("  Output: filename.csv file for excel opening ")


if n>1 :

    try:
        f = open(sys.argv[1], "r")
    except:
        print("File is not exists on the specified location!")
        exit()

    try:
        ft = open(sys.argv[1]+".csv","w")
    except:
        print("Unable to open the output file!")
        exit()

    Lines = f.readlines()
    lc = 0
    records = 0
    sizes = 0

    for line in Lines:
        lc += 1

        if lc == 4:
            lineout= re.sub("\s+", ";", line.strip())
            ft.write(lineout)
        if lc > 5:
            lineout= re.sub("\s+", ";", line.strip())
            
            ft.write(lineout)
            records += 1
            value = lineout.split(";")[1]
            sizes = sizes+ int(value)
            #print(sizes)
    ft.write( "Total number of records;Total sizes [mb]")
    ft.write( str(records)+";"+ str(sizes))
    ft.write( "Total number of records;Total sizes [tb]")
    ft.write( str(records)+";"+ str(sizes/1000/1000))
    print( "Total number of records;Total sizes [mb]")
    print( records,";", sizes)
    print( "Total number of records;Total sizes [tb]")
    print( records,";", sizes/1000/1000)
    f.close()
    ft.close()
exit()



