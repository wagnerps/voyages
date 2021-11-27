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

queries=[
	"alter table voyages_jcm_nov23_enslaverdatamigration.past_enslaveridentity add column text_id varchar(255);",
	"alter table voyages_jcm_nov23_enslaverdatamigration.past_enslaveralias add column text_id varchar(255);",
	"alter table past_enslaveridentity add column principal_location_id int;",
	"alter table past_enslaveridentity add foreign key (principal_location_id) references voyage_place(id);",
	"alter table past_enslavementrelation add column transaction_id int;",
	"ALTER TABLE past_enslaverinrelation drop foreign key `past_enslaverinrelat_transaction_id_a9604345_fk_past_ensl`;",
	"ALTER TABLE past_enslavedinrelation drop foreign key `past_enslavedinrelat_transaction_id_28a692bb_fk_past_ensl`;",
	"ALTER TABLE past_enslavementrelation MODIFY id INT AUTO_INCREMENT;",
	"ALTER TABLE past_enslavedinrelation add foreign key (transaction_id) references past_enslavementrelation(id);",
	"ALTER TABLE past_enslaverinrelation add foreign key (transaction_id) references past_enslavementrelation(id);",
	"ALTER TABLE past_enslavedinrelation MODIFY id INT AUTO_INCREMENT;",
	"ALTER TABLE past_enslaverinrelation MODIFY id INT AUTO_INCREMENT;"
	]

for q in queries:
	cursor.execute(q)
	cnx.commit()

	
