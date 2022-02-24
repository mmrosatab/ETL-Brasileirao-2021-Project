# ETL-Brasileirao-2021-Project

Application for build ETL with Brasileirão 2021 data

<div style="text-align: justify; padding: 1%;">
  The purpose this application is build basic ETL program with data from globo esporte website. The data consists in information of Brasileirão 2021. The first step was get the data by scraping for to construct csv files.
</div>

#### Steps

<div style="text-align: justify; padding: 1%;">
  The first step was get the data by scraping for to construct csv files. The recovered data are: 'Gol marcado','Gols sofridos','Gols contra', 'Gols de falta',
              'Gol de pênalti', 'Gols dentro da área', 'Gol de fora da área', 'Finalização na trave', 'Finalizações para fora', 'Faltas recebidas', 'Faltas cometidas', 'Impedimentos', 'Cartões amarelos', 'Cartões vermelhos', 'Defesas difíceis', 'Defesas de pênaltis', 'Roubadas de bola','Passes errados'
</div>

- This data can be found in :

  - https://interativos.globoesporte.globo.com/estatisticas/times/

  - <img src="Images/teams.png" width="400" height="200">

#### Todo List

- [x] Extract Process
  - [x] Web Scrapping with data globo esporte website
- [ ] Transform
- [ ] Load
  - [ ] Load data in relational database
- [ ] Create dashboard and charts
