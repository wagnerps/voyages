var fieldMap = {
  "Flag*": "var_imputed_nationality_idnum",
  "Broad region where voyage began": "var_imp_broad_region_voyage_begin_idnum",
  "Region where voyage began": "var_imp_region_voyage_begin_idnum",
  "Port where voyage began*": "var_imp_port_voyage_begin_idnum",
  "Embarkation regions": "var_imp_principal_region_of_slave_purchase_idnum",
  "Embarkation Ports": "var_imp_principal_place_of_slave_purchase_idnum",
  "Specific regions of disembarkation": "var_imp_principal_region_slave_dis_idnum",
  "Broad regions of disembarkation": "var_imp_principal_broad_region_disembark_idnum",
  "Disembarkation Ports": "var_imp_principal_port_slave_dis_idnum",
  'Principal place of purchase*': 'var_imp_principal_place_of_slave_purchase_idnum',
  'Principal place of landing*': 'var_imp_principal_port_slave_dis_idnum',
  "Individual Years": "var_imp_arrival_at_port_of_dis",
  "5-year periods": "var_imp_arrival_at_port_of_dis",
  "10-year periods": "var_imp_arrival_at_port_of_dis",
  "25-year periods": "var_imp_arrival_at_port_of_dis",
  "50-year periods": "var_imp_arrival_at_port_of_dis",
  "100-year periods": "var_imp_arrival_at_port_of_dis",
};

function makeYearRange(interval) {
  return { start: 1501, gap: interval, end: 2000 };
}

var otherGraphsXAxes = [
  { id: 0, varName: 'var_imputed_nationality', label: gettext('Flag*') },
  { id: 1, varName: 'var_rig_of_vessel', label: gettext('Rig') },
  { id: 2, varName: 'var_outcome_voyage', label: gettext('Particular outcome of the voyage') },
  { id: 3, varName: 'var_outcome_slaves', label: gettext('Outcome for slaves') },
  { id: 4, varName: 'var_outcome_owner', label: gettext('Outcome for owner') },
  { id: 5, varName: 'var_outcome_ship_captured', label: gettext('Outcome if ship captured') },
  { id: 6, varName: 'var_resistance', label: gettext('African resistance') },
  { id: 7, varName: 'var_imp_port_voyage_begin', label: gettext('Place where voyage began*') },
  { id: 8, varName: 'var_imp_region_voyage_begin', label: gettext('Region where voyage began') },
  { id: 9, varName: 'var_imp_principal_place_of_slave_purchase', label: gettext('Principal place of slave purchase*') },
  { id: 10, varName: 'var_imp_principal_region_of_slave_purchase', label: gettext('Principal region of slave purchase') },
  { id: 11, varName: 'var_imp_principal_port_slave_dis', label: gettext('Principal place of slave landing*') },
  { id: 12, varName: 'var_imp_principal_region_slave_dis', label: gettext('Principal region of slave landing') },
  { id: 13, varName: 'var_imp_principal_broad_region_disembark', label: gettext('Broad region of slave landing') },
  { id: 14, varName: 'var_place_voyage_ended', label: gettext('Place where voyage ended') },
  { id: 15, varName: 'var_region_voyage_ended', label: gettext('Region where voyage ended') },
  { id: 16, varName: 'var_voyage_began', label: gettext('Month voyage began') },
  { id: 17, varName: 'var_slave_purchase_began', label: gettext('Month trade began in Africa') },
  { id: 18, varName: 'var_date_departed_africa', label: gettext('Month vessel departed Africa') },
  { id: 19, varName: 'var_first_dis_of_slaves', label: gettext('Month vessel arrived with slaves') },
  { id: 20, varName: 'var_departure_last_place_of_landing', label: gettext('Month vessel departed for home port') },
  { id: 21, varName: 'var_voyage_completed', label: gettext('Month voyage completed') },
  { id: 22, varName: 'var_imp_arrival_at_port_of_dis_mod_5', label: gettext('Year arrived with slaves (5 year periods)') },
  { id: 23, varName: 'var_imp_arrival_at_port_of_dis_mod_10', label: gettext('Year arrived with slaves (10 year periods)') },
  { id: 24, varName: 'var_imp_arrival_at_port_of_dis_mod_25', label: gettext('Year arrived with slaves (25 year periods)') },
];

