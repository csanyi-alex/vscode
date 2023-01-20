try:
    number = int(input("How big do u want it to be? (might crash potato PCs)"))

except:
    print ("Value error ._.")

filler = open("text.txt", "a")
for i in range(0,12):
    filler.write(str(123456**i))
    filler.flush()