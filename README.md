# 🌵 Expansão Agrícola e Impacto Ambiental na Caatinga

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)

## 🗺️ 1. Introdução

A **Caatinga** ocupa cerca de 10% do território nacional e abriga uma rica biodiversidade adaptada ao clima semiárido. Contudo, frentes de expansão agrícola e pecuária têm avançado sobre suas florestas secas. Este avanço, muitas vezes desordenado, causa fragmentação de habitats, perda de solo e acelera processos de desertificação.

Este projeto analisará a relação entre a expansão das atividades agrícolas/pecuárias e a supressão de vegetação nativa no bioma **Caatinga**, um ecossistema exclusivamente brasileiro e altamente vulnerável à desertificação.

## 🎯 2. Objetivos do Projeto

*   📈 **Análise Temporal da Expansão Agrícola**: Mapear o crescimento da área colhida e a evolução da pecuária nos municípios da Caatinga ao longo do tempo.
*   🌳 **Monitoramento da Supressão Vegetal**: Analisar as mudanças de cobertura vegetal nativa e quantificar as áreas convertidas em pastagem ou agricultura.
*   🔍 **Correlação Espacial e Temporal**: Cruzar estatísticas agrícolas do IBGE com dados de uso e cobertura do solo para identificar hotspots de desmatamento impulsionados por commodities específicas.
*   🗺️ **Visualização Geoespacial**: Gerar mapas interativos e painéis analíticos que facilitem a interpretação visual dos vetores de desmatamento.
*   🏗️ **Engenharia de Dados Moderna**: Consolidar um pipeline estruturado e versionado de dados geográficos usando as melhores práticas de Analytics Engineering (ELT, dbt, modelagem modular e testes).

## ❓ 3. Perguntas Principais

O projeto buscará responder às seguintes perguntas:
1.  **Quais municípios da Caatinga apresentarão a maior taxa de conversão de vegetação nativa em áreas agrícolas nos últimos anos?**
2.  **Existe uma correlação direta entre o aumento do rebanho bovino/área colhida de grãos e a perda de florestas secas na Caatinga?**
3.  **Como as anomalias de precipitação (dados de clima do INMET) se relacionarão com as perdas agrícolas e o avanço da fronteira em áreas marginais?**
4.  **Quais microrregiões geográficas apresentarão maior risco ecológico imediato devido ao avanço da infraestrutura agropecuária?**

## 🏗️ 4. Arquitetura do Projeto (Planejada)

O fluxo de dados seguirá a filosofia **ELT moderna**, onde a extração e a carga serão feitas em Python, e toda a modelagem geométrica e transformações serão delegadas ao banco de dados utilizando **dbt** e **PostGIS**.

<p align="center">
  <img src="assets/Untitled-2026-05-13-0814.png" alt="Arquitetura do Projeto" width="100%">
</p>

## 🛠️ 5. Stack Tecnológica

*   **Linguagem Principal**: [Python 3.11+](https://www.python.org/)
*   **Ingestão de Dados**: [Pandas](https://pandas.pydata.org/) & [GeoPandas](https://geopandas.org/) (carga geométrica inicial via SQLAlchemy/GeoAlchemy2)
*   **Interface de APIs**: [Sidrapy](https://github.com/AlanTaranti/sidrapy) (Cliente oficial da API SIDRA do IBGE)
*   **Interface de Notebooks**: [Marimo](https://marimo.io/) (Notebooks analíticos reativos salvos em `.py` puro)
*   **Banco de Dados**: [PostgreSQL 16+](https://www.postgresql.org/) com extensão espacial [PostGIS 3+](https://postgis.net/)
*   **Transformação e Modelagem**: [dbt-core](https://www.getdbt.com/) com adaptador `dbt-postgres` (a ser implementado)
*   **Infraestrutura**: [Docker & Docker Compose](https://www.docker.com/) (Instanciação do banco PostGIS e Metabase)

## 📊 6. Fontes de Dados Planejadas

1.  **IBGE SIDRA**:
    *   **Tabela 9514**: Estimativas de População municipal (Censo/Estimativas).
    *   **Tabela 839**: Produção Agrícola Municipal (PAM) - dados de área colhida e valor de produção.
    *   **Tabela 74**: Pesquisa da Pecuária Municipal (PPM) - evolução histórica do efetivo dos rebanhos.
2.  **MapBiomas**:
    *   Transições anuais de uso e cobertura da terra na Caatinga (1987-2024), detalhando perda de vegetação florestal/savânica para agropecuária.
3.  **INMET (Instituto Nacional de Meteorologia)**:
    *   Dados meteorológicos de estações históricas automáticas (como a de Guanambi) para correlação climática (precipitação pluvial vs produção).

## 🔮 7. Progresso do Projeto & Próximos Passos

O desenvolvimento do projeto é feito de forma estruturada e incremental. Abaixo está a lista detalhada do que está planejado para as próximas etapas:

- [ ] **Modelagem dbt Completa**: Desenvolver todas as queries SQL modulares de Staging (`models/staging/`) para limpar, tipar e normalizar as tabelas de origem bruta na pasta do projeto dbt.
- [ ] **Cruzamentos Espaciais no dbt**: Codificar queries analíticas geográficas intermediárias (`models/intermediate/`) usando as funções espaciais do PostGIS (como intersecções `ST_Intersection` e cálculo de áreas de vegetação).
- [ ] **Tabelas de Fato e Dimensões (Marts)**: Estruturar as tabelas analíticas finais (`models/marts/`) agregando as métricas históricas de produção agrícola/pecuária integradas com o histórico de supressão vegetal municipal.
- [ ] **Configuração do Metabase**: Adicionar a imagem do Metabase ao arquivo `docker-compose.yml`, conectá-la ao banco de dados e construir painéis/gráficos geoespaciais integrados com as geometrias dos municípios da Caatinga.

---

Desenvolvido por [Maiko André](https://github.com/Maikoandre) como projeto de portfólio profissional de análise geoespacial. Feedbacks, sugestões de análises ecológicas e contribuições são muito bem-vindos! 🌎