import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import geopandas as gpd

    return (gpd,)


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
def _():
    return


if __name__ == "__main__":
    app.run()
