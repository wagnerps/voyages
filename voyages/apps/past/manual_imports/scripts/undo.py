import mysql.connector
import time
import json
import re

d=open("dbcheckconf.json","r")
t=d.read()
d.close()
conf=json.loads(t)

cnx = mysql.connector.connect(**conf)
cursor = cnx.cursor()

cursor.execute('delete from past_enslavervoyageconnection')
cnx.commit()

cursor.execute('delete from past_enslaverinrelation')
cnx.commit()

cursor.execute('delete from past_enslaveralias')
cnx.commit()

cursor.execute('delete from past_enslaveridentity')
cnx.commit()

cursor.execute('delete from past_enslavedinrelation')
cnx.commit()

cursor.execute('delete from past_enslavementrelation')
cnx.commit()


cnx.close()

