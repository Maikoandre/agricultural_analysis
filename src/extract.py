import pandas as pd
import geopandas as gpd
import sidrapy

def extract_populacao():
    sidra = sidrapy.get_table(
        table_code='9514', 
        territorial_level='6',
        variable='93',
        ibge_territorial_code='all'
    )
    return sidra

def extract_producao_agricola():
    sidra = sidrapy.get_table(
        table_code='839',
        territorial_level='6',
        variable='214',
        ibge_territorial_code='all'
    )
    return sidra

def extract_producao_pecuaria():
    sidra = sidrapy.get_table(
        table_code='74',
        territorial_level='6',
        variable='106',
        ibge_territorial_code='all'
    )
    return sidra

def extract_biomas():
    sidra = sidrapy.get_table(
        table_code='7016',
        territorial_level='123',
        variable='10476',
        ibge_territorial_code='all'
    )
    return sidra;

def extract_uso_solo():
    sidra = sidrapy.get_table(
        table_code='7319',
        territorial_level='123',
        variable='10473',
        ibge_territorial_code='all'
    )
    return sidra

import pandas as pd


def extract_clima():
    data = pd.read_csv(
        "data/INMET/INMET_NE_BA_A426_GUANAMBI_01-01-2024_A_31-12-2024.CSV",
        encoding="latin1",
        sep=";",
        decimal=",",
        skiprows=8,
        low_memory=False,
    )
    return data

def extract_malha_territorial():
    mapa = gpd.read_file("data/BR_Municipios_2025/BR_Municipios_2025.gpkg")
    return mapa

def transform_malha_territorial():
    mapa = gpd.read_file("data/BR_Municipios_2025/BR_Municipios_2025.shp")
    mapa.to_file("data/BR_Municipios_2025/BR_Municipios_2025.gpkg", driver="GPKG")
