import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import geopandas as gpd

    return (gpd,)


@app.cell
def _(gpd):
    df = gpd.read_file('data/BR_Municipios_2025/BR_Municipios_2025.shp')

    df.head(10)
    return (df,)


@app.cell
def _(df):
    type(df)
    return


@app.cell
def _(df):
    guanambi = df.loc[df.NM_MUN.isin(['Guanambi'])].copy()
    guanambi.head()
    return (guanambi,)


@app.cell
def _(guanambi):
    guanambi.plot()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
