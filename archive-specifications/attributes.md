# Global attributes

## Required global attributes

* `Conventions` () - Climate and Forecast (CF) convention version (always 1.10 ???)
* `activity_id` (CV) - activity  identifier ( RCM, ESD and FPS ??? )
* `contact` (free text) - contact information of the institution that is responsible for CORDEX simulations (avoid personal contact information) 
* `creation_date` (build rules) - date when file was created in format  YYYY-MM-DDTHH:MM:SSZ  (e.g., “2023-01-15T14:30:23Z”)
* `domain` (CV) - name of the CORDEX region (link)
* `domain_id` (CV) - an identifier assigned to each CORDEX region including a flag for resolution (link)
* `driving_experiment` (CV) - short description of the CMIP6 experiments (link)
* `driving_experiment_id` (CV) - root identifier of the CMIP6 experiments (link)
* `driving_institution_id` (CV) - an identifier of the institution that is responsible for the driving CMIP6 simulation (link) 
* `driving_source_id` (CV) - CMIP6 model identifier
* `driving_variant_label` - “variant” label of the driving CMIP6 simulation (e.g. “r1i1p1f1” etc.) 
* `frequency` (CV) -  sampling frequency (day, mon, 6hr, 3hr, 1hr) 
* `institution` (CV) - full name of institution that is responsible for CORDEX simulations
* `institution_id` (CV) - an identifier of institution that is responsible for CORDEX simulations
* `mip_era` (CV) - determine what cycle of CMIP defines experiment and data specifications (always ‘CMIP6’)
* `product` (CV) - product type (‘model-output’ and ‘esd-output’ ??? )
* `project_id` (CV) - project identifier (always CORDEX)
* `realm`
* `source` (some build rules) - full model name/version and components (aerosol, atmos, land etc.)
* `source_id` (CV) - model identifier (link)
* `source_type` (CV) - model configuration (RCM, ARCM ???)
* `source_configuration_id` ???
* `tracking_id` (structured form with some CV) - unique file identifier (note 15 in [CMIP6 DRS](https://docs.google.com/document/d/1h0r8RZr_f3-8egBMMh7aqLwy3snpD6_MrDz1q8n5XUk/edit))
* `variable_id` (CV) - variable identifier (link to the CMOR tables)

## Recommended

* `comment` (not mandatory)
* `history` (not mandatory)
* `title` (not mandatory)
* `references` (not mandatory)
* `attribution` (CV) - fixed attribute that attributes driving data ??.

## DRS elements

* `variable_id`: (CV) is the short name of the variable. The name is taken from the [CORDEX-CMIP6 Variable List](https://cordex.org/experiment-guidelines/cordex-cmip6/data-request) or CMOR tables (… link …).

* `domain_id`: (CV) is the name assigned to each of the CORDEX regions and includes a flag for resolution as listed in (… link …). 

* `driving_source_id`: (CV) is an identifier of the driving data. The name consists of a model identifier. For reanalysis driven runs this is the name of the reanalysis data (ERA5). For runs driven by CMIP6 model data this is the associated CMIP6 source_id, which can be found in the [CMIP6 source id CV](https://wcrp-cmip.github.io/CMIP6_CVs/docs/CMIP6_source_id.html). 

* `driving_experiment_id`: (CV) is either “evaluation” for the ERA5-driven experiment or the value of the CMIP6 experiment_id from the ScenarioMIP activity or “historical” for the historical experiment from CMIP. The values for experiment_id can be found in the [CMIP6 experiment id CV](https://wcrp-cmip.github.io/CMIP6_CVs/docs/CMIP6_experiment_id.html). 

* `driving_variant_label`: (CV) identifies the ensemble member of the CMIP6 experiment that produced the forcing data. It has to have the same value as the CMIP6 variant_label. For the evaluation experiment it has to be “r1i1p1f1”.

* `institution_id`: (CV) is an identifier for the institution that is responsible for generating and providing CORDEX simulations. All CORDEX Institutions must be registered to publish their simulations on ESGF. Instructions on how to register an institution and the actual state of the CV is found (… links …). 

* `source_id`: (CV to register) is an identifier (acronym) of the CORDEX RCM. All CORDEX RCMs have to be registered to publish their simulations on ESGF. Instructions on how to register a RCM and the actual state of the CV is found (… links …).

* `source_configuration_id`: (free string) identifies simulations with different combinations of parameterization schemes or changes in parameters for existing schemes. This DRS element can also be used to identify technical reruns related for example to configuration errors. Major upgrades and improvements should be reflected in the RCMModelName.

* `frequency`: (CV) is the output frequency indicator: 1hr - 1 hourly, 3hr - 3 hourly, 6hr - 6 hourly, day=daily, mon=monthly, and fx=invariant fields.

---

Additional depedent attributes that give more detailed meta info will be derived and can be filled automatically.

