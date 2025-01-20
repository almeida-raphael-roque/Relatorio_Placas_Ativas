# Projeto Relatório de Placas Ativadas

## 1) Objetivo Principal do Relatório

- O principal objetivo do relatório é acompanhar dois tipos de informação: a movimentação de placas entre as 3 cooperativas existentes e a respectiva quantidade total de placas ativas 

    - Ambas informações são analisadas em um contexto de dia anterior;
    - A atualização do relatório é diária.

<br>

1) As possíveis situações entre as movimentações de placas  são descritas como: "Novas", "Renovadas", "Migração" e "Canceladas"

    - Todas são analisadas entre as 3 cooperativas e também como acumulado geral

<br>

2) A outra parte da análise é verificar quantas placas ativas existem nas três cooperativas e no total geral 

<br>

## 2) Objetivo Principal do Projeto

- O relatório já existia previamente, porém seus processos eram demorados e ineficientes. Ademais, haviam equívocos e redundâncias de análise nas três frentes de construção: 
    - nas consultas em SQL (queries);
    - no ETL em Python;
    - no tratamento e modelagem de dados no Power Query e nas métricas em DAX, respectivamente.

- Logo, o objetivo principal do projeto é **tornar efetivo o relatório de acompanhamento de placas**. 
    
    - Efetividade se traduz em torná-lo eficiente (performático e organizado) e eficaz (analisa os dados corretamente)

<br>

## 3) Escopo do Projeto

    Problemática

1) **Consulta em SQL (query)**
- não constavam informações de cancelamentos, essa informações dependiam de uma planilha em excel preenchida de maneira manual, logo havia vários dias em que não constavam informações ou que haviam dados fora do padrão

- haviam _joins_ que não estavam sendo utilizados nas colunas;

- a antiga query utilizada para posterior composição de informações de migrações (listagem_mestra) não estava ordenada por data, tendo como efeito, na composição, o equívoco de não pegar o status mais atualizado da placa;

- essa mesma query também não estava paralela às outras consultas, visto que considerava a data atual em seu script, o que é um erro pois o relatório analisa sempre o dia anterior.

<br>

2) **ETL em Python**
- o Transform continha repetição de funções entre cooperativas que já haviam sido escritas, deixando a outra cooperativa sem tratamento;

- o Load atualizava informações de maneira incremental, não considerando a movimentação de placas, logo as primeiras composições da tabela depois de um tempo ficavam consequentemente desatualizadas, e mesmo assim compunham o resultado final geral de placas

<br>

3) **Tratamento e Modelagem de Dados (Power BI)**
- o tratamento em Power Query era redundante pois filtrava informações do relatório gerado e o espelhava na tabela "f_vendas", filtrando-a pela "placa", porém essa mesma tabela tem o princípio de construção muito semelhante ao do relatório, o que gerava redução significativa na performance de atualização do dashboard e perda de dados originais;

- a modelagem em dados, apesar de correta continha informações demais, métricas desorganizadas e colunas calculadas que dificultavam não só a performance do dashboard, mas também prejudicando a rastreabilidade e manutenção do relatório e do correto fluxo de informações.

<br><br>


    Soluções

1) **Consulta em SQL (query)**
- foi acrescentada um consulta em SQL para pegar as informações de placas no status 'cancelado' diretamente da base de dados;

- os _joins_ inutilizados foram removidos;

- criou-se uma nova query "placas_total_ordem" ordenada por data, agora o status mais atual das placas foi contemplado corretamente;

- desconsiderou-se, nessa mesma query, a data atual em seu script, pois o relatório analisa sempre o dia anterior;

- para a melhora do script, tanto em SQL quanto em Python, aglutinou-se as queries por cooperativa em uma query só, que as diferencia por cooperativa.

<br>

2) **ETL em Python**
- os equívocos já apresentados na problemática do Transform foram corrigidos, as devidas alterações para o acréscima da query de cancelamentos também foram realizadas;

- no Transform, também foi acrescentado uma consulta para composição de relatório apenas com placas com os status mais atuais, que é o correto a se analisar como um todo;

- o Load gera duas bases, uma que retorna o status atual de placas (considerando apenas as que foram atualizadas no âmbito diário), e outra que retorna o total geral de placas com o respectivo status corretamente atualizado agora.

<br>

3) **Tratamento e Modelagem de Dados (Power BI)**
- o tratamento em Power Query foi simplificado, há agora apenas duas fontes de dados oriundas do SharePoint; 

- as métricas foram organizadas e consequentemente diminuídas, resultando em maior rastrabilidade, coerência e performance do dashboard.
 


<br><br>


    Resultados

1) O incremento da informação de placas canceladas diretamente da base de dados diminuiu os erros humanos e tornou a atualização rápida, diária e correta;

2) A aglutinação das consultas por _UNION ALL_ deixou as consultas em SQL e o código mais organizado e "limpo";

3) A correta ordenação da query que pega o total de placas pela data de ativação (bem como os demais ajustes realizados) tornou possível retornar placas apenas com o status mais atualizado, solucionando o problema de desatualização de placas que constavam no relatório final;

4) Todos os equívocos no código ETL em python foram corrigidos;

5) Por gerar duas bases de dados, uma para movimentação de placas e a outra para composição total de placas simplificou-se o posterior tratamento dos dados no Power Query;

6) Todas as alterações permitiram a construção de um dashboard muito mais organizado, "leve" e coerente com a real situação das placas.

7) Todas as etapas estão organizadas e limpas para entendimento e rastreabilidade

8) Os passos somados levaram a reduzir o tempo de atualização do relatório completo de 20 minutos (15' Power BI + 5' Python) para 2' 30", total. Uma redução de 87,5% no tempo total gasto para atualizar;

9) O relatório final contempla a correta situação de placas nas 3 cooperativas.

10) A gerência e diretoria conseguem analisar com segurança e confiabilidade a situação de placas na empresa, tomar melhores decisões se baseando no relatório disponibilzado e, consequentemente, aumentar o faturamento da empresa. 

<br><br>

    Próximas Etapas

1) Comentar as linhas de código para gestão do conhecimento;

2) Evidenciar, no dashboard, que a diferença entre resultados diários na métrica "Placas carteira dia atual", do dia anterior, "Placas carteira dia anterior", do dia atual, se dá em função da mudança de status de placas de ativos para outros status disponíveis.