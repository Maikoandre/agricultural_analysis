from sqlalchemy import create_engine
from extract import *

engine = create_engine(
    "postgresql://admin:admin123@localhost:5433/geo"
)

malha_territorial = extract_malha_territorial()

malha_territorial.to_postgis(
    "raw_malha_territorial",
    engine,
    if_exists="replace"
)

populacao = extract_populacao()

populacao.to_sql(
    name='raw_populacao',
    con=engine,
    if_exists="replace",
)

producao_agricola = extract_producao_agricola()

producao_agricola.to_sql(
    name="raw_producao_agricola",
    con=engine,
    if_exists="replace"
)

producao_pecuaria = extract_producao_pecuaria()

producao_pecuaria.to_sql(
    name="raw_producao_pecuaria",
    con=engine,
    if_exists="replace"
)

biomas = extract_biomas()

biomas.to_sql(
    name="raw_biomas",
    con=engine,
    if_exists="replace"
)

solo = extract_uso_solo()

solo.to_sql(
    name="raw_uso_solo",
    con=engine,
    if_exists="replace"
)

clima = extract_clima()

clima.to_sql(
    name="raw_clima",
    con=engine,
    if_exists="replace"
)