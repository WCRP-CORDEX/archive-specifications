# CORDEX-CMIP6 Archiving Specifications

## Overview

This section provides the archiving specifications for CORDEX-CMIP6 simulations.

The CORDEX-CMIP6 archiving specifications define the Data Reference Syntax (DRS) elements necessary for post-processing CORDEX-CMIP6 simulations and publishing them on the Earth System Grid Federation (ESGF).

## Available Documents

### Dynamical Downscaling

The [Archiving Specifications for Dynamical Downscaling](CORDEX-CMIP6_archiving_specifications_DD.md) document includes:

- **DRS elements**: Variable ID, domain ID, driving source ID, experiment ID, variant labels, institution ID, source ID, version realization, frequency, time stamps, activity ID, and project ID
- **Global attributes**: Required metadata attributes for NetCDF files
- **File naming conventions**: Standard naming patterns for output files
- **ESGF directory structure**: Directory organization for data publication
- **File format requirements**: NetCDF specifications and CF conventions
- **CORDEX domains and coordinates**: Grid definitions and coordinate systems
- **Time coordinate specifications**: Time handling and calendar conventions
- **Registration requirements**: How to register institutions and models

## Reference Information

- **Latest Version**: [DOI: 10.5281/zenodo.10961068](https://doi.org/10.5281/zenodo.10961068)
- **Global Attributes Reference**: See the [Global Attributes](global_attributes.md) page for a complete reference table
- **Issues**: Report issues at [GitHub Issues](https://github.com/WCRP-CORDEX/archive-specifications/issues)
- **CVs**: Controlled vocabularies are maintained at [CORDEX-CMIP6 CV repository](https://github.com/WCRP-CORDEX/cordex-cmip6-cv)

## Version History

| Version | Date | Comment |
|---------|------|---------|
| v2 | 2025-03-21 | Change of project_id (CORDEX to CORDEX-CMIP6); mip_era excluded from ESGF directory structure; Fixed creation_date example; New scalar coordinate variables example; Specify time coordinate origin; Allow grid mapping variable to match grid_mapping_name |
| v1 | 2024-04-10 | Initial release |
