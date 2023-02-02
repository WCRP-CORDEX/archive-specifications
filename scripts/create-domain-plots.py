from os import path as op

import cartopy.crs as ccrs
import geopandas as gpd
import pandas as pd
from pyproj import CRS
from shapely.geometry import Polygon

bookpath = "archive-specifications"
figpath = op.join(bookpath, "figs")

df = pd.read_csv(
    "https://raw.githubusercontent.com/WCRP-CORDEX/domain-tables/main/rotated-latitude-longitude.csv",
    index_col="domain_id",
)


def create_polygon(domain_id):
    """create polygon in rotated pole coords"""
    data = df.loc[domain_id].to_dict()
    coords = [
        [data["ll_lon"], data["ll_lat"]],
        [data["ur_lon"], data["ll_lat"]],
        [data["ur_lon"], data["ur_lat"]],
        [data["ll_lon"], data["ur_lat"]],
    ]
    return Polygon(coords)


def get_ccrs(domain_id):
    data = df.loc[domain_id].to_dict()
    return ccrs.RotatedPole(data["pollon"], data["pollat"])


def get_crs(domain_id):
    data = df.loc[domain_id].to_dict()
    return CRS.from_cf(
        {
            "grid_mapping_name": "rotated_latitude_longitude",
            "grid_north_pole_longitude": data["pollon"],
            "grid_north_pole_latitude": data["pollat"],
        }
    )


def get_geodataframe(domain_id):
    polygon = create_polygon(domain_id)
    crs = get_crs(domain_id)
    return gpd.GeoDataFrame(index=[0], crs=crs, geometry=[polygon])


def get_center(domain_id):
    data = df.loc[domain_id].to_dict()
    return (
        0.5 * (data["ur_lon"] + data["ll_lon"]),
        0.5 * (data["ur_lat"] + data["ll_lat"]),
    )


def transform_center(cenlon, cenlat, transform, proj=None):
    if proj is None:
        proj = ccrs.PlateCarree()
    return proj.transform_point(cenlon, cenlat, transform)


def plot_domain(domain_id, figsize=None):
    import matplotlib.pyplot as plt

    if figsize is None:
        figsize = (10, 10)
    rotated = get_ccrs(domain_id)
    cenlon, cenlat = transform_center(*get_center(domain_id), rotated)
    print(cenlon, cenlat)
    # projection = ccrs.NearsidePerspective(
    #    central_longitude=cenlon, central_latitude=cenlat, globe=None, satellite_height = 10000000
    # )
    # entartet
    if abs(cenlat) > 85.0:
        cenlon = 0.0

    projection = ccrs.Orthographic(
        central_longitude=cenlon, central_latitude=cenlat, globe=None
    )
    # https://stackoverflow.com/questions/59020032/how-to-plot-a-filled-polygon-on-a-map-in-cartopy
    projection._threshold /= 100.0

    plt.figure(figsize=figsize)
    ax = plt.axes(projection=projection)
    ax.stock_img()
    ax.set_title(f"{domain_id} ({df.loc[domain_id].domain})", fontsize=14)

    ax.gridlines(
        draw_labels=True,
        linewidth=0.8,
        color="gray",
        xlocs=range(-180, 180, 15),
        ylocs=range(-90, 90, 15),
    )
    ax.coastlines(resolution="50m", linewidth=0.3, color="black")

    ax.add_geometries(
        [create_polygon(domain_id)],
        crs=get_ccrs(domain_id),
        facecolor="none",
        edgecolor="red",
        alpha=1.0,
        lw=2.0,
    )

    plt.savefig(op.join(figpath, f"{domain_id}.png"))

    return


def create_subsection(domain_id):
    title = df.loc[domain_id].domain
    table = df[df.index == domain_id].to_markdown()
    text = f"## {title}\n\n"
    text += f"![{title}](figs/{domain_id}.png)\n\n"
    text += f"{table}\n"
    return text


def create_domain_section(template):
    sections = "\n".join(create_subsection(d) for d in df.index)
    with open(template, "r") as f:
        tpl = f.read()
    with open(op.join(bookpath, "domains.md"), "w") as f:
        f.write(tpl.format(subsections=sections))


if __name__ == "__main__":
    for domain_id in df.index:
        print(domain_id)
        plot_domain(domain_id)
    create_domain_section(template=op.join(bookpath, "domains.tpl"))
