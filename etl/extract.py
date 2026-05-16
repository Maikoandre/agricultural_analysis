import pandas as pd
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
    pass

def extract_biomas():
    pass

def extract_uso_solo():
    sidra = sidrapy.get_table(
        table_code='7319',
        territorial_level='123',
        variable='10473',
        ibge_territorial_code='all'
    )
    return sidra

def extract_malha_territorial():
    pass

def extract_clima():
    pass


raw_data = extract_uso_solo()
raw_data.columns = raw_data.iloc[0]
print(raw_data.columns)