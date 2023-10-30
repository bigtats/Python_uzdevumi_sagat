"""
Papildināt programmu ar ciklu, kurā sarakstā esošiem uzvārdiem tiktu 
pievienots klāt doktora nosaukums - Dr.
"""

#1varients
saraksts1=["Kalniņš", "Opmanis", "Vēzis", "Almane"]
sarakts2=[]

for uzvards in saraksts1:
    doktors="Dr. "+uzvards
    sarakts2.append(doktors)

print(sarakts2)



