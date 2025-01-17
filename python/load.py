import logging
import openpyxl
import shutil
import os
import traceback

def import_df_final():

    from transform import Transform
    df_final = Transform.transforming_files()

    return df_final

class Load_relat_ativ_pend:

    def __init__(self) -> None:
        pass


    def load_files():

        try:

            df_final = import_df_final()

            template = r'C:\Users\raphael.almeida\Documents\Ativações Placas\report\ACOMPANHAMENTO_ATIVACOES.xlsx'

            wb = openpyxl.load_workbook(filename=template)

            ws1 = wb['ATIVAÇÕES']

            def get_last_row(sheet):
                for row in reversed(range(1, sheet.max_row + 1)):
                    for col in range(1, sheet.max_column + 1):
                        if sheet.cell(row=row, column=col).value is not None:
                            return row
                return 1

            # Encontrar a última linha não vazia em cada aba
            last_row_ws1 = get_last_row(ws1)

            # Adicionar dados em 'SEGTUCK & STCOOP'
            for r_idx, row in enumerate(df_final.values, last_row_ws1 + 1):
                for c_idx, value in enumerate(row, 2):  # Coluna começa em 1
                    ws1.cell(row=r_idx, column=c_idx, value=value)

            wb.save(r'C:\Users\raphael.almeida\Documents\Ativações Placas\report\ACOMPANHAMENTO_ATIVACOES.xlsx')
            wb.close()

            # PASSANDO ARQUIVO PARA O DIRETÓRIO DO SHAREPOINT
            file_path = r'C:\Users\raphael.almeida\Documents\Ativações Placas\report\ACOMPANHAMENTO_ATIVACOES.xlsx'
            destination_dir  = r'C:\Users\raphael.almeida\Grupo Unus\analise de dados - Arquivos em excel'
            destination_path = os.path.join(destination_dir, os.path.basename(file_path))
            shutil.copy(file_path, destination_path)

            logging.info('\n ----------------------------------------------------------------------------------')
            logging.info('\n Processo de Carregamento de Dados concluido com sucesso!')

        except Exception as e:

            logging.info('\n ----------------------------------------------------------------------------------')
            logging.info(f'\n Falha ao Carregar Relatorio Final: {e}')
            logging.info(traceback.format_exc())

if __name__ == '__main__':

    Load_relat_ativ_pend.load_files()
