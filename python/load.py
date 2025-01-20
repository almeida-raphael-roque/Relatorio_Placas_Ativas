import logging
import openpyxl
import shutil
import os
import traceback
from transform import Transform

def import_df_final():

    df_final = Transform.transforming_df_final()
    return df_final

def import_df_all_placas():

    df_placas_atual= Transform.transforming_df_all_placas()
    return df_placas_atual

class Load_relat_ativ_pend:

    def __init__(self) -> None:
        pass


    def load_files():

        try:

            df_final = import_df_final()
            df_placas_atual = import_df_all_placas()

            save_path = r'C:\Users\raphael.almeida\Documents\Ativações Placas\Relatório de Placas Ativadas'
            df_final_name = 'Movimentação de placas.xlsx'
            df_all_placas_name = 'Relação total de placas.xlsx'

            path1 = os.path.join(save_path, df_final_name)
            path2 = os.path.join(save_path, df_all_placas_name)
            
            df_final.to_excel(path1, index=False, engine='openpyxl')
            df_placas_atual.to_excel(path2, index=False, engine='openpyxl')

            #salvando no sharepoint
            share = r'C:\Users\raphael.almeida\Grupo Unus\analise de dados - Arquivos em excel'
            share_path1 = os.path.join(share, os.path.basename(path1))
            share_path2 = os.path.join(share,os.path.basename(path2))

            shutil.copy(path1,share_path1)
            shutil.copy(path2,share_path2)


            logging.info('\n ----------------------------------------------------------------------------------')
            logging.info('\n Processo de Carregamento de Dados concluido com sucesso!')

        except Exception as e:

            logging.info('\n ----------------------------------------------------------------------------------')
            logging.info(f'\n Falha ao Carregar Relatorio Final: {e}')
            logging.info(traceback.format_exc())

if __name__ == '__main__':

    Load_relat_ativ_pend.load_files()
