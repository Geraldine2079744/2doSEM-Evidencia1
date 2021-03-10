#for usando listas, en renglon/seguido
#para formar un XML
print("<datos>")
for g in ["a","b","c",3,2,1]:
    print("<dato> "+str(g),end=" </dato>")
print("")
print("</datos>")
