szamok=[3,4,2,7,8,1,9,7,3]
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
print(db)