var graphsYAxes = [ // WORKAROUND; var_name_MODE; maps to voyage/graphs.py; 4 modes: avg, count, sum, freq
  { id:0, varName: 'var_voyage_id_count', label: gettext('Number of voyages') },
  { id:1, varName: 'var_imp_length_home_to_disembark_avg', label: gettext('Average voyage length, home port to slaves landing (days)') },
  { id:2, varName: 'var_length_middle_passage_days_avg', label: gettext('Average middle passage (days)') },
  { id:3, varName: 'var_tonnage_mod_avg', label: gettext('Standardized tonnage*') },
  { id:4, varName: 'var_crew_voyage_outset_avg', label: gettext('Average crew at voyage outset') },
  { id:5, varName: 'var_crew_first_landing_avg', label: gettext('Average crew at first landing of slaves') },
  { id:6, varName: 'var_crew_voyage_outset_sum', label: gettext('Total crew at voyage outset') },
  { id:7, varName: 'var_crew_first_landing_sum', label: gettext('Total crew at first landing of slaves') },
  { id:8, varName: 'var_imp_total_num_slaves_purchased_avg', label: gettext('Average number of slaves embarked') },
  { id:9, varName: 'var_imp_total_slaves_disembarked_avg', label: gettext('Average number of slaves disembarked') },
  { id:10, varName: 'var_imp_total_num_slaves_purchased_sum', label: gettext('Total number of slaves embarked*') },
  { id:11, varName: 'var_imp_total_slaves_disembarked_sum', label: gettext('Total number of slaves disembarked*') },
  { id:12, varName: 'var_imputed_percentage_men_avg', label: gettext('Percent men') },
  { id:13, varName: 'var_imputed_percentage_women_avg', label: gettext('Percent women') },
  { id:14, varName: 'var_imputed_percentage_boys_avg', label: gettext('Percent boys') },
  { id:15, varName: 'var_imputed_percentage_girls_avg', label: gettext('Percent girls') },
  { id:16, varName: 'var_imputed_percentage_child_avg', label: gettext('Percent children') },
  { id:17, varName: 'var_imputed_percentage_male_avg', label: gettext('Percent male') },
  { id:18, varName: 'var_imputed_sterling_cash_avg', label: gettext('Sterling cash price in Jamaica') },
  { id:19, varName: 'var_resistance_freq', label: gettext('Rate of resistance') },
  { id:20, varName: 'var_imputed_mortality_avg', label: gettext('Percent of slaves embarked who died during voyage') },
];

