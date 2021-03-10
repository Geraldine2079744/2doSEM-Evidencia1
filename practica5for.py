#for usando listas, en renglon/seguido
#para formar un XML
fxml="<datos>"
for g in ["a","b","c",3,2,1]:
    fxml +="<dato> "+str(g)+" </dato>  "
print(fxml)
