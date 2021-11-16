szamok=[3,4,2,7,8,1,9,7,3,2,3,5,1,6,7,3,2,7,4,3,7,5,8,9,9,8,8,]
print(szamok)


#összegzés tétele
osszeg=0
for x in szamok:
    osszeg=osszeg+x    
print(osszeg)

print(sum(szamok))

#eldöntés tétele
vane=False
for x in szamok:
    if(x==1):
        vane=True
print(vane)

#Megszámlálás tétele:Hány darab hármas van benne ? 
db=0
for x in szamok:
    if (x==3):
         db=db+1;
print("A hármasok darabszáma: ")
print(db)

#Feltételes összegzés:Csak a páros számokat összegzem.
osszeg=0
for x in szamok:
    if (x%2==0): 
        osszeg=osszeg+x;
print("Páros számok összege: ")
print(osszeg)

#Minimum kiválasztás tétele:
print("Minimum kiválasztás tétele:")
min1=1000
for x in szamok:
    if (x<min1):                  
        min1=x   
print(min1)       

print(min(szamok))


#Maximum kiválasztás tétele:
print("Maximum kiválasztás tétele:")
max1=-1000
for x in szamok:
    if (x>max1):
        max1=x
print(max1)
print(max(szamok))

print("Feladat")

lista=[4,9,33,53,67,74,99,61,1,10]
#Átlag
szamolas=sum(lista)/len(lista)
print(szamolas)
#Minimum
print(min(lista))
#Maximum
print(max(lista))
#Van-e benne páros szám?
vane=False
for x in lista:
    if(x%2==0):
        vane=True
print(vane)
#Add össze az 50-nél nagyobb számokat
otven=0
for x in lista:
    if (x>50): 
        otven=otven+x;
print(otven)

#Hány darab 9-es van benne?
db=0
for x in lista:
    if (x==9):
         db=db+1;
print(db)