# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='BroadRegion',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('broad_region',
                 models.CharField(max_length=255,
                                  verbose_name='Broad region (Area) name')),
                ('longitude',
                 models.DecimalField(null=True,
                                     verbose_name='Longitude of point',
                                     max_digits=10,
                                     decimal_places=7,
                                     blank=True)),
                ('latitude',
                 models.DecimalField(null=True,
                                     verbose_name='Latitude of point',
                                     max_digits=10,
                                     decimal_places=7,
                                     blank=True)),
                ('value', models.IntegerField(verbose_name='Numeric code')),
                ('show_on_map', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['value'],
                'verbose_name': 'Broad region (area)',
                'verbose_name_plural': 'Broad regions (areas)',
            },
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('label', models.CharField(max_length=255)),
                ('value', models.IntegerField()),
            ],
            options={
                'ordering': ['value'],
                'verbose_name': 'Nationality',
                'verbose_name_plural': 'Nationalities',
            },
        ),
        migrations.CreateModel(
            name='OwnerOutcome',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('label',
                 models.CharField(max_length=200,
                                  verbose_name='Outcome label')),
                ('value',
                 models.IntegerField(verbose_name='Code of outcome')),
            ],
            options={
                'ordering': ['value'],
            },
        ),
        migrations.CreateModel(
            name='ParticularOutcome',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('label',
                 models.CharField(max_length=200,
                                  verbose_name='Outcome label')),
                ('value',
                 models.IntegerField(verbose_name='Code of outcome')),
            ],
            options={
                'ordering': ['value'],
                'verbose_name': 'Fate (particular outcome of voyage)',
                'verbose_name_plural':
                'Fates (particular outcomes of voyages)',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('place', models.CharField(max_length=255)),
                ('value',
                 models.IntegerField(unique=True,
                                     verbose_name='Numeric code')),
                ('longitude',
                 models.DecimalField(null=True,
                                     verbose_name='Longitude of point',
                                     max_digits=10,
                                     decimal_places=7,
                                     blank=True)),
                ('latitude',
                 models.DecimalField(null=True,
                                     verbose_name='Latitude of point',
                                     max_digits=10,
                                     decimal_places=7,
                                     blank=True)),
                ('show_on_main_map', models.BooleanField(default=True)),
                ('show_on_voyage_map', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['value'],
                'verbose_name': 'Place (Port or Location)',
                'verbose_name_plural': 'Places (Ports or Locations)',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('region',
                 models.CharField(
                     max_length=255,
                     verbose_name='Specific region (country or colony)')),
                ('longitude',
                 models.DecimalField(null=True,
                                     verbose_name='Longitude of point',
                                     max_digits=10,
                                     decimal_places=7,
                                     blank=True)),
                ('latitude',
                 models.DecimalField(null=True,
                                     verbose_name='Latitude of point',
                                     max_digits=10,
                                     decimal_places=7,
                                     blank=True)),
                ('value', models.IntegerField(verbose_name='Numeric code')),
                ('show_on_map', models.BooleanField(default=True)),
                ('show_on_main_map', models.BooleanField(default=True)),
                ('broad_region', models.ForeignKey(to='voyage.BroadRegion',
                                                   on_delete=models.CASCADE)),
            ],
            options={
                'ordering': ['value'],
            },
        ),
        migrations.CreateModel(
            name='Resistance',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('label',
                 models.CharField(max_length=255,
                                  verbose_name='Resistance label')),
                ('value',
                 models.IntegerField(verbose_name='Code of resistance')),
            ],
            options={
                'ordering': ['value'],
            },
        ),
        migrations.CreateModel(
            name='RigOfVessel',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('label', models.CharField(max_length=25)),
                ('value', models.IntegerField()),
            ],
            options={
                'ordering': ['value'],
                'verbose_name': 'Rig of vessel',
                'verbose_name_plural': 'Rigs of vessel',
            },
        ),
        migrations.CreateModel(
            name='SlavesOutcome',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('label',
                 models.CharField(max_length=200,
                                  verbose_name='Outcome label')),
                ('value',
                 models.IntegerField(verbose_name='Code of outcome')),
            ],
            options={
                'ordering': ['value'],
            },
        ),
        migrations.CreateModel(
            name='TonType',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('label', models.CharField(max_length=255)),
                ('value', models.IntegerField()),
            ],
            options={
                'ordering': ['value'],
                'verbose_name': 'Type of tons',
                'verbose_name_plural': 'Types of tons',
            },
        ),
        migrations.CreateModel(
            name='VesselCapturedOutcome',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('label',
                 models.CharField(max_length=200,
                                  verbose_name='Outcome label')),
                ('value',
                 models.IntegerField(verbose_name='Code of outcome')),
            ],
            options={
                'ordering': ['value'],
            },
        ),
        migrations.CreateModel(
            name='Voyage',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('voyage_id',
                 models.IntegerField(unique=True, verbose_name='Voyage ID')),
                ('voyage_in_cd_rom',
                 models.BooleanField(default=False,
                                     max_length=1,
                                     verbose_name='Voyage in 1999 CD-ROM?')),
            ],
            options={
                'ordering': ['voyage_id'],
                'verbose_name': 'Voyage',
                'verbose_name_plural': 'Voyages',
            },
        ),
        migrations.CreateModel(
            name='VoyageCaptain',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('name',
                 models.CharField(max_length=255,
                                  verbose_name="Captain's name")),
            ],
        ),
        migrations.CreateModel(
            name='VoyageCaptainConnection',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('captain_order', models.IntegerField()),
                ('captain',
                 models.ForeignKey(related_name='captain_name',
                                   to='voyage.VoyageCaptain',
                                   on_delete=models.CASCADE)),
                ('voyage',
                 models.ForeignKey(related_name='voyage',
                                   to='voyage.Voyage',
                                   on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Voyage captain information',
                'verbose_name_plural': 'Voyage captain information',
            },
        ),
        migrations.CreateModel(
            name='VoyageCrew',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('crew_voyage_outset',
                 models.IntegerField(null=True,
                                     verbose_name='Crew at voyage outset',
                                     blank=True)),
                ('crew_departure_last_port',
                 models.IntegerField(
                     null=True,
                     verbose_name='Crew at departure from last port of slave '
                                  'purchase',
                     blank=True)),
                ('crew_first_landing',
                 models.IntegerField(
                     null=True,
                     verbose_name='Crew at first landing of slaves',
                     blank=True)),
                ('crew_return_begin',
                 models.IntegerField(
                     null=True,
                     verbose_name='Crew when return voyage begin',
                     blank=True)),
                ('crew_end_voyage',
                 models.IntegerField(null=True,
                                     verbose_name='Crew at end of voyage',
                                     blank=True)),
                ('unspecified_crew',
                 models.IntegerField(null=True,
                                     verbose_name='Number of crew '
                                                  'unspecified',
                                     blank=True)),
                ('crew_died_before_first_trade',
                 models.IntegerField(
                     null=True,
                     verbose_name='Crew died before first place of trade in '
                                  'Africa',
                     blank=True)),
                ('crew_died_while_ship_african',
                 models.IntegerField(
                     null=True,
                     verbose_name='Crew died while ship was on African coast',
                     blank=True)),
                ('crew_died_middle_passage',
                 models.IntegerField(
                     null=True,
                     verbose_name='Crew died during Middle Passage',
                     blank=True)),
                ('crew_died_in_americas',
                 models.IntegerField(null=True,
                                     verbose_name='Crew died in the Americas',
                                     blank=True)),
                ('crew_died_on_return_voyage',
                 models.IntegerField(null=True,
                                     verbose_name='Crew died on return '
                                                  'voyage',
                                     blank=True)),
                ('crew_died_complete_voyage',
                 models.IntegerField(
                     null=True,
                     verbose_name='Crew died during complete voyage',
                     blank=True)),
                ('crew_deserted',
                 models.IntegerField(
                     null=True,
                     verbose_name='Total number of crew deserted',
                     blank=True)),
                ('voyage',
                 models.ForeignKey(related_name='voyage_name_crew',
                                   blank=True,
                                   to='voyage.Voyage',
                                   null=True,
                                   on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Crew',
                'verbose_name_plural': 'Crews',
            },
        ),
        migrations.CreateModel(
            name='VoyageDates',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('voyage_began',
                 models.CommaSeparatedIntegerField(
                     help_text='Date in format: MM,DD,YYYY',
                     max_length=10,
                     null=True,
                     verbose_name='Date that voyage began (DATEDEPB,A,C)',
                     blank=True)),
                ('slave_purchase_began',
                 models.CommaSeparatedIntegerField(
                     help_text='Date in format: MM,DD,YYYY',
                     max_length=10,
                     null=True,
                     verbose_name='Date that slave purchase began '
                                  '(D1SLATRB,A,C)',
                     blank=True)),
                ('vessel_left_port',
                 models.CommaSeparatedIntegerField(
                     help_text='Date in format: MM,DD,YYYY',
                     max_length=10,
                     null=True,
                     verbose_name='Date that vessel left last slaving port '
                                  '(DLSLATRB,A,C)',
                     blank=True)),
                ('first_dis_of_slaves',
                 models.CommaSeparatedIntegerField(
                     help_text='Date in format: MM,DD,YYYY',
                     max_length=10,
                     null=True,
                     verbose_name='Date of first disembarkation of slaves '
                                  '(DATARR33,32,34)',
                     blank=True)),
                ('date_departed_africa',
                 models.CommaSeparatedIntegerField(
                     help_text='Date in format: MM,DD,YYYY',
                     max_length=10,
                     null=True,
                     verbose_name='Date vessel departed Africa (DATELEFTAFR)',
                     blank=True)),
                ('arrival_at_second_place_landing',
                 models.CommaSeparatedIntegerField(
                     help_text='Date in format: MM,DD,YYYY',
                     max_length=10,
                     null=True,
                     verbose_name='Date of arrival at second place of '
                                  'landing (DATARR37,36,38)',
                     blank=True)),
                ('third_dis_of_slaves',
                 models.CommaSeparatedIntegerField(
                     help_text='Date in format: MM,DD,YYYY',
                     max_length=10,
                     null=True,
                     verbose_name='Date of third disembarkation of slaves '
                                  '(DATARR40,39,41)',
                     blank=True)),
                ('departure_last_place_of_landing',
                 models.CommaSeparatedIntegerField(
                     help_text='Date in format: MM,DD,YYYY',
                     max_length=10,
                     null=True,
                     verbose_name='Date of departure from last place of '
                                  'landing (DDEPAMB,*,C)',
                     blank=True)),
                ('voyage_completed',
                 models.CommaSeparatedIntegerField(
                     help_text='Date in format: MM,DD,YYYY',
                     max_length=10,
                     null=True,
                     verbose_name='Date on which slave voyage completed '
                                  '(DATARR44,43,45)',
                     blank=True)),
                ('length_middle_passage_days',
                 models.IntegerField(
                     null=True,
                     verbose_name='Length of Middle Passage in (days) '
                                  '(VOYAGE)',
                     blank=True)),
                ('imp_voyage_began',
                 models.CommaSeparatedIntegerField(
                     help_text='Date in format: MM,DD,YYYY',
                     max_length=10,
                     null=True,
                     verbose_name='Year voyage began',
                     blank=True)),
                ('imp_departed_africa',
                 models.CommaSeparatedIntegerField(
                     help_text='Date in format: MM,DD,YYYY',
                     max_length=10,
                     null=True,
                     verbose_name='Year departed Africa',
                     blank=True)),
                ('imp_arrival_at_port_of_dis',
                 models.CommaSeparatedIntegerField(
                     help_text='Date in format: MM,DD,YYYY',
                     max_length=10,
                     null=True,
                     verbose_name='Year of arrival at port of '
                                  'disembarkation (YEARAM)',
                     blank=True)),
                ('imp_length_home_to_disembark',
                 models.IntegerField(
                     null=True,
                     verbose_name='Voyage length from home port to '
                                  'disembarkation (days) (VOY1IMP)',
                     blank=True)),
                ('imp_length_leaving_africa_to_disembark',
                 models.IntegerField(
                     null=True,
                     verbose_name='Voyage length from leaving Africa to '
                                  'disembarkation (days) (VOY2IMP)',
                     blank=True)),
                ('voyage',
                 models.ForeignKey(related_name='voyage_name_dates',
                                   blank=True,
                                   to='voyage.Voyage',
                                   null=True,
                                   on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Date',
                'verbose_name_plural': 'Dates',
            },
        ),
        migrations.CreateModel(
            name='VoyageGroupings',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('label', models.CharField(max_length=30)),
                ('value', models.IntegerField()),
            ],
            options={
                'verbose_name':
                    'Grouping for estimating imputed slaves',
                'verbose_name_plural':
                    'Groupings for estimating imputed slaves',
            },
        ),
        migrations.CreateModel(
            name='VoyageItinerary',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('ports_called_buying_slaves',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of ports of call prior to buying '
                                  'slaves (NPPRETRA)',
                     blank=True)),
                ('number_of_ports_of_call',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of ports of call in Americas prior '
                                  'to sale of slaves (NPPRIOR)',
                     blank=True)),
                ('broad_region_of_return',
                 models.ForeignKey(
                     related_name='broad_region_of_return',
                     verbose_name='Broad region of return (RETRNREG1)',
                     blank=True,
                     to='voyage.BroadRegion',
                     null=True,
                     on_delete=models.CASCADE)),
                ('first_landing_place',
                 models.ForeignKey(
                     related_name='first_landing_place',
                     verbose_name='First place of slave landing (SLA1PORT)',
                     blank=True,
                     to='voyage.Place',
                     null=True,
                     on_delete=models.CASCADE)),
                ('first_landing_region',
                 models.ForeignKey(
                     related_name='first_landing_region',
                     verbose_name='First region of slave landing (REGDIS1)',
                     blank=True,
                     to='voyage.Region',
                     null=True,
                     on_delete=models.CASCADE)),
                ('first_place_slave_purchase',
                 models.ForeignKey(
                     related_name='first_place_slave_purchase',
                     verbose_name='First place of slave purchase (PLAC1TRA)',
                     blank=True,
                     to='voyage.Place',
                     null=True,
                     on_delete=models.CASCADE)),
                ('first_region_slave_emb',
                 models.ForeignKey(
                     related_name='first_region_slave_emb',
                     verbose_name='First region of embarkation of slaves '
                                  '(REGEM1)',
                     blank=True,
                     to='voyage.Region',
                     null=True,
                     on_delete=models.CASCADE)),
                ('imp_broad_region_of_slave_purchase',
                 models.ForeignKey(
                     related_name='imp_broad_region_of_slave_purchase',
                     verbose_name='Imputed principal broad region of slave '
                                  'purchase (MAJBYIMP1)',
                     blank=True,
                     to='voyage.BroadRegion',
                     null=True,
                     on_delete=models.CASCADE)),
                ('imp_broad_region_slave_dis',
                 models.ForeignKey(
                     related_name='imp_broad_region_slave_dis',
                     verbose_name='Imputed broad region of slave '
                                  'disembarkation (MJSELIMP1)',
                     blank=True,
                     to='voyage.BroadRegion',
                     null=True,
                     on_delete=models.CASCADE)),
                ('imp_broad_region_voyage_begin',
                 models.ForeignKey(
                     related_name='imp_broad_region_voyage_begin',
                     verbose_name='Imputed broad region where voyage began '
                                  '(DEPTREGIMP1)',
                     blank=True,
                     to='voyage.BroadRegion',
                     null=True,
                     on_delete=models.CASCADE)),
                ('imp_port_voyage_begin',
                 models.ForeignKey(
                     related_name='imp_port_voyage_begin',
                     verbose_name='Imputed port where voyage began '
                                  '(PTDEPIMP)',
                     blank=True,
                     to='voyage.Place',
                     null=True,
                     on_delete=models.CASCADE)),
                ('imp_principal_place_of_slave_purchase',
                 models.ForeignKey(
                     related_name='imp_principal_place_of_slave_purchase',
                     verbose_name='Imputed principal place of slave purchase '
                                  '(MJBYPTIMP)',
                     blank=True,
                     to='voyage.Place',
                     null=True,
                     on_delete=models.CASCADE)),
                ('imp_principal_port_slave_dis',
                 models.ForeignKey(
                     related_name='imp_principal_port_slave_dis',
                     verbose_name='Imputed principal port of slave '
                                  'disembarkation (MJSLPTIMP)',
                     blank=True,
                     to='voyage.Place',
                     null=True,
                     on_delete=models.CASCADE)),
                ('imp_principal_region_of_slave_purchase',
                 models.ForeignKey(
                     related_name='imp_principal_region_of_slave_purchase',
                     verbose_name='Imputed principal region of slave '
                                  'purchase (MAJBYIMP)',
                     blank=True,
                     to='voyage.Region',
                     null=True,
                     on_delete=models.CASCADE)),
                ('imp_principal_region_slave_dis',
                 models.ForeignKey(
                     related_name='imp_principal_region_slave_dis',
                     verbose_name='Imputed principal region of slave '
                                  'disembarkation (MJSELIMP)',
                     blank=True,
                     to='voyage.Region',
                     null=True,
                     on_delete=models.CASCADE)),
                ('imp_region_voyage_begin',
                 models.ForeignKey(
                     related_name='imp_region_voyage_begin',
                     verbose_name='Imputed region where voyage began '
                                  '(DEPTREGIMP)',
                     blank=True,
                     to='voyage.Region',
                     null=True,
                     on_delete=models.CASCADE)),
                ('int_first_port_dis',
                 models.ForeignKey(
                     related_name='int_first_port_dis',
                     verbose_name='First intended port of disembarkation '
                                  '(ARRPORT)',
                     blank=True,
                     to='voyage.Place',
                     null=True,
                     on_delete=models.CASCADE)),
                ('int_first_port_emb',
                 models.ForeignKey(
                     related_name='int_first_port_emb',
                     verbose_name='First intended port of embarkation '
                                  '(EMBPORT)',
                     blank=True,
                     to='voyage.Place',
                     null=True,
                     on_delete=models.CASCADE)),
                ('int_first_region_purchase_slaves',
                 models.ForeignKey(
                     related_name='int_first_region_purchase_slaves',
                     verbose_name='First intended region of purchase of '
                                  'slaves (EMBREG)',
                     blank=True,
                     to='voyage.Region',
                     null=True,
                     on_delete=models.CASCADE)),
                ('int_first_region_slave_landing',
                 models.ForeignKey(
                     related_name='int_first_region_slave_landing',
                     verbose_name='First intended region of slave landing '
                                  '(REGARR)',
                     blank=True,
                     to='voyage.Region',
                     null=True,
                     on_delete=models.CASCADE)),
                ('int_second_place_region_slave_landing',
                 models.ForeignKey(
                     related_name='int_second_region_slave_landing',
                     verbose_name='Second intended region of slave landing '
                                  '(REGARR2)',
                     blank=True,
                     to='voyage.Region',
                     null=True,
                     on_delete=models.CASCADE)),
                ('int_second_port_dis',
                 models.ForeignKey(
                     related_name='int_second_port_dis',
                     verbose_name='Second intended port of disembarkation '
                                  '(ARRPORT2)',
                     blank=True,
                     to='voyage.Place',
                     null=True,
                     on_delete=models.CASCADE)),
                ('int_second_port_emb',
                 models.ForeignKey(
                     related_name='int_second_port_emb',
                     verbose_name='Second intended port of embarkation '
                                  '(EMBPORT2)',
                     blank=True,
                     to='voyage.Place',
                     null=True,
                     on_delete=models.CASCADE)),
                ('int_second_region_purchase_slaves',
                 models.ForeignKey(
                     related_name='int_second_region_purchase_slaves',
                     verbose_name='Second intended region of purchase of '
                                  'slaves (EMBREG2)',
                     blank=True,
                     to='voyage.Region',
                     null=True,
                     on_delete=models.CASCADE)),
                ('place_voyage_ended',
                 models.ForeignKey(
                     related_name='place_voyage_ended',
                     verbose_name='Place at which voyage ended (PORTRET)',
                     blank=True,
                     to='voyage.Place',
                     null=True,
                     on_delete=models.CASCADE)),
                ('port_of_call_before_atl_crossing',
                 models.ForeignKey(
                     related_name='port_of_call_before_atl_crossing',
                     verbose_name='Port of call before Atlantic crossing '
                                  '(NPAFTTRA)',
                     blank=True,
                     to='voyage.Place',
                     null=True,
                     on_delete=models.CASCADE)),
                ('port_of_departure',
                 models.ForeignKey(related_name='port_of_departure',
                                   verbose_name='Port of departure (PORTDEP)',
                                   blank=True,
                                   to='voyage.Place',
                                   null=True,
                                   on_delete=models.CASCADE)),
                ('principal_place_of_slave_purchase',
                 models.ForeignKey(
                     related_name='principal_place_of_slave_purchase',
                     verbose_name='Principal place of slave purchase '
                                  '(MAJBUYPT)',
                     blank=True,
                     to='voyage.Place',
                     null=True,
                     on_delete=models.CASCADE)),
                ('principal_port_of_slave_dis',
                 models.ForeignKey(
                     related_name='principal_port_of_slave_dis',
                     verbose_name='Principal port of slave disembarkation '
                                  '(MAJSELPT)',
                     blank=True,
                     to='voyage.Place',
                     null=True,
                     on_delete=models.CASCADE)),
                ('region_of_return',
                 models.ForeignKey(related_name='region_of_return',
                                   verbose_name='Region of return (RETRNREG)',
                                   blank=True,
                                   to='voyage.Region',
                                   null=True,
                                   on_delete=models.CASCADE)),
                ('second_landing_place',
                 models.ForeignKey(
                     related_name='second_landing_place',
                     verbose_name='Second place of slave landing (ADPSALE1)',
                     blank=True,
                     to='voyage.Place',
                     null=True,
                     on_delete=models.CASCADE)),
                ('second_landing_region',
                 models.ForeignKey(
                     related_name='second_landing_region',
                     verbose_name='Second region of slave landing (REGDIS2)',
                     blank=True,
                     to='voyage.Region',
                     null=True,
                     on_delete=models.CASCADE)),
                ('second_place_slave_purchase',
                 models.ForeignKey(
                     related_name='second_place_slave_purchase',
                     verbose_name='Second place of slave purchase (PLAC2TRA)',
                     blank=True,
                     to='voyage.Place',
                     null=True,
                     on_delete=models.CASCADE)),
                ('second_region_slave_emb',
                 models.ForeignKey(
                     related_name='second_region_slave_emb',
                     verbose_name='Second region of embarkation of '
                                  'slaves (REGEM2)',
                     blank=True,
                     to='voyage.Region',
                     null=True,
                     on_delete=models.CASCADE)),
                ('third_landing_place',
                 models.ForeignKey(
                     related_name='third_landing_place',
                     verbose_name='Third place of slave landing (ADPSALE2)',
                     blank=True,
                     to='voyage.Place',
                     null=True,
                     on_delete=models.CASCADE)),
                ('third_landing_region',
                 models.ForeignKey(
                     related_name='third_landing_region',
                     verbose_name='Third region of slave landing (REGDIS3)',
                     blank=True,
                     to='voyage.Region',
                     null=True,
                     on_delete=models.CASCADE)),
                ('third_place_slave_purchase',
                 models.ForeignKey(
                     related_name='third_place_slave_purchase',
                     verbose_name='Third place of slave purchase (PLAC3TRA)',
                     blank=True,
                     to='voyage.Place',
                     null=True,
                     on_delete=models.CASCADE)),
                ('third_region_slave_emb',
                 models.ForeignKey(
                     related_name='third_region_slave_emb',
                     verbose_name='Third region of embarkation '
                                  'of slaves (REGEM3)',
                     blank=True,
                     to='voyage.Region',
                     null=True,
                     on_delete=models.CASCADE)),
                ('voyage',
                 models.ForeignKey(related_name='voyage_name_itinerary',
                                   blank=True,
                                   to='voyage.Voyage',
                                   null=True,
                                   on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Itinerary',
                'verbose_name_plural': 'Itineraries',
            },
        ),
        migrations.CreateModel(
            name='VoyageOutcome',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('outcome_owner',
                 models.ForeignKey(verbose_name='Owner Outcome',
                                   blank=True,
                                   to='voyage.OwnerOutcome',
                                   null=True,
                                   on_delete=models.CASCADE)),
                ('outcome_slaves',
                 models.ForeignKey(verbose_name='Slaves Outcome',
                                   blank=True,
                                   to='voyage.SlavesOutcome',
                                   null=True,
                                   on_delete=models.CASCADE)),
                ('particular_outcome',
                 models.ForeignKey(verbose_name='Particular Outcome',
                                   blank=True,
                                   to='voyage.ParticularOutcome',
                                   null=True,
                                   on_delete=models.CASCADE)),
                ('resistance',
                 models.ForeignKey(verbose_name='Resistance',
                                   blank=True,
                                   to='voyage.Resistance',
                                   null=True,
                                   on_delete=models.CASCADE)),
                ('vessel_captured_outcome',
                 models.ForeignKey(verbose_name='Vessel Captured Outcome',
                                   blank=True,
                                   to='voyage.VesselCapturedOutcome',
                                   null=True,
                                   on_delete=models.CASCADE)),
                ('voyage',
                 models.ForeignKey(related_name='voyage_name_outcome',
                                   blank=True,
                                   to='voyage.Voyage',
                                   null=True,
                                   on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Outcome',
                'verbose_name_plural': 'Outcomes',
            },
        ),
        migrations.CreateModel(
            name='VoyageShip',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('ship_name',
                 models.CharField(max_length=255,
                                  null=True,
                                  verbose_name='Name of vessel',
                                  blank=True)),
                ('tonnage',
                 models.IntegerField(null=True,
                                     verbose_name='Tonnage of vessel',
                                     blank=True)),
                ('guns_mounted',
                 models.IntegerField(null=True,
                                     verbose_name='Guns mounted',
                                     blank=True)),
                ('year_of_construction',
                 models.IntegerField(
                     null=True,
                     verbose_name="Year of vessel's construction",
                     blank=True)),
                ('registered_year',
                 models.IntegerField(
                     null=True,
                     verbose_name="Year of vessel's registration",
                     blank=True)),
                ('tonnage_mod',
                 models.DecimalField(
                     null=True,
                     verbose_name='Tonnage standardized on British '
                                  'measured tons, 1773-1870',
                     max_digits=8,
                     decimal_places=1,
                     blank=True)),
                ('imputed_nationality',
                 models.ForeignKey(related_name='imputed_nationality',
                                   blank=True,
                                   to='voyage.Nationality',
                                   null=True,
                                   on_delete=models.CASCADE)),
                ('nationality_ship',
                 models.ForeignKey(related_name='nationality_ship',
                                   blank=True,
                                   to='voyage.Nationality',
                                   null=True,
                                   on_delete=models.CASCADE)),
                ('registered_place',
                 models.ForeignKey(
                     related_name='registered_place',
                     verbose_name='Place where vessel registered',
                     blank=True,
                     to='voyage.Place',
                     null=True,
                     on_delete=models.CASCADE)),
                ('registered_region',
                 models.ForeignKey(
                     related_name='registered_region',
                     verbose_name='Region where vessel registered',
                     blank=True,
                     to='voyage.Region',
                     null=True,
                     on_delete=models.CASCADE)),
                ('rig_of_vessel',
                 models.ForeignKey(blank=True,
                                   to='voyage.RigOfVessel',
                                   null=True,
                                   on_delete=models.CASCADE)),
                ('ton_type',
                 models.ForeignKey(blank=True, to='voyage.TonType', null=True,
                                   on_delete=models.CASCADE)),
                ('vessel_construction_place',
                 models.ForeignKey(
                     related_name='vessel_construction_place',
                     verbose_name='Place where vessel constructed',
                     blank=True,
                     to='voyage.Place',
                     null=True,
                     on_delete=models.CASCADE)),
                ('vessel_construction_region',
                 models.ForeignKey(
                     related_name='vessel_construction_region',
                     verbose_name='Region where vessel constructed',
                     blank=True,
                     to='voyage.Region',
                     null=True,
                     on_delete=models.CASCADE)),
                ('voyage',
                 models.ForeignKey(related_name='voyage_name_ship',
                                   blank=True,
                                   to='voyage.Voyage',
                                   null=True,
                                   on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Ship',
                'verbose_name_plural': 'Ships',
            },
        ),
        migrations.CreateModel(
            name='VoyageShipOwner',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VoyageShipOwnerConnection',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('owner_order', models.IntegerField()),
                ('owner',
                 models.ForeignKey(related_name='owner_name',
                                   to='voyage.VoyageShipOwner',
                                   on_delete=models.CASCADE)),
                ('voyage',
                 models.ForeignKey(related_name='voyage_related',
                                   to='voyage.Voyage',
                                   on_delete=models.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='VoyageSlavesNumbers',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('slave_deaths_before_africa',
                 models.IntegerField(
                     null=True,
                     verbose_name='Slaves death before leaving '
                                  'Africa (SLADAFRI)',
                     blank=True)),
                ('slave_deaths_between_africa_america',
                 models.IntegerField(
                     null=True,
                     verbose_name='Slaves death before arrival and '
                                  'sale (SLADAMER)',
                     blank=True)),
                ('num_slaves_intended_first_port',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of slaves intended from first port '
                                  'of purchase (SLINTEND)',
                     blank=True)),
                ('num_slaves_intended_second_port',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of slaves intended from second '
                                  'port of purchase (SLINTEN2)',
                     blank=True)),
                ('num_slaves_carried_first_port',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of slaves carried from first port '
                                  'of purchase (NCAR13)',
                     blank=True)),
                ('num_slaves_carried_second_port',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of slaves carried from second port '
                                  'of purchase (NCAR15)',
                     blank=True)),
                ('num_slaves_carried_third_port',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of slaves carried from third port '
                                  'of purchase (NCAR17)',
                     blank=True)),
                ('total_num_slaves_purchased',
                 models.IntegerField(
                     null=True,
                     verbose_name='Total slaves purchased (TSLAVESP)',
                     blank=True)),
                ('total_num_slaves_dep_last_slaving_port',
                 models.IntegerField(
                     null=True,
                     verbose_name='Total slaves on board at departure from '
                                  'last slaving port (TSLAVESD)',
                     blank=True)),
                ('total_num_slaves_arr_first_port_embark',
                 models.IntegerField(
                     null=True,
                     verbose_name='Total slaves arrived at first port '
                                  'of disembarkation (SLAARRIV)',
                     blank=True)),
                ('num_slaves_disembark_first_place',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of slaves disembarked '
                                  'at first place (SLAS32)',
                     blank=True)),
                ('num_slaves_disembark_second_place',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of slaves disembarked '
                                  'at second place (SLAS36)',
                     blank=True)),
                ('num_slaves_disembark_third_place',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of slaves disembarked '
                                  'at third place (SLAS39)',
                     blank=True)),
                ('imp_total_num_slaves_embarked',
                 models.IntegerField(
                     null=True,
                     verbose_name='Total slaves embarked imputed * (slaximp)',
                     blank=True)),
                ('imp_total_num_slaves_disembarked',
                 models.IntegerField(
                     null=True,
                     verbose_name='Total slaves disembarked '
                                  'imputed * (SLAMIMP)',
                     blank=True)),
                ('imp_jamaican_cash_price',
                 models.DecimalField(
                     null=True,
                     verbose_name='Sterling cash price in Jamaica* (imputed)',
                     max_digits=10,
                     decimal_places=4,
                     blank=True)),
                ('imp_mortality_during_voyage',
                 models.IntegerField(
                     null=True,
                     verbose_name='Imputed number of slave deaths '
                                  'during Middle Passage (VYMRTIMP)',
                     blank=True)),
                ('num_men_embark_first_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of men (MEN1) embarked at first '
                                  'port of purchase',
                     blank=True)),
                ('num_women_embark_first_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of women (WOMEN1) embarked at '
                                  'first port of purchase',
                     blank=True)),
                ('num_boy_embark_first_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of boys (BOY1) embarked at first '
                                  'port of purchase',
                     blank=True)),
                ('num_girl_embark_first_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of girls (GIRL1) embarked at first '
                                  'port of purchase',
                     blank=True)),
                ('num_adult_embark_first_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of adults (gender unspecified) '
                                  '(ADULT1) embarked at first port '
                                  'of purchase',
                     blank=True)),
                ('num_child_embark_first_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of children (gender unspecified) '
                                  '(CHILD1) embarked at first port '
                                  'of purchase',
                     blank=True)),
                ('num_infant_embark_first_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of infants (INFANT1) embarked at '
                                  'first port of purchase',
                     blank=True)),
                ('num_males_embark_first_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of males (age unspecified) (MALE1) '
                                  'embarked at first port of purchase',
                     blank=True)),
                ('num_females_embark_first_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of females (age unspecified) '
                                  '(FEMALE1) embarked at first port '
                                  'of purchase',
                     blank=True)),
                ('num_men_died_middle_passage',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of men '
                                  '(MEN2) died on Middle Passage',
                     blank=True)),
                ('num_women_died_middle_passage',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of women (WOMEN2) '
                                  'died on Middle Passage',
                     blank=True)),
                ('num_boy_died_middle_passage',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of boys '
                                  '(BOY2) died on Middle Passage',
                     blank=True)),
                ('num_girl_died_middle_passage',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of girls '
                                  '(GIRL2) died on Middle Passage',
                     blank=True)),
                ('num_adult_died_middle_passage',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of adults (gender unspecified) '
                                  '(ADULT2) died on Middle Passage',
                     blank=True)),
                ('num_child_died_middle_passage',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of children (gender unspecified) '
                                  '(CHILD2) died on Middle Passage',
                     blank=True)),
                ('num_infant_died_middle_passage',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of infants '
                                  '(INFANT2) died on Middle Passage',
                     blank=True)),
                ('num_males_died_middle_passage',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of males (age unspecified) '
                                  '(MALE2) died on Middle Passage',
                     blank=True)),
                ('num_females_died_middle_passage',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of females (age unspecified) '
                                  '(FEMALE2) died on Middle Passage',
                     blank=True)),
                ('num_men_disembark_first_landing',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of men (MEN3) disembarked at '
                                  'first place of landing',
                     blank=True)),
                ('num_women_disembark_first_landing',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of women (WOMEN3) disembarked at '
                                  'first place of landing',
                     blank=True)),
                ('num_boy_disembark_first_landing',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of boys (BOY3) disembarked at '
                                  'first place of landing',
                     blank=True)),
                ('num_girl_disembark_first_landing',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of girls (GIRL3) disembarked at '
                                  'first place of landing',
                     blank=True)),
                ('num_adult_disembark_first_landing',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of adults (gender unspecified) '
                                  '(ADULT3) disembarked at first place '
                                  'of landing',
                     blank=True)),
                ('num_child_disembark_first_landing',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of children (gender unspecified) '
                                  '(CHILD3) disembarked at first place '
                                  'of landing',
                     blank=True)),
                ('num_infant_disembark_first_landing',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of infants (INFANT3) disembarked '
                                  'at first place of landing',
                     blank=True)),
                ('num_males_disembark_first_landing',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of males (age unspecified) (MALE3) '
                                  'disembarked at first place of landing',
                     blank=True)),
                ('num_females_disembark_first_landing',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of females (age unspecified) '
                                  '(FEMALE3) disembarked at first place '
                                  'of landing',
                     blank=True)),
                ('num_men_embark_second_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of men (MEN4) embarked at second '
                                  'port of purchase',
                     blank=True)),
                ('num_women_embark_second_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of women (WOMEN4) embarked at '
                                  'second port of purchase',
                     blank=True)),
                ('num_boy_embark_second_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of boys (BOY4) embarked at second '
                                  'port of purchase',
                     blank=True)),
                ('num_girl_embark_second_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of girls (GIRL4) embarked at '
                                  'second port of purchase',
                     blank=True)),
                ('num_adult_embark_second_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of adults (gender unspecified) '
                                  '(ADULT4) embarked at second port '
                                  'of purchase',
                     blank=True)),
                ('num_child_embark_second_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of children (gender unspecified) '
                                  '(CHILD4) embarked at second port '
                                  'of purchase',
                     blank=True)),
                ('num_infant_embark_second_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of infants (INFANT4) embarked at '
                                  'second port of purchase',
                     blank=True)),
                ('num_males_embark_second_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of males (age unspecified) (MALE4) '
                                  'embarked at second port of purchase',
                     blank=True)),
                ('num_females_embark_second_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of females (age unspecified) '
                                  '(FEMALE4) embarked at second port '
                                  'of purchase',
                     blank=True)),
                ('num_men_embark_third_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of men (MEN5) embarked at third '
                                  'port of purchase',
                     blank=True)),
                ('num_women_embark_third_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of women (WOMEN5) embarked at '
                                  'third port of purchase',
                     blank=True)),
                ('num_boy_embark_third_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of boys (BOY5) embarked at third '
                                  'port of purchase',
                     blank=True)),
                ('num_girl_embark_third_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of girls (GIRL5) embarked at third '
                                  'port of purchase',
                     blank=True)),
                ('num_adult_embark_third_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of adults (gender unspecified) '
                                  '(ADULT5) embarked at third port '
                                  'of purchase',
                     blank=True)),
                ('num_child_embark_third_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of children (gender unspecified) '
                                  '(CHILD5) embarked at third port '
                                  'of purchase',
                     blank=True)),
                ('num_infant_embark_third_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of infants (INFANT5) embarked at '
                                  'third port of purchase',
                     blank=True)),
                ('num_males_embark_third_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of males (age unspecified) (MALE5) '
                                  'embarked at third port of purchase',
                     blank=True)),
                ('num_females_embark_third_port_purchase',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of females (age unspecified) '
                                  '(FEMALE5) embarked at third port '
                                  'of purchase',
                     blank=True)),
                ('num_men_disembark_second_landing',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of men (MEN6) disembarked at '
                                  'second place of landing',
                     blank=True)),
                ('num_women_disembark_second_landing',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of women (WOMEN6) disembarked at '
                                  'second place of landing',
                     blank=True)),
                ('num_boy_disembark_second_landing',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of boys (BOY6) disembarked at '
                                  'second place of landing',
                     blank=True)),
                ('num_girl_disembark_second_landing',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of girls (GIRL6) disembarked at '
                                  'second place of landing',
                     blank=True)),
                ('num_adult_disembark_second_landing',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of adults (gender unspecified) '
                                  '(ADULT6) disembarked at second place '
                                  'of landing',
                     blank=True)),
                ('num_child_disembark_second_landing',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of children (gender unspecified) '
                                  '(CHILD6) disembarked at second place '
                                  'of landing',
                     blank=True)),
                ('num_infant_disembark_second_landing',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of infants (INFANT6) disembarked '
                                  'at second place of landing',
                     blank=True)),
                ('num_males_disembark_second_landing',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of males (age unspecified) '
                                  '(MALE6) disembarked at second place '
                                  'of landing',
                     blank=True)),
                ('num_females_disembark_second_landing',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of females (age unspecified) '
                                  '(FEMALE6) disembarked at second place '
                                  'of landing',
                     blank=True)),
                ('imp_num_adult_embarked',
                 models.IntegerField(
                     null=True,
                     verbose_name='Imputed number of adults embarked '
                                  '(ADLT1IMP)',
                     blank=True)),
                ('imp_num_children_embarked',
                 models.IntegerField(
                     null=True,
                     verbose_name='Imputed number of adults embarked '
                                  '(CHIL1IMP)',
                     blank=True)),
                ('imp_num_male_embarked',
                 models.IntegerField(
                     null=True,
                     verbose_name='Imputed number of males embarked '
                                  '(MALE1IMP)',
                     blank=True)),
                ('imp_num_female_embarked',
                 models.IntegerField(
                     null=True,
                     verbose_name='Imputed number of females embarked '
                                  '(FEML1IMP)',
                     blank=True)),
                ('total_slaves_embarked_age_identified',
                 models.IntegerField(
                     null=True,
                     verbose_name='Total slaves embarked with age identified '
                                  '(SLAVEMA1)',
                     blank=True)),
                ('total_slaves_embarked_gender_identified',
                 models.IntegerField(
                     null=True,
                     verbose_name='Total slaves embarked with gender '
                                  'identified (SLAVEMX1)',
                     blank=True)),
                ('imp_adult_death_middle_passage',
                 models.IntegerField(
                     null=True,
                     verbose_name='Imputed number of adults who died on '
                                  'Middle Passage (ADLT2IMP)',
                     blank=True)),
                ('imp_child_death_middle_passage',
                 models.IntegerField(
                     null=True,
                     verbose_name='Imputed number of children who died on '
                                  'Middle Passage (CHIL2IMP)',
                     blank=True)),
                ('imp_male_death_middle_passage',
                 models.IntegerField(
                     null=True,
                     verbose_name='Imputed number of males who died on '
                                  'Middle Passage (MALE2IMP)',
                     blank=True)),
                ('imp_female_death_middle_passage',
                 models.IntegerField(
                     null=True,
                     verbose_name='Imputed number of females who died on '
                                  'Middle Passage (FEML2IMP)',
                     blank=True)),
                ('imp_num_adult_landed',
                 models.IntegerField(
                     null=True,
                     verbose_name='Imputed number of adults landed '
                                  '(ADLT3IMP)',
                     blank=True)),
                ('imp_num_child_landed',
                 models.IntegerField(
                     null=True,
                     verbose_name='Imputed number of children landed '
                                  '(CHIL3IMP)',
                     blank=True)),
                ('imp_num_male_landed',
                 models.IntegerField(
                     null=True,
                     verbose_name='Imputed number of males landed (MALE3IMP)',
                     blank=True)),
                ('imp_num_female_landed',
                 models.IntegerField(
                     null=True,
                     verbose_name='Imputed number of females landed '
                                  '(FEML3IMP)',
                     blank=True)),
                ('total_slaves_landed_age_identified',
                 models.IntegerField(
                     null=True,
                     verbose_name='Total slaves identified by age among '
                                  'landed slaves (SLAVEMA3)',
                     blank=True)),
                ('total_slaves_landed_gender_identified',
                 models.IntegerField(
                     null=True,
                     verbose_name='Total slaves identified by gender among '
                                  'landed slaves (SLAVEMX3)',
                     blank=True)),
                ('total_slaves_dept_or_arr_age_identified',
                 models.IntegerField(
                     null=True,
                     verbose_name='Total slaves identified by age at '
                                  'departure or arrival (SLAVEMA7)',
                     blank=True)),
                ('total_slaves_dept_or_arr_gender_identified',
                 models.IntegerField(
                     null=True,
                     verbose_name='Total slaves identified by gender at '
                                  'departure or arrival(SLAVEMX7)',
                     blank=True)),
                ('imp_slaves_embarked_for_mortality',
                 models.IntegerField(
                     null=True,
                     verbose_name='Imputed number of slaves embarked for '
                                  'mortality calculation (TSLMTIMP)',
                     blank=True)),
                ('imp_num_men_total',
                 models.IntegerField(null=True,
                                     verbose_name='Number of men (MEN7)',
                                     blank=True)),
                ('imp_num_women_total',
                 models.IntegerField(null=True,
                                     verbose_name='Number of women (WOMEN7) ',
                                     blank=True)),
                ('imp_num_boy_total',
                 models.IntegerField(null=True,
                                     verbose_name='Number of boys (BOY7)',
                                     blank=True)),
                ('imp_num_girl_total',
                 models.IntegerField(null=True,
                                     verbose_name='Number of girls (GIRL7)',
                                     blank=True)),
                ('imp_num_adult_total',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of adults (gender unspecified) '
                                  '(ADULT7)',
                     blank=True)),
                ('imp_num_child_total',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of children (gender unspecified) '
                                  '(CHILD7)',
                     blank=True)),
                ('imp_num_males_total',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of males (age unspecified) (MALE7)',
                     blank=True)),
                ('imp_num_females_total',
                 models.IntegerField(
                     null=True,
                     verbose_name='Number of females (age unspecified) '
                                  '(FEMALE7) ',
                     blank=True)),
                ('percentage_men',
                 models.FloatField(null=True,
                                   verbose_name='Percentage men on voyage',
                                   blank=True)),
                ('percentage_women',
                 models.FloatField(null=True,
                                   verbose_name='Percentage women on voyage',
                                   blank=True)),
                ('percentage_boy',
                 models.FloatField(null=True,
                                   verbose_name='Percentage boy on voyage',
                                   blank=True)),
                ('percentage_girl',
                 models.FloatField(null=True,
                                   verbose_name='Percentage girl on voyage',
                                   blank=True)),
                ('percentage_male',
                 models.FloatField(null=True,
                                   verbose_name='Percentage male on voyage',
                                   blank=True)),
                ('percentage_child',
                 models.FloatField(
                     null=True,
                     verbose_name='Percentage children on voyage',
                     blank=True)),
                ('percentage_adult',
                 models.FloatField(null=True,
                                   verbose_name='Percentage adult on voyage',
                                   blank=True)),
                ('percentage_female',
                 models.FloatField(null=True,
                                   verbose_name='Percentage female on voyage',
                                   blank=True)),
                ('imp_mortality_ratio',
                 models.FloatField(null=True,
                                   verbose_name='Imputed mortality ratio',
                                   blank=True)),
                ('voyage',
                 models.ForeignKey(
                     related_name='voyage_name_slave_characteristics',
                     to='voyage.Voyage',
                     on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Slaves Characteristic',
                'verbose_name_plural': 'Slaves Characteristics',
            },
        ),
        migrations.CreateModel(
            name='VoyageSources',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('short_ref',
                 models.CharField(max_length=255,
                                  null=True,
                                  verbose_name='Short reference',
                                  blank=True)),
                ('full_ref',
                 models.CharField(max_length=2550,
                                  null=True,
                                  verbose_name='Full reference',
                                  blank=True)),
            ],
            options={
                'ordering': ['short_ref', 'full_ref'],
                'verbose_name': 'Source',
                'verbose_name_plural': 'Sources',
            },
        ),
        migrations.CreateModel(
            name='VoyageSourcesConnection',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('source_order', models.IntegerField()),
                ('text_ref',
                 models.CharField(max_length=255,
                                  null=True,
                                  verbose_name='Text reference(citation)',
                                  blank=True)),
                ('group',
                 models.ForeignKey(related_name='group', to='voyage.Voyage',
                                   on_delete=models.CASCADE)),
                ('source',
                 models.ForeignKey(related_name='source',
                                   blank=True,
                                   to='voyage.VoyageSources',
                                   null=True,
                                   on_delete=models.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='VoyageSourcesType',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('group_id', models.IntegerField()),
                ('group_name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['group_id'],
                'verbose_name': 'Sources type',
                'verbose_name_plural': 'Sources types',
            },
        ),
        migrations.AddField(
            model_name='voyagesources',
            name='source_type',
            field=models.ForeignKey(to='voyage.VoyageSourcesType', null=True,
                                    on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='voyage',
            name='voyage_captain',
            field=models.ManyToManyField(
                help_text='Voyage Captain',
                to='voyage.VoyageCaptain',
                through='voyage.VoyageCaptainConnection',
                blank=True),
        ),
        migrations.AddField(
            model_name='voyage',
            name='voyage_crew',
            field=models.ForeignKey(related_name='voyage_crew',
                                    blank=True,
                                    to='voyage.VoyageCrew',
                                    null=True,
                                    on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='voyage',
            name='voyage_dates',
            field=models.ForeignKey(related_name='voyage_dates',
                                    blank=True,
                                    to='voyage.VoyageDates',
                                    null=True,
                                    on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='voyage',
            name='voyage_groupings',
            field=models.ForeignKey(blank=True,
                                    to='voyage.VoyageGroupings',
                                    null=True,
                                    on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='voyage',
            name='voyage_itinerary',
            field=models.ForeignKey(related_name='voyage_itinerary',
                                    blank=True,
                                    to='voyage.VoyageItinerary',
                                    null=True,
                                    on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='voyage',
            name='voyage_ship',
            field=models.ForeignKey(related_name='voyage_ship',
                                    blank=True,
                                    to='voyage.VoyageShip',
                                    null=True,
                                    on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='voyage',
            name='voyage_ship_owner',
            field=models.ManyToManyField(
                help_text='Voyage Ship Owner',
                to='voyage.VoyageShipOwner',
                through='voyage.VoyageShipOwnerConnection',
                blank=True),
        ),
        migrations.AddField(
            model_name='voyage',
            name='voyage_slaves_numbers',
            field=models.ForeignKey(related_name='voyage_slaves_numbers',
                                    blank=True,
                                    to='voyage.VoyageSlavesNumbers',
                                    null=True,
                                    on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='voyage',
            name='voyage_sources',
            field=models.ManyToManyField(
                related_name='voyage_sources',
                through='voyage.VoyageSourcesConnection',
                to='voyage.VoyageSources',
                blank=True),
        ),
        migrations.AddField(
            model_name='place',
            name='region',
            field=models.ForeignKey(to='voyage.Region',
                                    on_delete=models.CASCADE),
        ),
    ]
