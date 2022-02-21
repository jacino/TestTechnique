import mysql.connector
from scipy.stats import pearsonr
import pandas as pd


#Connexion à la BD    
connection = mysql.connector.connect(host='localhost', database='test', user='root', password='')

#Récupération des données
query = "SELECT * FROM arbres"
req  = connection.cursor()
req.execute(query)
bd=req.fetchall()

#Mettre les données dans une data frame
df = pd.DataFrame(bd)

#Conversion de string vers int
df[7]=df[7].astype('category').cat.codes
df[2]=df[2].astype('category').cat.codes

# Conversion de la data frame en listes
list1 = df[7]
list2 = df[4]

# Application de pearsonr()
corr, _ = pearsonr(list1, list2)
print('Pearsons correlation: %.3f' % corr)