# 🌵 Expansão Agrícola e Impacto Ambiental na Caatinga

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)

> ⚠️ **Nota:** Este projeto está em **ativo desenvolvimento**. A estrutura inicial de banco de dados, os scripts de extração e os notebooks de análise exploratória já foram estabelecidos, enquanto a modelagem dbt avançada e os dashboards de consumo serão implementados nas próximas etapas.

Este projeto de **Geospatial Analytics** e **Analytics Engineering** analisará a relação entre a expansão das atividades agrícolas/pecuárias e a supressão de vegetação nativa no bioma **Caatinga**, um ecossistema exclusivamente brasileiro e altamente vulnerável à desertificação.

O projeto adotará uma abordagem moderna de **ELT (Extract, Load, Transform)**, onde dados geoespaciais e tabulares serão extraídos de fontes oficiais (IBGE e MapBiomas), consolidados em um banco de dados geográfico **PostgreSQL/PostGIS**, modelados semanticamente usando **dbt** e analisados por meio de notebooks interativos (**marimo**) e visualizações dinâmicas no **Metabase**.

---

## 🔮 Próximos Passos & Melhorias Futuras

- [ ] **Modelagem dbt Completa**: Desenvolver todas as queries SQL de staging e marts para limpar as tabelas `raw_` geradas pela carga Python.
- [ ] **Cruzamentos Espaciais complexos no dbt**: Implementar as macros e views espaciais no dbt utilizando funções PostGIS.
- [ ] **Configuração do Metabase**: Conectar o container do Metabase à camada analítica final (`marts/`) para estruturação dos painéis interativos.
- [ ] **CI/CD Automático**: Habilitar a validação automática (Pull Request/Push) dos modelos dbt no GitHub Actions usando banco de testes temporário.

---

## 🗺️ 1. Introdução

A **Caatinga** ocupa cerca de 10% do território nacional e abriga uma rica biodiversidade adaptada ao clima semiárido. Contudo, frentes de expansão agrícola e pecuária têm avançado sobre suas florestas secas. Este avanço, muitas vezes desordenado, causa fragmentação de habitats, perda de solo e acelera processos de desertificação.

Este projeto visa estruturar uma **plataforma analítica geoespacial** para entender onde, quando e com qual intensidade essas transformações ocorrem, fornecendo uma base técnica para o estudo de vetores de desmatamento e conservação ambiental.

---

## 🎯 2. Objetivos do Projeto

*   📈 **Análise Temporal da Expansão Agrícola**: Mapear o crescimento da área colhida e a evolução da pecuária nos municípios da Caatinga ao longo do tempo.
*   🌳 **Monitoramento da Supressão Vegetal**: Analisar as mudanças de cobertura vegetal nativa e quantificar as áreas convertidas em pastagem ou agricultura.
*   🔍 **Correlação Espacial e Temporal**: Cruzar estatísticas agrícolas do IBGE com dados de uso e cobertura do solo para identificar hotspots de desmatamento impulsionados por commodities específicas.
*   🗺️ **Visualização Geoespacial**: Gerar mapas interativos e painéis analíticos que facilitem a interpretação visual dos vetores de desmatamento.
*   🏗️ **Engenharia de Dados Moderna**: Consolidar um pipeline estruturado e versionado de dados geográficos usando as melhores práticas de Analytics Engineering (ELT, dbt, modelagem modular e testes).

---

## ❓ 3. Perguntas Analíticas Principais

O projeto buscará responder às seguintes perguntas:
1.  **Quais municípios da Caatinga apresentarão a maior taxa de conversão de vegetação nativa em áreas agrícolas nos últimos anos?**
2.  **Existe uma correlação direta entre o aumento do rebanho bovino/área colhida de grãos e a perda de florestas secas na Caatinga?**
3.  **Como as anomalias de precipitação (dados de clima do INMET) se relacionarão com as perdas agrícolas e o avanço da fronteira em áreas marginais?**
4.  **Quais microrregiões geográficas apresentarão maior risco ecológico imediato devido ao avanço da infraestrutura agropecuária?**

