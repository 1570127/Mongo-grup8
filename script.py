from pymongo import MongoClient
import csv
import datetime

# Import csv
clients = []
with open('./clients.csv') as file:
    clients_data = csv.reader(file)
    noms = clients_data.__next__()
    noms = noms[0].split('\t')
    for i in clients_data:
        i = i[0].split('\t')
        client = {}
        targeta = []
        for idx, j in enumerate(noms):
            client[j] = i[idx]
            if j == "edat" or j == "codi_postal":
                client[j] = int(i[idx])
        clients.append(client)

cotxes = []
with open('./cotxes.csv') as file:
    cotxes_data = csv.reader(file)
    noms = cotxes_data.__next__()
    noms = noms[0].split('\t')
    for i in cotxes_data:
        i = i[0].split('\t')
        cotxe = {}
        for idx, j in enumerate(noms):
            cotxe[j] = i[idx]
        cotxes.append(cotxe)

estades = []
with open('./estades.csv') as file:
    estades_data = csv.reader(file)
    noms = estades_data.__next__()
    noms = noms[0].split('\t')
    for i in estades_data:
        i = i[0].split('\t')
        estada = {}
        for idx, j in enumerate(noms):
            estada[j] = i[idx]
            if j == "data_hora_sortida" or j == "data_hora_entrada":
                estada[j] = datetime.datetime.strptime(i[idx], "%d-%m-%Y:%H:%M")
            elif j == "id" or j == "porta_entrada" or j == "porta_sortida" or j == "placa":
                estada[j] = int(i[idx])
        estades.append(estada)

places = []
with open('./places_parking.csv') as file:
    places_data = csv.reader(file)
    noms = places_data.__next__()
    noms = noms[0].split('\t')
    for i in places_data:
        i = i[0].split('\t')
        placa = {}
        for idx, j in enumerate(noms):
            try:
                placa[j] = int(i[idx])
            except:
                placa[j] = (i[idx] == "si")
        places.append(placa)

productes = []
with open('./productes.csv') as file:
    productes_data = csv.reader(file)
    noms = productes_data.__next__()
    noms = noms[0].split('\t')   
    for i in productes_data:
        i = i[0].split('\t')
        producte = {}
        for idx, j in enumerate(noms):
            producte[j] = i[idx]
            if j == "codi":
                producte[j] = int(i[idx])
            elif j == "pes" or j == "preu":
                producte[j] = float(i[idx])
        productes.append(producte)

tiquets = []
with open('./tiquets.csv') as file:
    tiquets_data = csv.reader(file)
    noms = tiquets_data.__next__()
    noms = noms[0].split('\t')
    for i in tiquets_data:
        i = i[0].split('\t')
        tiquet = {}
        for idx, j in enumerate(noms):
            tiquet[j] = i[idx]
            if j == "id_tiquet":
                tiquet[j] = int(i[idx])
            elif j == "preu_total":
                tiquet[j] = float(i[idx])
            elif j == "data":
                tiquet[j] = datetime.datetime.strptime(i[idx], "%d/%m/%Y")
        tiquets.append(tiquet)

packs = []
with open('./pack.csv') as file:
    packs_data = csv.reader(file)
    noms = packs_data.__next__()
    noms = noms[0].split('\t')
    for i in packs_data:
        i = i[0].split('\t')
        pack = {}
        for idx, j in enumerate(noms):
            pack[j] = int(i[idx])
        packs.append(pack)

targetes = []
with open('./targetes.csv') as file:
    targetes_data = csv.reader(file)
    noms = targetes_data.__next__()
    noms = noms[0].split('\t')
    for i in targetes_data:
        i = i[0].split('\t')
        targeta = {}
        for idx, j in enumerate(noms):
            targeta[j] = i[idx]
            if j == "numero":
                targeta[j] = int(i[idx])
        targetes.append(targeta)

tiquet_productes = []
with open('./tiquet_producte.csv') as file:
    tiquet_productes_data = csv.reader(file)
    noms = tiquet_productes_data.__next__()
    noms = noms[0].split('\t')
    for i in tiquet_productes_data:
        i = i[0].split('\t')
        targeta = {}
        for idx, j in enumerate(noms):
            targeta[j] = int(i[idx])
        tiquet_productes.append(targeta)

# Fer les connexions
for i in clients:
    i["tiquets"] = []
    for j in tiquets:
        if i["DNI"] == j["DNI"]:
            i["tiquets"].append(j["id_tiquet"])

for i in clients:
    i["cotxes"] = []
    for j in cotxes:
        if i["DNI"] == j["DNI"]:
            i["cotxes"].append(j["matricula"])

for i in cotxes:
    i["estades"] = []
    for j in estades:
        if i["matricula"] == j["matricula"]:
            i["estades"].append(j["id"])

for i in places:
    i["estades"] = []
    for j in estades:
        if i["id_placa"] == j["placa"]:
            i["estades"].append(j["id"])

for i in clients:
    i["targetes"] = []
    for j in targetes:
        if i["DNI"] == j["DNI"]:
            i["targetes"].append(j["numero"])

# Passar-ho a Mongodb
Host = 'localhost'
Port = 27017

DSN = "mongodb://{}:{}".format(Host,Port)

conn = MongoClient(DSN)

db = conn.botiga

db.clients
db.clients.drop()
db.clients.insert_many(clients)

db.cotxes
db.cotxes.drop()
db.cotxes.insert_many(cotxes)

db.estades
db.estades.drop()
db.estades.insert_many(estades)

db.places
db.places.drop()
db.places.insert_many(places)

db.productes
db.productes.drop()
db.productes.insert_many(productes)

db.tiquets
db.tiquets.drop()
db.tiquets.insert_many(tiquets)

db.packs
db.packs.drop()
db.packs.insert_many(packs)

db.targetes
db.targetes.drop()
db.targetes.insert_many(targetes)

db.tiquet_productes
db.tiquet_productes.drop()
db.tiquet_productes.insert_many(tiquet_productes)
