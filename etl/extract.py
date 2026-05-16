import pandas as pd
import sidrapy

def extract_data():
    sidra = sidrapy.get_table(
        table_code='9514', 
        territorial_level='6',
        variable='93',
        ibge_territorial_code='all'
    )
    return sidra

raw_data = extract_data()
raw_data.head()