---

## 🏗️ 4. Arquitetura do Projeto (Planejada)

O fluxo de dados seguirá a filosofia **ELT moderna**, onde a extração e a carga serão feitas em Python, e toda a modelagem geométrica e transformações serão delegadas ao banco de dados utilizando **dbt** e **PostGIS**.

<p align="center">
  <img src="assets/Untitled-2026-05-13-0814.png" alt="Arquitetura do Projeto" width="100%">
</p>


---

## 🛠️ 5. Stack Tecnológica

*   **Linguagem Principal**: [Python 3.11+](https://www.python.org/)
*   **Ingestão de Dados**: [Pandas](https://pandas.pydata.org/) & [GeoPandas](https://geopandas.org/) (carga geométrica inicial via SQLAlchemy/GeoAlchemy2)
*   **Interface de APIs**: [Sidrapy](https://github.com/AlanTaranti/sidrapy) (Cliente oficial da API SIDRA do IBGE)
*   **Interface de Notebooks**: [Marimo](https://marimo.io/) (Notebooks analíticos reativos salvos em `.py` puro)
*   **Banco de Dados**: [PostgreSQL 16+](https://www.postgresql.org/) com extensão espacial [PostGIS 3+](https://postgis.net/)
*   **Transformação e Modelagem**: [dbt-core](https://www.getdbt.com/) com adaptador `dbt-postgres` (a ser implementado)
*   **Infraestrutura**: [Docker & Docker Compose](https://www.docker.com/) (Instanciação do banco PostGIS e Metabase)

---

## 🔄 6. Pipeline de Dados (Fluxo ELT)

O pipeline será estruturado em três etapas distintas:

1.  **Extract & Load (EL - Implementado/Em Ajustes)**:
    *   Scripts Python (`src/extract.py` e `src/load.py`) consultam as APIs do IBGE SIDRA trazendo dados demográficos, uso da terra, produção agrícola e pecuária.
    *   Dados de clima locais e limites geográficos são lidos com **GeoPandas** e salvos no banco.
    *   A carga é feita no PostGIS com o prefixo `raw_` de forma a persistir as geometrias e tabelas brutas originais.
2.  **Transform (T - Planejado com dbt)**:
    *   Os dados brutos na camada **RAW** serão limpos, padronizados e enriquecidos na camada de **Staging**.
    *   Índices espaciais, agregações municipais e correlações temporais serão consolidados na camada de **Marts** (tabelas de consumo final).
3.  **Consume (Análise & Insights - Em Andamento)**:
    *   Notebooks exploratórios no **Marimo** e dashboards visuais no **Metabase** consumirão a base de dados refinada.

---

## 📂 7. Estrutura de Pastas

Abaixo está o layout organizacional planejado e em consolidação para o repositório:

```text
agricultural_analysis/
├── .github/
│   └── workflows/
│       └── dbt_ci.yml          # Pipeline de integração contínua (Futuro)
├── assets/                     # Recursos visuais (diagramas, imagens)
├── data/                       # Armazenamento local de dados brutos (IGNORADOS no Git)
│   ├── BR_Municipios_2025/     # Geometrias municipais do IBGE
│   ├── BR_RG_Imediatas_2025/   # Limites das Regiões Geográficas Imediatas
│   ├── Biomas/                 # Dados históricos de desmatamento/uso do solo
│   └── INMET/                  # Séries temporais meteorológicas (Guanambi/região)
├── src/                        # Código-fonte da aplicação
│   ├── extract.py              # Funções de extração das fontes (SIDRA, INMET, Geometrias)
│   ├── load.py                 # Orquestrador da carga inicial no PostgreSQL/PostGIS
│   ├── notebooks/              # Notebooks analíticos interativos (marimo)
│   │   └── regiao_gbi.py       # EDA da região de Guanambi/RGI (Notebook Marimo)
│   └── transform/              # Diretório raiz do projeto dbt (Estrutura Inicial)
│       ├── dbt_project.yml     # Configuração principal do dbt
│       ├── profiles.yml        # Configuração de conexão do dbt (Postgres)
│       └── models/             # Camadas de dados estruturadas do dbt (A ser construído)
│           ├── staging/        # Camada de Staging (limpeza, tipagem e renomeações)
│           ├── intermediate/   # Agregações espaciais e cruzamento de limites
│           └── marts/          # Tabelas fato e dimensão prontas para visualização
├── docker-compose.yml          # Setup rápido do container PostgreSQL/PostGIS (Pronto)
├── pyproject.toml              # Dependências e empacotamento Python (PEP 621)
├── uv.lock                     # Lockfile do gerenciador de pacotes uv
└── README.md                   # Documentação do projeto (este arquivo)
```

---

## 📐 8. Estrutura das Camadas dbt (Modelo Mental)

Durante a fase de transformação com dbt, as tabelas serão estruturadas em três níveis lógicos:

*   **Camada Staging (`models/staging/`)**: Fará a limpeza primária. Padronizará nomes de colunas técnicos da origem em nomes explícitos (ex: converter códigos como `V214` para `area_colhida_hectares`), converterá tipos de dados e assegurará que todas as geometrias estejam no mesmo sistema de projeção espacial (**SIRGAS 2000 / SRID 4674**).
*   **Camada Intermediate (`models/intermediate/`)**: Realizará cruzamentos geográficos intermediários (ex: calcular a intersecção de limites municipais com o polígono oficial da Caatinga para mensurar a porcentagem interna do bioma por município).
*   **Camada Marts (`models/marts/`)**: Consolidação do modelo analítico em formato estrela (tabelas Fato e Dimensão), como por exemplo a futura tabela `fct_agro_desmatamento_correlacao` contendo dados históricos anuais de área colhida, rebanho pecuário, desmatamento acumulado e dados meteorológicos integrados.

---

## 🌍 9. Uso de GeoPandas & PostGIS (Metodologia)

As análises geográficas complexas serão viabilizadas pelo uso conjunto de bibliotecas geoespaciais e funções nativas de banco espacial:

*   **GeoPandas**: Utilizado para ingestão, conversão de arquivos vetoriais locais (GeoPackage, Shapefiles) e envio para o banco usando SQLAlchemy via `to_postgis()`. Também é a principal ferramenta para plotagens coropléticas rápidas e manipulação geométrica em notebooks de exploração.
*   **PostGIS**: No banco, a extensão espacial permitirá consultas espaciais de alta performance e junções baseadas em localização. Um exemplo de query a ser executada no dbt inclui:

```sql
-- Exemplo de query espacial planejada para calcular a área de município interna à Caatinga
SELECT
    mun.id_municipio,
    mun.nome_municipio,
    ST_Area(ST_Intersection(mun.geom, caatinga.geom)) AS area_caatinga_municipio_m2,
    (ST_Area(ST_Intersection(mun.geom, caatinga.geom)) / ST_Area(mun.geom)) * 100 AS pct_area_no_bioma
FROM 
    {{ ref('stg_ibge__municipios_geom') }} mun
INNER JOIN 
    {{ ref('stg_mapbiomas__limite_caatinga') }} caatinga 
ON 
    ST_Intersects(mun.geom, caatinga.geom);
```

---

## 📊 10. Fontes de Dados Planejadas

1.  **IBGE SIDRA** ([Portal](https://sidra.ibge.gov.br)):
    *   **Tabela 9514**: Estimativas de População municipal (Censo/Estimativas).
    *   **Tabela 839**: Produção Agrícola Municipal (PAM) - dados de área colhida e valor de produção.
    *   **Tabela 74**: Pesquisa da Pecuária Municipal (PPM) - evolução histórica do efetivo dos rebanhos.
2.  **MapBiomas** ([Portal](https://mapbiomas.org/)):
    *   Transições anuais de uso e cobertura da terra na Caatinga (1987-2024), detalhando perda de vegetação florestal/savânica para agropecuária.
3.  **INMET (Instituto Nacional de Meteorologia)**:
    *   Dados meteorológicos de estações históricas automáticas (como a de Guanambi) para correlação climática (precipitação pluvial vs produção).

---

## 📈 11. Análises Pretendidas & Insights Esperados

### 🔍 Correlação Espacial (Avanco Agrícola vs Supressão de Vegetação)
O projeto buscará medir espacialmente a taxa de substituição da cobertura vegetal original por pastagens ou lavouras temporárias/permanentes.
*   **Métricas Pretendidas**: `taxa_conversao_anual_vegetacao` (hectares de vegetação nativa convertidos ao ano) e `densidade_bovina_pastagem` (cabeças de rebanho por hectare de pastagem municipal para avaliar índices de degradação).

### 💡 Insights Esperados:
1.  **Vetores de Desmatamento**: Identificar se a pecuária extensiva ou grandes lavouras de commodities representam a maior pressão sobre as florestas secas da região de estudo.
2.  **Influência de Ciclos de Seca**: Avaliar se os surtos de desmatamento se aceleram em anos subsequentes a grandes estiagens, em decorrência da busca por novas áreas úmidas ou produtivas.

---

## 🚀 12. Como Executar o Projeto Localmente (Fase Atual)

### Pré-requisitos
*   [Docker & Docker Compose](https://docs.docker.com/engine/install/) instalados.
*   [uv](https://github.com/astral-sh/uv) instalado (gerenciador de pacotes Python).

---

### Passo 1: Inicializar o Banco de Dados (PostgreSQL/PostGIS)

Suba o container do banco de dados geográfico:

```bash
docker compose up -d
```

O banco será criado e exposto localmente na porta `5433` (mapeada para a porta interna 5432) com as seguintes configurações:
*   **Host**: `localhost`
*   **Porta**: `5433`
*   **User**: `admin`
*   **Password**: `admin123`
*   **Database**: `geo`

---

### Passo 2: Configurar o Ambiente Virtual Python com `uv`

Crie o ambiente virtual e instale as dependências declaradas no `pyproject.toml`:

```bash
uv venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
uv pip install -e .
```

---

### Passo 3: Rodar os Scripts de Extração e Carga (EL)

Para rodar o script que extrai os dados do SIDRA/INMET/Geometrias locais e os insere no banco PostGIS (etapa de carga crua `raw_`):

```bash
python3 src/load.py
```

---

### Passo 4: Explorar os Notebooks Científicos (EDA) com Marimo

Para visualizar as análises de exploração de dados já existentes da Região Geográfica Imediata de Guanambi (RGI) e interagir com gráficos espaciais reativos:

```bash
marimo edit src/notebooks/regiao_gbi.py
```

Siga a URL gerada no terminal (normalmente `http://localhost:8080`) para abrir a interface do Marimo no navegador.

---

### Passo 5: Configurar e Rodar o dbt (Próxima Fase)

Os modelos dbt serão criados na pasta `src/transform/models/`. Uma vez estruturados, a execução seguirá os comandos clássicos:

```bash
cd src/transform

# Testa a conexão configurada com o PostGIS
dbt debug

# Compila e roda os modelos que serão criados
dbt run

# Roda os testes de qualidade a serem definidos nas fontes e modelos
dbt test
```

---

## 📄 13. Licença

Este projeto será de código aberto e disponibilizado sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido por [Maiko André](https://github.com/Maikoandre) como projeto de portfólio profissional de **Geospatial Analytics & Analytics Engineering** em andamento. Feedbacks, sugestões de análises ecológicas e contribuições são muito bem-vindos! 🌵🌎