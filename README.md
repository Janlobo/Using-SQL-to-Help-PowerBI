# Using-SQL-to-Help-PowerBI
## Get rid of useless information from your semantic model. How to reduce a Power BI file from 2 GB to 28 MB. ##

In a recent data analysis study to understand how federal deputies in Brazil spend their parliamentary quota (Study published on my LinkedIn at https://www.linkedin.com/posts/janlobo_um-bilh%C3%A3o-de-reais-paraqu%C3%AA-mesmo-activity-7281818691871080451-3PXC?utm_source=social_share_send&utm_medium=member_desktop_web )<br>
I had to use a database of CNPJs (identification of Brazilian companies) extracted from the website of the Brazilian Federal Revenue Service, which contained, at the time, almost 63 million records.<br>
This data was used in the federal deputies' spending dashboard, where I categorized the expenses by the activity of the company providing the services.<br>
This caused a considerable increase in the database and left the PowerBI file with almost 2GB in size.<br>

<b>The solution I found was as follows:</b>
1. I used the PostGreSQL database as a source of work and information cleaning
2. I used Fábio Serpa's guidelines to extract all the CNPJ information. ( https://github.com/fabioserpa/CNPJ-full )
3. I created a code in Python that reads the Federal Deputies' Expenses files for 2023 and 2024 on the Open Data website of the Chamber of Deputies ( https://dadosabertos.camara.leg.br/ ), which creates the tables in PostGreeSQL and loads the data. 4. In PostGree, I created a SQL to join the 2 downloaded quota databases from 2023 and 2024 (Criacao_Tabela_unificada_CNPJs.sql)
5. I created a View with several JOINs to search for additional CNPJ data and cross-reference it with the CNPJs that exist in the Federal Deputies' expenditure table. This way, the CNPJs that are not in the quota table will be disregarded. This reduced the number of rows from almost 63 million to 30 thousand rows.
6. Returning to Power BI, I obtain the data by referencing this view.

   --------------------------------------------------

Em um estudo recente de analise de dados para entender como os deputados federais no Brasil gastam sua cota parlamentar (Estudo publicado no meu linkedin em https://www.linkedin.com/posts/janlobo_um-bilh%C3%A3o-de-reais-paraqu%C3%AA-mesmo-activity-7281818691871080451-3PXC?utm_source=social_share_send&utm_medium=member_desktop_web )<br>
Tive que utilizar uma base de CNPJs (identificação de empresas brasileiras) extrair do site da Receita Federal do Brasil no qual continha, na época, quase 63 milhões de registros.<br>
Esses dados foram utilizados no painel de gastos dos deputados federais onde categorizei os gastos pela atividade da empresa fornecedora dos serviços.<br>
Isso causou um aumento considerável na base de dados e deixou o arquivo do PowerBI com quase 2GB de tamanho.<br>

<b>A Solução que encontrei foi a seguinte:</b>
1. Utilizei o banco de dados PostGreSQL como fonte de trabalho e limpeza das informações
2. Utilizei as orientações do Fábio Serpa para realizar a extração de todas as informações de CNPJs. ( https://github.com/fabioserpa/CNPJ-full ) 
3. Criei um código em Python que lê os arquivos de Gastos dos Deputados Federais de 2023 e 2024 no site de Dados Abertos da Camara dos Deputados ( https://dadosabertos.camara.leg.br/ ), o qual cria as tabelas no PostGreeSQL e realiza a carga dos dados.
4. No PostGree criei um sql para unir as 2 bases de cotas baixadas de 2023 e 2024 (Criacao_Tabela_unificada_CNPJs.sql) 
5. Criei uma View com vários JOINs para buscar dados complementares do CNPJ e cruzar com os CNPJs existentes na tabela de gastos dos Deputados federais. Desta forma, os CNPJs que não estão na tabela de cotas serão desconsiderados. Isso reduziu de quase 63 milhões de linhas para 30 mil linhas.
6. Retornando ao Power BI faço a obtenção dos dados fazendo referência a essa view.
