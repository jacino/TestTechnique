import requests
import json 
import mysql.connector

#Importation des données via l'API
url = "https://opendata.paris.fr/api/records/1.0/search/?dataset=arbresremarquablesparis&q=&rows=150&facet=libellefrancais&facet=genre&facet=espece&facet=stadedeveloppement&facet=varieteoucultivar&facet=dateplantation"

reponse = requests.get(url)
print(reponse)

#Mettre les données dans un fichier
with open("file.json","w") as outfile :
    
    json.dump(reponse.json(), outfile)

#Ouverture du fichier
f = open ('file.json')

#Chargement des données à partir du fichier
data = json.load(f)

#Chargement des IDBASES
records = data['records']
IDBASES = []
for record in records:
        fields = record['fields']
        IDBASE=fields['idbase']
        IDBASES.append(str(IDBASE))
            
print(IDBASES)
type(IDBASES[0])

#Chargement des LIBELLEFRANCAISS
records = data['records']
LIBELLEFRANCAISS = []
for record in records:
        fields = record['fields']
        LIBELLEFRANCAIS=fields['libellefrancais']
        LIBELLEFRANCAISS.append(LIBELLEFRANCAIS)
            
print(LIBELLEFRANCAISS)
type(LIBELLEFRANCAISS[0])

#Chargement des GENRES
records = data['records']
GENRES = []
for record in records:
        fields = record['fields']
        GENRE=fields['genre']
        GENRES.append(GENRE)
            
print(GENRES)
type(GENRES[0])


#Chargement des ESPECES
records = data['records']
ESPECES = []
for record in records:
        fields = record['fields']
        ESPECE=fields['espece']
        ESPECES.append(ESPECE)
            
print(ESPECES)
type(ESPECES[0])


#Chargement des HAUTEURSENMS
records = data['records']
HAUTEURENMS = []
for record in records:
        fields = record['fields']
        HAUTEURENM=fields['hauteurenm']
        HAUTEURENMS.append(int(HAUTEURENM))
            
print(HAUTEURENMS)
type(HAUTEURENMS[0])

#Chargement des DOMANIALITES
records = data['records']
DOMANIALITES = []
for record in records:
        fields = record['fields']
        DOMANIALITE=fields['domanialite']
        DOMANIALITES.append(DOMANIALITE)
            
print(DOMANIALITES)
type(DOMANIALITES[0])

#Chargement des ARRONDISSEMENTS
records = data['records']
ARRONDISSEMENTS = []
for record in records:
        fields = record['fields']
        ARRONDISSEMENT=fields['arrondissement']
        ARRONDISSEMENTS.append(ARRONDISSEMENT)
            
print(ARRONDISSEMENTS)
type(ARRONDISSEMENTS[0])

#Chargement des STADEDEVELOPPEMENTS
records = data['records']
STADEDEVELOPPEMENTS = []
for record in records:
        fields = record['fields']
        STADEDEVELOPPEMENT=fields['stadedeveloppement']
        STADEDEVELOPPEMENTS.append(STADEDEVELOPPEMENT)
            
print(STADEDEVELOPPEMENTS)
type(STADEDEVELOPPEMENTS[0])



#Connexion à la BD    
connection = mysql.connector.connect(host='localhost', database='test', user='root', password='')

#Fonction d'ajout des données à la BD MySQL
def insert_arbre(IDBASE, LIBELLEFRANCAIS, GENRE, ESPECE, HAUTEURENM, DOMANIALITE, ARRONDISSEMENT, STADEDEVELOPPEMENT):
    query = "INSERT INTO arbres(IDBASE, LIBELLEFRANCAIS, GENRE, ESPECE, HAUTEURENM, DOMANIALITE, ARRONDISSEMENT, STADEDEVELOPPEMENT) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    args = (IDBASE, LIBELLEFRANCAIS, GENRE, ESPECE, HAUTEURENM, DOMANIALITE, ARRONDISSEMENT, STADEDEVELOPPEMENT)
    req  = connection.cursor()
    req.executemany(query, (args,))

#Exécution de la fonction d'ajout
a=len(IDBASES)
i=0   
for i in range(a):
    idbase=IDBASES[i]
    libellefrancais=LIBELLEFRANCAISS[i]
    genre=GENRES[i]
    espece=ESPECES[i]
    hauteurenm=HAUTEURENMS[i]
    domanialite=DOMANIALITES[i]
    arrondissement=ARRONDISSEMENTS[i]
    stadedeveloppement=STADEDEVELOPPEMENTS[i]
    insert_arbre(idbase,libellefrancais,genre,espece,hauteurenm,domanialite, arrondissement, stadedeveloppement)

#Fermeture du fichier    
f.close()
