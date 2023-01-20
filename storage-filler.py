try:
    size = int(input("How big do u want it to be? 0 - 9,223,372,036,854,775,807 (might crash potato PCs)"))

except:
    print ("Value error ._.")

filler = open("text.txt", "a")

for i in range(0,size):
    filler.write(str(123456789101112**i))
    filler.flush()