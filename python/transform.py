import pandas as pd
import numpy as np
import datetime as dt
from extract import Extract
import logging
import traceback
import numpy as np

class Transform:
        
    def __init__(self) -> None:
        pass

    def transforming_files():

        try:

            df_ativ = Extract.extract_ativacoes()
            df_renov = Extract.extract_renovacoes()
            df_mig_all_placas = Extract.extract_conf_migracoes()


            # CRIANDO DATAFRAME FINAIL VIAVANTE (VERIFICANDO RENOVAÇÕES)
            if not df_renov.empty:
                df_renov['status'] = 'RENOVAÇÃO'
                df_final = pd.concat([df_ativ, df_renov])

            else:

                df_final = df_ativ

        except Exception as e:

            logging.info('\n ----------------------------------------------------------------------------------')
            logging.info(f'Falha ao atualizar placas referente às renovações: {e}')

        try:

            # CRIANDO DATAFRAME FINAIL VIAVANTE (VERIFICANDO MIGRAÇÕES)

            # CRIANDO COLUNA DE MIGRAÇÃO (MIGRATION_FROM)
            df_final['migration_from'] = None


            # ATUALIZANDO MIGRAÇÕES DE PLACAS (SEGTRUCK & STCOOP ---> VIAVANTE)
            for idx, row in df_final.iterrows():
                
                df_filtred = df_mig_all_placas[
                    (df_mig_all_placas['placa'] == row['placa']) |
                    (df_mig_all_placas['chassi'] == row['chassi'])
                ]

                if not df_filtred.empty and len(df_filtred['empresa'].values) > 1:

                    if df_filtred['empresa'].values[1] != row['empresa']:
                        df_final.at[idx, 'status'] = 'MIGRAÇÃO'

                        if df_filtred['empresa'].values[1] == 'Segtruck':
                            df_final.at[idx, 'migration_from'] = 'Segtruck'

                        elif df_filtred['empresa'].values[1] == 'Stcoop':
                            df_final.at[idx, 'migration_from'] = 'Stcoop'
                        else:
                            df_final.at[idx, 'migration_from'] = 'Viavante'
                else: 
                    df_final.at[idx, 'migration_from'] = 'NULL' 
     
            logging.info('\n ----------------------------------------------------------------------------------')
            logging.info(f' Processo de atualização de status de placas migradas realizado com sucesso!')
        
        except Exception as e:

            logging.info('\n ----------------------------------------------------------------------------------')
            logging.info(f'Falha na atualização de status de placas migradas: {e}')
            logging.info(traceback.format_exc())


        try:

            # TRANSFORMANDO O STATUS 'ATIVO' EM 'NOVO'
            df_final.loc[df_final['status'] == 'ATIVO', 'status'] = 'NOVO'

        except Exception as e:

            logging.info('\n ----------------------------------------------------------------------------------')
            logging.info(f'Falha ao unir os dataframes: {e}')
            logging.info(traceback.format_exc())
            
        try:

            df_final['placa'] = df_final['placa'].fillna('SEM-PLACA')
            df_final['chassi'] = df_final['chassi'].fillna('NULL')
            df_final['id_placa'] = df_final['id_placa'].fillna(0)
            df_final['id_veiculo'] = df_final['id_veiculo'].fillna(0)
            df_final['id_carroceria'] = df_final['id_carroceria'].fillna(0)
            df_final['matricula'] = df_final['matricula'].fillna(0)
            df_final['conjunto'] = df_final['conjunto'].fillna(0)
            df_final['unidade'] = df_final['unidade'].fillna('NULL')
            df_final['status'] = df_final['status'].fillna('NULL')
            df_final['cliente'] = df_final['cliente'].fillna('NULL')
            df_final['data'] = df_final['data'].fillna(pd.Timestamp('1900-01-01'))
            df_final['data_ativacao'] = df_final['data_ativacao'].fillna(pd.Timestamp('1900-01-01'))
            df_final['suporte'] = df_final['suporte'].fillna('NULL')
            df_final['data_filtro'] = df_final['data_filtro'].fillna(pd.Timestamp('1900-01-01'))
            df_final['empresa'] = df_final['empresa'].fillna('NULL')
            df_final['migration_from'] = df_final['migration_from'].fillna('NULL')

            
            # df_final = df_final.fillna('NULL')

            logging.info('\n ----------------------------------------------------------------------------------')
            logging.info('\n Processo de Transformacao de Dados concluido com sucesso!')

        except Exception as e:

            logging.info('\n ----------------------------------------------------------------------------------')
            logging.info(f'Falha ao realizar tratamento de dados: {e}')
            logging.info(traceback.format_exc())

        return df_final
        



