# IMPORTANDO BIBLIOTECAS E PACOTES
import awswrangler as awr
import logging


logging.info('\n ----------------------------------------------------------------------------------')
logging.info('\n Executando Rotina - RELATÓRIO DE PLACAS ATIVADAS')

class Extract:
    def __init__(self) -> None:
        pass
    
    def extract_ativacoes():

        try:

            dir_query = r'C:\Users\raphael.almeida\Documents\Ativações Placas\Relatório de Placas Ativadas\sql\placas_novas.sql'

            with open(dir_query, 'r') as file:
                query = file.read()

            df_ativ = awr.athena.read_sql_query(query,database='silver')
        
            logging.info('\n ----------------------------------------------------------------------------------')
            logging.info('\n Relatorio ativacoes de placas novas  - Dados Extraidos com sucesso!')

            return df_ativ

        except Exception as e:

            logging.info('\n ----------------------------------------------------------------------------------')
            logging.info(f'\n Falha ao Extrair relatorio ativacoes (Viavante): {e}')


    def extract_renovacoes():

        try:

            dir_query = r'C:\Users\raphael.almeida\Documents\Ativações Placas\Relatório de Placas Ativadas\sql\placas_renovadas.sql'

            with open(dir_query, 'r') as file:
                query = file.read()

            df_renov = awr.athena.read_sql_query(query, database='silver')
        
            logging.info('\n ----------------------------------------------------------------------------------')
            logging.info('\n Relatorio renovacoes (Vivante)  - Dados Extraidos com sucesso!')

            return df_renov

        except Exception as e:

            logging.info('\n ----------------------------------------------------------------------------------')
            logging.info(f'\n Falha ao Extrair relatorio renovacoes (Viavante): {e}')


    def extract_cancelamentos():

        try:

            dir_query = r'C:\Users\raphael.almeida\Documents\Ativações Placas\Relatório de Placas Ativadas\sql\placas_canceladas.sql'

            with open(dir_query, 'r') as file:
                query = file.read()

            df_cancel = awr.athena.read_sql_query(query, database='silver')
        
            logging.info('\n ----------------------------------------------------------------------------------')
            logging.info('\n Relatorio renovacoes (Vivante)  - Dados Extraidos com sucesso!')

            return df_cancel

        except Exception as e:

            logging.info('\n ----------------------------------------------------------------------------------')
            logging.info(f'\n Falha ao Extrair relatorio renovacoes (Viavante): {e}')


    def extract_conf_migracoes():

        try:

            dir_query = r'C:\Users\raphael.almeida\Documents\Ativações Placas\Relatório de Placas Ativadas\sql\placas_total_ordem.sql'

            with open(dir_query, 'r') as file:
                query = file.read()

            df_migracoes_placas = awr.athena.read_sql_query(query, database='silver')
        
            logging.info('\n ----------------------------------------------------------------------------------')
            logging.info('\n Relatorio renovacoes(Stcoop)  - Dados Extraidos com sucesso!')

            logging.info('\n ----------------------------------------------------------------------------------')
            logging.info('\n Processo de Extracao de Dados concluido com sucesso!')

            return df_migracoes_placas

        except Exception as e:

            logging.info('\n ----------------------------------------------------------------------------------')
            logging.info(f'\n Falha ao Extrair relatorio renovacoes (Stcoop): {e}')


    


    






