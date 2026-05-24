# pyright: reportUndefinedVariable=false

import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import geopandas as gpd
    import pandas as pd
    import matplotlib.pyplot as plt
    from sqlalchemy import create_engine

    return create_engine, gpd, pd, plt


@app.cell
def _(gpd):
    df = gpd.read_file('/home/maiko/Projects/agricultural_analysis/data/BR_RG_Imediatas_2025/BR_RG_Imediatas_2025.shp')
    df.head()
    return (df,)


@app.cell
def _(df):
    gbi = df.loc[df.NM_RGI.isin(['Guanambi'])].copy()
    gbi.head()
    return (gbi,)


@app.cell
def _(gbi):
    gbi.plot()
    return


@app.cell
def _(pd):
    deforestation = pd.read_csv('/home/maiko/Projects/agricultural_analysis/data/Biomas/Time series of Deforestation • Annual by class • 1987 - 2024.csv')
    deforestation.head()
    return (deforestation,)


@app.cell
def _(deforestation):
    df_long = deforestation.melt(
        id_vars=['Level 1'],
        var_name='ano',
        value_name='area'
    )
    df_long = df_long.rename(columns={'Level 1': 'classe'})
    df_long['ano'] = df_long['ano'].astype(int)
    df_long['area'] = df_long['area'].astype(float)
    df_long = df_long.sort_values(by='ano')
    df_long.head()
    return (df_long,)


@app.cell
def _(df_long, plt):
    df_long.plot(x='ano', y='area', kind='line')
    plt.title('Deforestation over time')
    plt.xlabel('Year')
    plt.ylabel('Deforested Area (hectares)')
    plt.grid()
    plt.show()
    return


@app.cell
def _(df_long):
    valor_inicial = df_long['area'].iloc[0]
    valor_final = df_long['area'].iloc[-1]
    crescimento = (
        (valor_final - valor_inicial)
        / valor_inicial
    ) * 100

    print(crescimento)
    return


@app.cell
def _(df_long, plt):
    df_long['media_movel'] = df_long['area'].rolling(window=5).mean()
    plt.figure(figsize=(12,6))

    plt.plot(
        df_long["ano"],
        df_long["area"],
        label="Original"
    )

    plt.plot(
        df_long["ano"],
        df_long["media_movel"],
        label="Média móvel"
    )

    plt.legend()

    plt.show()
    return


@app.cell
def _(create_engine, pd):
    engine = create_engine(
        "postgresql://admin:admin123@localhost:5433/geo"
    )

    df_raw = pd.read_sql("SELECT * FROM raw_producao_agricola", engine)
    producao_agricola = df_raw.copy()
    producao_agricola.columns = producao_agricola.iloc[0]
    producao_agricola = producao_agricola[1:].reset_index(drop=True)
    return (producao_agricola,)


@app.cell
def _(producao_agricola):
    producao_agricola.head()
    return


@app.cell
def _(producao_agricola):
    producao_agricola.columns
    return


@app.cell
def _(producao_agricola):
    producao_agricola["Valor"].unique()
    return


@app.cell
def _(producao_agricola):
    producao_agricola[
        "Produto das lavouras temporárias"
    ].unique()
    return


if __name__ == "__main__":
    app.run()
