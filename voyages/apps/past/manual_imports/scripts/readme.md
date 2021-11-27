Documenting the workflow here for sanity's sake.

1. We dump the production sql
1. Domingos shifts over all the new values from it into his past build
1. Domingos then runs the enslaved import off the PAST csvs
1. Domingos sends me his sql dump from python3 past
1. I then wipe the database on this specific migration branch and remove the voyage and past migrations dating from 2021
1. I check Domingos' models against mine (I'm adding in a text_ref field into enslaver identity & alias models to keep track of individuals)
1. I then apply the existing migrations to this blank db
1. I inject Domingos' sql dump into it
1. I then manually add in my extra columns, god help me
1. I run my migration scripts
1. I dump the sql & hand it back to Domingos
1. He pulls the values from these and updates all his enslaver & relation tables with it



	alter table voyages_jcm_nov23_enslaverdatamigration.past_enslaveridentity add column text_id varchar(255);
	alter table voyages_jcm_nov23_enslaverdatamigration.past_enslaveralias add column text_id varchar(255);
	alter table past_enslaveridentity add column principal_location_id int;
	alter table past_enslaveridentity add foreign key (principal_location_id) references voyage_place(id);