var tabs = {
  // Tables Tab
  tables: {
    row: {
      // currently selected value
      variable: "tabs.tables.row",
      value: 12,
      options: [{ id: 0, varName: "var_imputed_nationality_idnum", label: gettext("Flag*")},
        {id: 1, varName: "var_imp_broad_region_voyage_begin_idnum", label: gettext("Broad region where voyage began")},
        { id: 2, varName: "var_imp_region_voyage_begin_idnum", label: gettext("Region where voyage began")},
        { id: 3, varName: "var_imp_port_voyage_begin_idnum", label: gettext("Port where voyage began*")},
        { id: 4, varName: "var_imp_principal_region_of_slave_purchase_idnum", label: gettext("Embarkation regions")},
        { id: 5, varName: "var_imp_principal_place_of_slave_purchase_idnum", label: gettext("Principal place of purchase*")},
        { id: 6, varName: "var_imp_principal_region_slave_dis_idnum", label: gettext("Specific regions of disembarkation")},
        { id: 7, varName: "var_imp_principal_broad_region_disembark_idnum", label: gettext("Broad regions of disembarkation")},
        { id: 8, varName: "var_imp_principal_port_slave_dis_idnum", label: gettext("Principal place of landing*")},
        { id: 9, varName: "var_imp_arrival_at_port_of_dis", label: gettext("Individual years*")},
        { id: 10, varName: "var_imp_arrival_at_port_of_dis", label: gettext("5-year periods"), range: makeYearRange(5)},
        { id: 11, varName: "var_imp_arrival_at_port_of_dis", label: gettext("10-year periods"), range: makeYearRange(10)},
        { id: 12, varName: "var_imp_arrival_at_port_of_dis", label: gettext("25-year periods"), range: makeYearRange(25)},
        { id: 13, varName: "var_imp_arrival_at_port_of_dis", label: gettext("50-year periods"), range: makeYearRange(50)},
        { id: 14, varName: "var_imp_arrival_at_port_of_dis", label: gettext("100-year periods"), range: makeYearRange(100)}],
    },
    column: {
      // currently selected value
      variable: "tabs.tables.column",
      value: 7,
      options: [{ id: 0, varName: "var_imputed_nationality_idnum", label: gettext("Flag*")},
        { id: 1, varName: "var_imp_broad_region_voyage_begin_idnum", label: gettext("Broad region where voyage began")},
        { id: 2, varName: "var_imp_region_voyage_begin_idnum", label: gettext("Region where voyage began")},
        { id: 3, varName: "var_imp_port_voyage_begin_idnum", label: gettext("Port where voyage began*")},
        { id: 4, varName: "var_imp_principal_region_of_slave_purchase_idnum", label: gettext("Embarkation regions")},
        { id: 5, varName: "var_imp_principal_place_of_slave_purchase_idnum", label: gettext("Principal place of purchase*")},
        { id: 6, varName: "var_imp_principal_region_slave_dis_idnum", label: gettext("Specific regions of disembarkation")},
        { id: 7, varName: "var_imp_principal_broad_region_disembark_idnum", label: gettext("Broad regions of disembarkation")},
        { id: 8, varName: "var_imp_principal_port_slave_dis_idnum", label: gettext("Principal place of landing*")}],
    },
    cell: {
      // currently selected value
      variable: "tabs.tables.cell",
      value: 1,
      options: [{id: 0, label: gettext("Number of voyages"), functions: {"cell": "unique(var_voyage_id)"}},
      {id: 1, label: gettext("Sum of embarked slaves*"), functions: {"cell": "sum(var_imp_total_num_slaves_purchased)"}},
      {id: 2, label: gettext("Average number of embarked slaves"), avg: true, functions: {"cell": "avg(var_imp_total_num_slaves_purchased)"}},
      {id: 3, label: gettext("Number of voyages - embarked slaves"), functions: {"cell": "unique(var_voyage_id)", "_filter": "var_imp_total_num_slaves_purchased:[* TO *]"}},
      {id: 4, label: gettext("Percent of embarked slaves (row total)"), processing: 'perc_row_total', functions: {"cell": "sum(var_imp_total_num_slaves_purchased)"}},
      {id: 5, label: gettext("Percent of embarked slaves (column total)"), processing: 'perc_col_total', functions: {"cell": "sum(var_imp_total_num_slaves_purchased)"}},
      {id: 6, label: gettext("Sum of disembarked slaves*"), functions: {"cell": "sum(var_imp_total_slaves_disembarked)"}},
      {id: 7, label: gettext("Average number of disembarked slaves"), avg: true, functions: {"cell": "avg(var_imp_total_slaves_disembarked)"}},
      {id: 8, label: gettext("Number of voyages - disembarked slaves"), functions: {"cell": "unique(var_voyage_id)", "_filter": "var_imp_total_slaves_disembarked:[* TO *]"}},
      {id: 9, label: gettext("Percent of disembarked slaves (row total)"), processing: 'perc_row_total', functions: {"cell": "sum(var_imp_total_slaves_disembarked)"}},
      {id: 10, label: gettext("Percent of disembarked slaves (column total)"), processing: 'perc_col_total', functions: {"cell": "sum(var_imp_total_slaves_disembarked)"}},
      {id: 11, label: gettext("Sum of embarked/disembarked slaves*"), functions: {"Embarked": "sum(var_imp_total_num_slaves_purchased)", "Disembarked": "sum(var_imp_total_slaves_disembarked)"}},
      {id: 12, label: gettext("Average number of embarked/disembarked slaves"), avg: true, functions: {"Embarked": "avg(var_imp_total_num_slaves_purchased)", "Disembarked": "avg(var_imp_total_slaves_disembarked)"}},
      {id: 13, label: gettext("Number of voyages - embarked/disembarked slaves"), functions: {"cell": "unique(var_voyage_id)", "_filter": "var_imp_total_num_slaves_purchased:[* TO *] AND var_imp_total_slaves_disembarked:[* TO *]"}},
      {id: 14, label: gettext("Average percentage male"), avg: true, format: 'percent', functions: {"cell": "avg(var_imputed_percentage_male)"}},
      {id: 15, label: gettext("Number of voyages - percentage male"), functions: {"cell": "unique(var_voyage_id)", "_filter": "var_imputed_percentage_male:[* TO *]"}},
      {id: 16, label: gettext("Average percentage children"), avg: true, format: 'percent', functions: {"cell": "avg(var_imputed_percentage_child)"}},
      {id: 17, label: gettext("Number of voyages - percentage children"), functions: {"cell": "unique(var_voyage_id)", "_filter": "var_imputed_percentage_child:[* TO *]"}},
      {id: 18, label: gettext("Average percentage of slaves embarked who died during voyage"), avg: true, format: 'percent', functions: {"cell": "avg(var_imputed_mortality)"}},
      {id: 19, label: gettext("Number of voyages - percentage of slaves embarked who died during voyage"), functions: {"cell": "unique(var_voyage_id)", "_filter": "var_imputed_mortality:[* TO *]"}},
      {id: 20, label: gettext("Average middle passage (days)"), avg: true, functions: {"cell": "avg(var_length_middle_passage_days)"}},
      {id: 21, label: gettext("Number of voyages - middle passage (days)"), functions: {"cell": "unique(var_voyage_id)", "_filter": "var_length_middle_passage_days:[* TO *]"}},
      {id: 22, label: gettext("Average standarized tonnage*"), avg: true, functions: {"cell": "avg(var_tonnage_mod)"}},
      {id: 23, label: gettext("Number of voyages - standarized tonnage"), functions: {"cell": "unique(var_voyage_id)", "_filter": "var_tonnage_mod:[* TO *]"}},
      {id: 24, label: gettext("Sterling cash price in Jamaica"), avg: true, functions: {"cell": "avg(var_imputed_sterling_cash)"}},
      {id: 25, label: gettext("Number of voyages - sterling cash price in Jamaica"), functions: {"cell": "unique(var_voyage_id)", "_filter": "var_imputed_sterling_cash:[* TO *]"}},],
    },
    options: {
      omitEmpty: false,
    }
  },

  // Data Visualization Tab
  visualization: {
    scatter: {
      x: {
        // currently selected value
        variable: "tabs.visualization.scatter.x",
        value: [0],
        options: [{ id: 0, varName: 'var_imp_arrival_at_port_of_dis', label: gettext('Year arrived with slaves*') },
        { id: 1, varName: 'var_imp_length_home_to_disembark', label: gettext('Voyage length, home port to slaves landing (days)') },
        { id: 2, varName: 'var_length_middle_passage_days', label: gettext('Middle passage (days)') },
        { id: 3, varName: 'var_crew_voyage_outset', label: gettext('Crew at voyage outset') },
        { id: 4, varName: 'var_crew_first_landing', label: gettext('Crew at first landing of slaves') },
        { id: 5, varName: 'var_imp_total_num_slaves_purchased', label: gettext('Slaves embarked*') },
        { id: 6, varName: 'var_imp_total_slaves_disembarked', label: gettext('Slaves disembarked*') }],
      },
      y: {
        // currently selected value
        variable: "tabs.visualization.scatter.y",
        value: [10],
        options: graphsYAxes,
      },
    },
    bar: {
      x: {
        // currently selected value
        variable: "tabs.visualization.bar.x",
        value: [0],
        options: otherGraphsXAxes,
      },
      y: {
        // currently selected value
        variable: "tabs.visualization.bar.y",
        value: [10],
        options: graphsYAxes,
      },
    },
    donut: {
      sectors: {
        // currently selected value
        variable: "tabs.visualization.donut.sectors",
        value: [0],
        options: otherGraphsXAxes,
      },
      values: {
        // currently selected value
        variable: "tabs.visualization.donut.values",
        value: 10,
        options: graphsYAxes,
      },
    },
  },

  // Timeline Tab
  timeline: {
    chart: {
      // currently selected value
      variable: "tabs.timeline.chart",
      value: 9,
      options: [ // this is a workaround to be having unique keys submitted to the backend: ##var_name; maps to globals.py > voyage_timeline_variables
        { id: 0, varName: "0var_imp_arrival_at_port_of_dis", label: gettext("Number of voyages") },
        { id: 1, varName: "2var_tonnage_mod", label: gettext("Average tonnage (standardized)*") },
        { id: 2, varName: "3var_guns_mounted", label: gettext("Average number of guns") },
        { id: 3, varName: "4var_resistance_idnum", label: gettext("Rate of resistance") },
        { id: 4, varName: "5var_imp_length_home_to_disembark", label: gettext("Average duration of voyage from home port to disembarkation (days)") },
        { id: 5, varName: "6var_length_middle_passage_days", label: gettext("Average duration of middle passage (days)") },
        { id: 6, varName: "7var_crew_voyage_outset", label: gettext("Average crew at outset") },
        { id: 7, varName: "8var_crew_first_landing", label: gettext("Average crew at first landing of slaves") },
        { id: 8, varName: "9var_crew_died_complete_voyage", label: gettext("Average crew deaths") },
        { id: 9, varName: "13var_imp_total_num_slaves_purchased", label: gettext("Total number of slaves embarked*") },
        { id: 10, varName: "14var_imp_total_num_slaves_purchased", label: gettext("Average number of slaves embarked") },
        { id: 11, varName: "15var_imp_total_slaves_disembarked", label: gettext("Total number of slaves disembarked*") },
        { id: 12, varName: "16var_imp_total_slaves_disembarked", label: gettext("Average number of slaves disembarked") },
        { id: 13, varName: "17var_imputed_percentage_men", label: gettext("Percentage men (among slaves)") },
        { id: 14, varName: "18var_imputed_percentage_women", label: gettext("Percentage women (among slaves)") },
        { id: 15, varName: "19var_imputed_percentage_boys", label: gettext("Percentage boys (among slaves)") },
        { id: 16, varName: "20var_imputed_percentage_girls", label: gettext("Percentage girls (among slaves)") },
        { id: 17, varName: "21var_imputed_percentage_female", label: gettext("Percentage female (among slaves)") },
        { id: 18, varName: "22var_imputed_percentage_male", label: gettext("Percentage male (among slaves)") },
        { id: 19, varName: "23var_imputed_sterling_cash", label: gettext("Sterling cash price in Jamaica") },
        { id: 20, varName: "26var_imputed_mortality", label: gettext("Average percentage of slaves embarked who died during the voyage") }
      ],
    },
  },
}
