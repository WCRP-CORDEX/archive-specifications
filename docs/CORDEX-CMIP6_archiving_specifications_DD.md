---
pdf: true
---
# CORDEX-CMIP6 Archiving Specifications for Dynamical Downscaling

!!! warning "Under Development"
    This is a test markdown implementation of the CORDEX-CMIP6 archiving specifications. Until fully tested, please, refer to the official document in Zenodo ([https://doi.org/10.5281/zenodo.15047096](https://doi.org/10.5281/zenodo.15047096)).

21st March 2025

DOI: [10.5281/zenodo.15047096](https://doi.org/10.5281/zenodo.15047096)

Grigory Nikulin<sup>1</sup>, Lars Buntemeyer<sup>2</sup>, Jesús Fernández<sup>3</sup>, Seth McGinnis<sup>4</sup> and Jason P. Evans<sup>5</sup>

 1. Swedish Meteorological and Hydrological Institute (SMHI), Sweden
 2. Climate Service Center Germany (GERICS), Germany
 3. Instituto de Física de Cantabria (IFCA), CSIC-Universidad de Cantabria, Spain
 4. National Center for Atmospheric Research (NCAR), USA
 5. Climate Change Research Centre, University of New South Wales (UNSW), Australia

This document provides Data Reference Syntax (DRS) elements necessary for post-processing CORDEX-CMIP6 simulations and publishing them on the Earth System Grid Federation (ESGF).
The document includes file and directory naming conventions, global attributes and ESGF Search Facets Mapping.
Known issues are collected at [https://github.com/WCRP-CORDEX/archive-specifications/issues](https://github.com/WCRP-CORDEX/archive-specifications/issues).
Newer versions of this document may exist.
Find the latest version under [https://doi.org/10.5281/zenodo.10961068](https://doi.org/10.5281/zenodo.10961068). 

## 1. DRS elements

The DRS element values must consist of the characters a-z, A-Z, 0-9 and '-' (dash).
No other character is allowed.
The terms in brackets following the DRS element names in the list below indicate whether the values must be taken from a controlled vocabulary ('CV'), i.e. a fixed list of values, must be registered with CORDEX ('CV to register'), or must follow a predefined structure  ('structured form').
Note that most elements must have the same value as the mandatory NetCDF global attribute. 

`variable_id` (CV) is the short name of the variable.
The name is taken from the [CORDEX-CMIP6 Variable List](https://cordex.org/experiment-guidelines/cordex-cmip6/data-request) or [CORDEX-CMIP6 CMOR tables](https://github.com/WCRP-CORDEX/cordex-cmip6-cmor-tables/tree/main/Tables).

`domain_id` (CV) is the name assigned to each of the CORDEX regions and includes a flag for resolution as listed in the [CORDEX-CMIP6 domain id CV](https://github.com/WCRP-CORDEX/cordex-cmip6-cv/blob/main/CORDEX-CMIP6_domain_id.json).   
   
`driving_source_id` (CV) is an identifier of the driving data.
The name consists of a model identifier.
For reanalysis driven runs this is the name of the reanalysis data (ERA5).
For runs driven by CMIP6 model data this is the associated CMIP6 source_id, which can be found in the [CORDEX-CMIP6 driving source id CV](https://github.com/WCRP-CORDEX/cordex-cmip6-cv/blob/main/CORDEX-CMIP6_driving_source_id.json).

`driving_experiment_id` (CV) is either "evaluation" for the ERA5-driven experiment, the value of the CMIP6 experiment_id from the ScenarioMIP activity, or "historical" for the historical experiment from CMIP.
The values for driving_experiment_id can be found in the [CORDEX-CMIP6 driving experiment id CV](https://github.com/WCRP-CORDEX/cordex-cmip6-cv/blob/main/CORDEX-CMIP6_driving_experiment_id.json).

`driving_variant_label` (CV) identifies the ensemble member of the CMIP6 simulation that produced the forcing data.
It must have the same value as the variant_label DRS element of the driving CMIP6 simulation (r<k>i<l>p<m>f<n>, see [CMIP6 DRS Appendix 1:  Global Attributes for Labeling Experiments](https://goo.gl/v1drZl)).
For the evaluation experiment driven by ERA5 it is "r1i1p1f1".
For all invariant fields (frequency = fx, e.g. orog or sftlf), `driving_variant_label` must be the same as variant_label of the driving CMIP6 simulation (e.g. r1i1p1f1, r2i1p1f1, etc.); r0i0p0f0 is not allowed.

`institution_id` (CV to register) is an identifier for the institution that is responsible for generating and providing CORDEX simulations.
All CORDEX institutions must be registered to publish their simulations on ESGF.
See instructions on [how to register an institution](https://github.com/WCRP-CORDEX/cordex-cmip6-cv) and the current state of the [CORDEX-CMIP6 institution id CV](https://wcrp-cordex.github.io/cordex-cmip6-cv/CORDEX-CMIP6_institution_id.html).

`source_id` (CV to register) is an identifier (acronym) of the CORDEX RCM.
All CORDEX RCMs must be registered to publish their simulations on ESGF.
See instructions on [how to register a model](https://github.com/WCRP-CORDEX/cordex-cmip6-cv) and the current state of the [CORDEX-CMIP6 source id CV](https://wcrp-cordex.github.io/cordex-cmip6-cv/CORDEX-CMIP6_source_id.html).
Different configurations of the same RCM such as different combinations of parameterization schemes or changes in parameters for existing schemes must be reflected in source_id by a free text suffix (e.g. RCM123, RCM123A for Africa or RCM123T for the tropics).
RCM simulations with spectral nudging must use the "SN" suffix in source_id (e.g. RCM123-SN) while RCM simulations with Newtonian/dynamical nudging must use the "NN" suffix (e.g. RCM123-NN).

`version_realization` (structured form) is a combination that identifies i) versions of CORDEX datasets (simulations) related to technical, configuration, or postprocessing errors and ii) realizations with different initial conditions for RCMs.
This DRS element has the form "vN-rM".
"N" in the version part "vN" is 1 for the first release of dataset (v1) and sequential numbers (2, 3, 4, etc.) for any rerun or re-processing of the dataset (v2, v3, v4, etc.).
The later version always supersedes the earlier version.
"M'' in the realization part "rM" is sequential numbers (1, 2, 3 etc.) that reflect multiple RCM simulations with perturbed initial conditions (r1, r2, r3, etc.) driven by the same GCM and the same GCM member.
The version and realization parts are separated by a dash "-" (e.g. v1-r1, v1-r2, v1-r3).
The version part of this DRS element should not be confused with the ESGF-related DRS element version that has the form "vYYYYMMDD '' and is only included in the ESGF directory structure (see [4. ESGF Directory Structure](#4-esgf-directory-structure)).

`frequency` (CV) is the output frequency indicator: 1hr - 1 hourly, 3hr - 3 hourly, 6hr - 6 hourly, day - daily, mon - monthly, and fx - invariant fields; see the [CORDEX-CMIP6 frequency CV](https://github.com/WCRP-CORDEX/cordex-cmip6-cv/blob/main/CORDEX-CMIP6_frequency.json).

`StartTime` and `EndTime` (structured form) indicate the time span of the file content.
The format is YYYY[MM[DD[hhmm]]], i.e. the year is represented by 4 digits, while the month, day, hour, and minutes are represented by exactly 2 digits, if they are present at all (monthly output - YYYYMM, daily – YYYYMMDD, sub-daily - YYYYMMDDhhmm).
The `StartTime` and `EndTime` of sub-daily instantaneous and average data are based on the time values of the first and last record in the file.
The two dates are separated by a dash.
All time stamps refer to UTC.
Constant fields (`frequency=fx`) do not have the `StartTime`-`EndTime` element in their file names.

`activity_id` (CV) - an identifier of different CORDEX activities such as dynamical downscaling (DD) and empirical-statistical downscaling (ESD), see the [CORDEX-CMIP6 activity id CV](https://github.com/WCRP-CORDEX/cordex-cmip6-cv/blob/main/CORDEX-CMIP6_activity_id.json).

`project_id` (CV) - project identifier ("CORDEX-CMIP6" is the only option)

## 2. Global attributes

**Table 1:** CORDEX-CMIP6 global attribute description (see examples in section [13.6](#136-global-attributes)) and comparison with CORDEX-CMIP5

--8<-- "global_attributes.md"

Table 1 notes:

 1. The "grid" global attribute can be used to describe the horizontal grid and regridding procedure.   There is no standard form used to record this information, but it is suggested that when appropriate the following be indicated:  brief description of native grid and resolution, and if data have been regridded, regridding procedure and description of target grid (see note 10 in [CMIP6 DRS](https://goo.gl/v1drZl)).  Here are some examples:
```python
   grid = "Lambert conic conformal with 25 km grid spacing"
   grid = "Rotated-pole latitude-longitude with 0.22 degree grid spacing"
   grid = "Rotated-pole latitude-longitude with 0.11 degree grid spacing, interpolated by 2nd order conservative remapping    from the original unstructured icosahedral ICON grid R13B05 (~12.1 km)"
   grid = "Rotated-pole latitude-longitude with 0.22 degree grid spacing; ocean grid Mediterranean Sea only, 9-12 km with a tilted and stretched grid at the Gibraltar Strait"
```

 2. The `version_realization_info` global attribute provides information on how  new reruns (e.g. v2, v3, etc.) and/or realizations (e.g. r2, r3, etc.) are generated; recommended if the `version_realization` is not v1-r1.

 3. `tracking_id` must be of the form `<PID>/<uuid>` where PID is a Persistent Identifier (`hdl:21.14103` for CORDEX-CMIP6) and  uuid is a Universally Unique IDentifier e.g. `hdl:21.14103/187fcd6c-7cc6-11ee-9481-7824afb1963b`. The `tracking_id` should be unique for each CORDEX-CMIP6 file published in ESGF.  The `<uuid>` should be generated using the OSSP utility which supports a number of different DCE 1.1 variant UUID options.  For CORDEX-CMIP6, version 4 (random number based) is required.  Download the software from [OSSP uuid](http://www.ossp.org/pkg/lib/uuid/). (see note 15 in [CMIP6 DRS](https://goo.gl/v1drZl)).

## 3. File naming

file_name=`<variable_id>_<domain_id>_<driving_source_id>_<driving_experiment_id>_<driving_variant_label>_<institution_id>_<source_id>_<version_realization>_<frequency>[_<StartTime>-<EndTime>].nc`

Examples:
```
tas_AFR-25_ERA5_evaluation_r1i1p1f1_INST_RCM123_v1-r1_mon_201101-202012.nc
tas_AFR-25_GCM_historical_r1i1p1f1_INST_RCM123_v1-r1_mon_201101-201412.nc
tas_AFR-25_GCM_ssp370_r1i1p1f1_INST_RCM123_v1-r1_mon_201501-202012.nc
orog_AFR-25_GCM_ssp370_r1i1p1f1_INST_RCM123_v1-r1_fx.nc
```
In contrast to CORDEX-CMIP5: 

i) the institution that is responsible for CORDEX simulations (institution_id) and model acronym (source_id) are 2 different DRS elements, i.e. separated by the underscore "_" in the file name

ii) the institution that is responsible for the driving CMIP6 simulation (driving_institution_id) is not a part of DRS and not included in the file name and ESGF directory structure.

## 4. ESGF directory structure

directory_structure=`<project_id>/<activity_id>/<domain_id>/<institution_id>/<driving_source_id>/<driving_experiment_id>/<driving_variant_label>/<source_id>/<version_realization>/<frequency>/<variable_id>/<version>/`

The  <version> DRS element indicates an approximate date of model output files or publication on ESGF and has the form "vYYYYMMDD" (e.g., "v20231206").
 This is the only DRS element that is not stored as a global attribute.
Note that files contained in a single <version>  subdirectory at the end of the directory path should represent all the available time-samples reported from the simulation; a time-series can be split across several files, but all the files must be found in the same subdirectory.
This implies that <version> will not generally be the actual date that all files in the subdirectory were written or published (see also Directory structure template in [CMIP6 DRS](https://goo.gl/v1drZl)).

Examples:

```
/CORDEX-CMIP6/DD/AFR-25/INST/ERA5/evaluation/r1i1p1f1/RCM123/v1-r1/mon/tas/v20240319
/CORDEX-CMIP6/DD/AFR-25/INST/GCM/historical/r1i1p1f1/RCM123/v1-r1/mon/tas/v20240319
/CORDEX-CMIP6/DD/AFR-25/INST/GCM/ssp370/r1i1p1f1/RCM123/v1-r1/mon/tas/v20240319
/CORDEX-CMIP6/DD/AFR-25/INST/GCM/ssp370/r1i1p1f1/RCM123/v1-r1/fx/orog/v20240319
```

## 5. File format

Data files must be in  NetCDF format, version 4, using the NetCDF 4 classic data model.
It is recommended that data should be compressed by using "deflate level" 1 and with "shuffle" turned on.
Data files must conform to the [CF Conventions 1.11](https://cfconventions.org/Data/cf-conventions/cf-conventions-1.11/cf-conventions.html).

Each file may contain only one output field (target variable) from a single simulation.
It must include a target variable with attributes defined in the [CORDEX-CMIP6 CMOR tables](https://github.com/WCRP-CORDEX/cordex-cmip6-cmor-tables/tree/main/Tables) and coordinate variables.
The entire time series of a target variable is to be distributed over several files as described in section [8 Time period for each data file](#8-time-period-for-each-data-file).

All output fields must be single precision (type NC_FLOAT), while all coordinate variables (time and space) must be double precision (type NC_DOUBLE).
All missing data must be assigned the single precision floating point value of 1.e20.

## 6. CORDEX domains and horizontal coordinates

The CORDEX domains are defined in the [CORDEX domain tables](https://github.com/WCRP-CORDEX/domain-tables).
A domain must lie fully inside the RCM interior computational domain, i.e. in the area left once the relaxation zone is excluded.
It is strongly recommended that RCMs using the rotated-pole coordinate system exactly follow the CORDEX grid definition provided.
The rotated-pole coordinate system is always defined in terms of rotation of the North Pole in accordance with [CF-1.11](https://cfconventions.org/Data/cf-conventions/cf-conventions-1.11/cf-conventions.html#grid-mappings-and-projections).
All variables from a simulation must be provided on the same grid (i.e., variables on staggered grids must be regridded to the standard grid).
Zonal and meridional winds must be provided as real north- and eastward winds if the RCM uses a coordinate system/projection that does not coincide with real north- and eastward directions (e.g. the rotated pole, Lambert Conformal, etc.).

The domain acronym is ‘domain name’-‘resolution’, where ‘resolution’ is the nearest grid spacing in km of the 3 resolutions used in CORDEX-CMIP5 and CORDEX-CMIP6 (50, 25 and 12 km).
Changing ‘resolution’ from degrees, which are related only to the rotated coordinate system (CORDEX-CMIP5), to the more common kilometres allows us to unify the terminology used in CORDEX, making it easily understandable by all users.
For example, "AFR-25" means the CORDEX-Africa domain with 25 km resolution in a projected coordinate system and 0.22° resolution in the rotated pole coordinate system.
The resolution flag indicates the resolution of the atmospheric component of CORDEX models.
The domain acronyms for the regular grids are the same as those for the corresponding model grid with the letter 'i' appended to the resolution (e.g. "AFR-25i").

Data must  be provided for the CORDEX domain only, i.e. the relaxation zones must be removed before the data is delivered.
Names of the CORDEX domains are provided in [CORDEX-CMIP6 domain id CV](https://github.com/WCRP-CORDEX/cordex-cmip6-cv/blob/main/CORDEX-CMIP6_domain_id.json).

Data files must contain a full description of native coordinate systems used by RCMs:

 * the 1-dimensional coordinate variables (e.g. rlon and rlat for the rotated pole coordinate system or x and y for the Lambert Conformal Conic (LCC) projection),

 * grid mapping variable crs[^1] describing the coordinate reference system and

 * the variable attribute - `grid_mapping = "crs"`

in accordance with [CF-1.11](https://cfconventions.org/Data/cf-conventions/cf-conventions-1.11/cf-conventions.html#grid-mappings-and-projections) (see examples [13.1](#131-rotated-pole-coordinate-system) and [13.2](#132-lambert-conformal-conic-projection)).
The grid mapping variable crs is of arbitrary type (e.g. char or int) since it contains no data.
The shape and size of the Earth used for the model grid must be specified.
For a spherical earth this is done via the crs attribute earth_radius.
If a model grid specifies an ellipsoid for the shape of the earth then see [CF-1.11 Appendix F](https://cfconventions.org/Data/cf-conventions/cf-conventions-1.11/cf-conventions.html#appendix-grid-mappings).

The 2-dimensional geographic latitudes and longitudes of the model grid cells (lon and lat) must be also provided as auxiliary coordinates.
Longitude coordinates must be strictly monotonically increasing and confined to the range -180 to 360; they must also have absolute values as small as possible given the first two constraints (e.g., store 170 E to 170 W as 170 to 190, but store 150 W to 130 W as -150 to -130, not 210 to 230). 

For models with native unstructured grids, it is up to the regional CORDEX communities to decide whether data must be remapped to one of the regular lat-lon domain grids (e.g., AFR-25i) or to the most common native RCM grid used for a specific CORDEX domain.

## 7. Time coordinate

The units of the time coordinate is `days since 1950-01-01`[^2] for all files.
The earlier reference date `days since 1850-01-01` is also allowed if a RCM group downscales a longer period that includes the pre-1950 era.
All time dependent variables must have an attribute `cell_methods: time` with values provided in the [CORDEX-CMIP6 CMOR tables](https://github.com/WCRP-CORDEX/cordex-cmip6-cmor-tables/tree/main/Tables).

The time value of the instantaneous data is [0Z, 6Z, 12Z, 18Z], [0Z, 3Z, 6Z, 9Z, 12Z, 15Z, 18Z, 21Z], and [0Z, 1Z, 2Z, 3Z, ..., 20Z, 21Z, 22Z, 23Z]  of each day for the 6-, 3-, and 1-hourly data respectively.

Variables that are representative of an interval (averages, maxima, minima, sum) must use the midpoints of the time intervals (bounds) as time coordinate values.
Therefore, these variables have the time values 0.5Z, 1.5Z, 2.5Z, ..., 23.5Z (1-hourly); 1.5Z, 4.5Z, 7.5Z, ... 22.5Z (3-hourly); 3Z, 9Z, 15Z, 21Z (6-hourly); 12Z (daily); Jan 16 12Z, Feb 15 0Z; (monthly, non leap years); Jan 16 12Z, Feb 12Z (monthly, leap years); Jan 16 0Z, Feb 16 0Z (monthly, 360 day); etc.

Furthermore, interval variables must have a `time_bnds` field of dimensions `(ntimes,2)`, where `ntimes` is the dimension of the time coordinate (see an example in section [13.4](#134-time-coordinate)).
Intervals for daily and monthly data should start and end at 00:00:00 UTC of the appropriate day.
Intervals for sub-daily data should start and end at 00:00:00 UTC or an integer multiple of the frequency (1, 3, or 6 hours) from that point.

The time variable must have a calendar attribute.
Use of the proleptic-gregorian or standard calendar is strongly recommended when possible.
Other calendars (360_day and 365_day) inherited from the driving models are also allowed.
If the driving model uses the gregorian calendar (which is deprecated since CF-1.9), use the standard calendar.

## 8. Time period for each data file

The time spans to be included in a single file depend on the aggregation, which is 1-hourly, 6-hourly, daily, monthly, or invariant:

* 1-hourly or 6-hourly: one year,  
* daily: 5 years, or less if some of the years in the 5-year period are unavailable,  
* monthly: 10 years, or less if some of the years in the 10-year period are unavailable,  
* invariant: single file.

Files should always contain full years if the data are available, but are allowed to be shorter if it is not.

Files with monthly data start with years that end with '1' or the first year of the experiment; they end with '0' or the last year of the experiment.
Daily data files start with years that end with '1' or '6' or the first experiment year; the last year they contain ends with '5' or '0' or is the last experiment year.
For example, the ERA5-driven evaluation experiment for 1979-2021 with 1979 as a spin-up:

| monthly | daily | subdaily |
| :---: | :---: | :---: |
| 1980-1980<br>1981-1990<br>1991-2000<br>2001-2010<br>2011-2020<br>2021-2021 | 1980-1980<br>1981-1985<br>1986-1990<br>...<br>2016-2020<br>2021-2021 | 1980-1980<br>1981-1981<br>1982-1982<br>...<br>2020-2020<br>2021-2021 |

## 9. License

All CORDEX modeling groups choose a license for their CMIP6-driven simulations depending on institutional and/or funding agency policies.
This information is necessary to register a RCM in the [CORDEX-CMIP6 source id CV.](https://github.com/WCRP-CORDEX/cordex-cmip6-cv/blob/main/CORDEX-CMIP6_source_id.json) It is strongly recommended to use the Creative Commons Attribution 4.0 International ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)) license, as is currently used in [CMIP6](https://pcmdi.llnl.gov/CMIP6/TermsOfUse/TermsOfUse6-2.html).
Note, that any kind of "non-commercial" license will significantly limit the use of the data in downstream climate mitigation and adaptation applications.

The global attribute license has the only option "[https://cordex.org/data-access/cordex-cmip6-data/cordex-cmip6-terms-of-use](https://cordex.org/data-access/cordex-cmip6-data/cordex-cmip6-terms-of-use)" leading to the CORDEX-CMIP6 Terms of Use page.

## 10. Registration

All institutions (modelling groups) that contribute or plan to contribute to CORDEX-CMIP6 must

 1. register their institution and model following the instructions on [how to register institutions and models](https://github.com/WCRP-CORDEX/cordex-cmip6-cv) and 

 2. provide information about their planned simulations in the [CORDEX-CMIP6 downscaling plan](https://github.com/WCRP-CORDEX/simulation-status). 

The modelling groups will not be able to publish their CORDEX-CMIP6 simulations on ESGF without first registering their institution and model.

## 11. ESGF Search Facets Mapping

| ESGF Search Facet | CORDEX-CMIP6 DRS element or global attribute | Values |
| ----- | ----- | ----- |
| Project | project_id | "CORDEX-CMIP6" is the only option (CV) |
| Activity | activity_id | "DD" is the only option (CV) |
| Product | product | "model-output" is the only option (CV) |
| Domain ID | domain_id | AFR-25, EUR-12, AFR-25i, etc. (CV) |
| Driving Source ID | driving_source_id | ERA5 or CMIP6 models (CV) |
| Source ID | source_id | CORDEX models (CV) |
| Institution ID | institution_id | CORDEX institutions (CV) |
| Source Type | source_type | ARCM, AORCM, AGCM, AOGCM (CV) |
| Experiment ID | driving_experiment_id | evaluation, historical, ssp370, etc. (CV) |
| Variant Label | driving_variant_label | r1i1p1f1, r2i1p1f1, etc. (structured form) |
| Version-Realization | version_realization | v1-r1, v2-r1, v1-r2, etc. (structured form) |
| Frequency | frequency | mon, day, 6hr, 1hr, fx (CV) |
| Variable | variable_id | tas, pr, tasmax, etc. (CMOR tables) |

## 12. User support

In case of any questions or doubts please create an issue in [https://github.com/WCRP-CORDEX/cordex-cmip6-cv](https://github.com/WCRP-CORDEX/cordex-cmip6-cv). 

## Acknowledgments

We thank all who provided their valuable comments and suggestions on the CORDEX-CMIP6 archiving specifications for dynamical downscaling.

## 13. Examples

### 13.1 Rotated Pole Coordinate System

```cdl
char crs ;
    crs:grid_mapping_name = "rotated_latitude_longitude" ;
    crs:grid_north_pole_latitude = 39.25 ;
    crs:grid_north_pole_longitude = -162. ;
    crs:earth_radius = 6371229. ;

double rlon(rlon) ;
    rlon:standard_name = "grid_longitude" ;
    rlon:long_name = "longitude in rotated pole grid" ;
    rlon:units = "degrees" ;

double rlat(rlat) ;
    rlat:standard_name = "grid_latitude" ;
    rlat:long_name = "latitude in rotated pole grid" ;
    rlat:units = "degrees" ;

double lon(rlat, rlon) ;
    lon:standard_name = "longitude" ;
    lon:long_name = "longitude" ;
    lon:units = "degrees_east" ;

double lat(rlat, rlon) ;
    lat:standard_name = "latitude" ;
    lat:long_name = "latitude" ;
    lat:units = "degrees_north" ;

float pr(time, rlat, rlon) ;
    pr:standard_name = "precipitation_flux" ;
    pr:long_name = "Precipitation" ;
    pr:units = "kg m-2 s-1" ;
    pr:coordinates = "lon lat" ;
    pr:_FillValue = 1.e+20f ;
    pr:missing_value = 1.e+20f ;
    pr:cell_methods = "time: mean" ;
    pr:grid_mapping = "crs" ;
```

### 13.2 Lambert Conformal Conic projection

```cdl
int crs ;
    crs:grid_mapping_name = "lambert_conformal_conic" ;
    crs:standard_parallel = 49.5 ;
    crs:longitude_of_central_meridian = 10.5 ;
    crs:latitude_of_projection_origin = 49.5 ;
    crs:false_easting = 2925000. ;
    crs:false_northing = 2925000. ;
    crs:earth_radius = 6371229. ;

double x(x) ;
    x:standard_name = "projection_x_coordinate" ;
    x:long_name = "X Coordinate Of Projection" ;
    x:units = "m" ;

double y(y) ;
    y:standard_name = "projection_y_coordinate" ;
    y:long_name = "Y Coordinate Of Projection" ;
    y:units = "m" ;

double lon(y, x) ;
    lon:standard_name = "longitude" ;
    lon:long_name = "longitude" ;
    lon:units = "degrees_east" ;

double lat(y, x) ;
    lat:standard_name = "latitude" ;
    lat:long_name = "latitude" ;
    lat:units = "degrees_north" ;

float pr(time, y, x) ;
    pr:standard_name = "precipitation_flux" ;
    pr:long_name = "Precipitation" ;
    pr:units = "kg m-2 s-1" ;
    pr:coordinates = "lon lat" ;
    pr:_FillValue = 1.e+20f ;
    pr:missing_value = 1.e+20f ;
    pr:cell_methods = "time: mean" ;
    pr:grid_mapping = "crs" ;
```

### 13.3 Vertical coordinate depth

a surface model with 4 layers:  layer 1: 0-7cm, layer 2: 7-28cm, layer 3: 28-100cm, layer 4: 100-289cm

```cdl
dimensions:
  bnds = 2 ;
  depth = 4 ;

variables:

  double depth(depth) ;
    depth:standard_name = "depth" ;
    depth:long_name = "depth" ;
    depth:units = "m" ;    
    depth:bounds = "depth_bnds" ;
    depth:positive = "down" ;

  double depth_bnds(depth, bnds) ;

data:

  depth = 0.035, 0.175, 0.64, 1.945 ;

  depth_bnds =
    0, 0.7,
    0.7, 0.28,
    0.28, 1,
    1, 2.89 ;
```

### 13.4 Time coordinate

for a daily variable representative of an interval (e.g. pr, tasmax)

```cdl
dimensions:

   time = UNLIMITED ;
   bnds = 2 ;

variables:

   double time(time);
      time:long_name = "time";
      time:units = "days since 1950-01-01";
      time:calendar = "standard"
      time:bounds = "time_bnds";

   double time_bnds(time, bnds) ;

data:

   time = 0.5, 1.5, 2.5, ... ;

   time_bnds = 
      0, 1,
      1, 2,
      2, 3,
      ... ;
```

### 13.5 Scalar coordinate variables

for variables on individual levels (e.g. at 2 meters, or at 850 hPa), do not include an extra dimension of size 1.
Use a [CF scalar coordinate variable](https://cfconventions.org/Data/cf-conventions/cf-conventions-1.11/cf-conventions.html#scalar-coordinate-variables) instead.

```cdl
variables:

	double height ;
		height:units = "m" ;
		height:axis = "Z" ;
		height:positive = "up" ;
		height:long_name = "height" ;
		height:standard_name = "height" ;

	float tas(time, rlat, rlon) ;
        [...]
		tas:coordinates = "height lat lon" ;
data:

   height = 2. ;
```
 

### 13.6 Global attributes

```cdl
// global attributes:
  :Conventions = "CF-1.11" ;
  :activity_id = "DD" ;
  :comment = "optional" ;
  :contact = "[cordex-data@iircm.org](mailto:cordex-data@iircm.org)" ;
  :creation_date = "2023-11-19T18:01:15Z" ;	
  :domain = "Africa" ;
  :domain_id = "AFR-25" ;
  :driving_experiment = "reanalysis simulation of the recent past" ;
  :driving_experiment_id = "evaluation" ;
  :driving_institution_id = "ECMWF" ;
  :driving_source_id = "ERA5" ;
  :driving_variant_label = "r1i1p1f1" ;
  :frequency = "mon" ;
  :grid = "Lambert conic conformal with 25 km grid spacing"
  :institution = "Interdisciplinary Institute of Regional Climate Modeling" ;
  :institution_id = "IIRCM" ;
  :license = "[https://cordex.org/data-access/cordex-cmip6-data/  cordex-cmip6-terms-of-use](https://cordex.org/data-access/cordex-cmip6-data/  cordex-cmip6-terms-of-use)" ;
  :mip_era = "CMIP6" ;
  :product = "model-output" ;
  :project_id = "CORDEX-CMIP6" ;
  :source = "Interdisciplinary Regional Climate Model version 1" ;
  :source_id = "InterRCM1" ;
  :source_type = "ARCM" ;
  :tracking_id = "hdl:21.14103/187fcd6c-7cc6-11ee-9481-7824afb1963b" 
  :variable_id = "tas" ;
  :version_realization = "v1-r1" ;
```

## 14. Version history

| Version | Date | Comment |
| :---: | :---- | :---- |
| v2 | 2025-03-21 | <ul><li>Change of project_id (CORDEX to CORDEX-CMIP6) due to ESGF publication requirements ([#22](https://github.com/WCRP-CORDEX/archive-specifications/issues/22)) <li>`mip_era` is excluded from the ESGF directory structure and search facets mapping, must be presented as the global attribute only ([#24](https://github.com/WCRP-CORDEX/archive-specifications/issues/24)) <li>Fixed example for `creation_date` global attribute ([#19](https://github.com/WCRP-CORDEX/archive-specifications/issues/19)) <li>New example (13.5) illustrating scalar coordinate variables for height ([#18](https://github.com/WCRP-CORDEX/archive-specifications/issues/18)) <li>Specify time coordinate origin, but not specific formatting ([#5](https://github.com/WCRP-CORDEX/archive-specifications/issues/5)) <li>Allow grid mapping variable to match the grid_mapping_name ([#17](https://github.com/WCRP-CORDEX/archive-specifications/issues/17))</ul> |
| v1 | 2024-04-10 | Initial release on April, 10th, 2024. |

[^1]:  The grid mapping variable is also allowed to be called after the CF standard grid_mapping_name used. This is the default hardcoded behaviour in the CMOR library as of version 3.9.0 (2024-08-28). Of course, the main variable corresponding grid_mapping attribute should then match this grid mapping variable name.

[^2]:  The format of the reference date can be either "days since 1950-01-01" (preferred), "days since 1950-01-01 00:00:00", or "days since 1950-01-01T00:00:00Z"