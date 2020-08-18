import os
import logging
import creopyson
import sys
import tkinter
import xlrd

# Path to folder where excel files are located.
global path
path = "C:\\Users\\ZovinecJ\\Desktop\\listy\\"

try:
    os.remove("list_grupy.log")
    os.remove("existing.txt")
    os.remove("non_existing.txt")
except:
    pass

logging.basicConfig(filename="list_material_numbers_from_excel_sheets.log", level=logging.INFO)
logger = logging.getLogger()


def creoson_setup():

    """This function connects this application to PTC Creo session via Creoson"""

    global creo_client
    creo_client = creopyson.Client()
    try:
        creo_client.connect()
        print('Creoson is running')
        logger.info('Creoson is running')
    except ConnectionError:
        creoson_folder = os.path.dirname(sys.argv[0]) + '\\creoson'
        os.startfile(creoson_folder)
        tkinter.messagebox.showinfo("Kraussmaffei Assembly Automation", "Creoson is not running. Start Creoson before starting Automation app.")
        logger.critical("Kraussmaffei Assembly Automation", "Creoson is not running. Start Creoson before starting Automation app.")
        exit()


def list_all_excels():

    """Function which will lists all excel files in path folder."""

    lists = []
    for f in os.walk(path):
        for fileX in f:
            print(fileX)
        for each in fileX:
            print(each)
            lists.append(each)
    return lists


def lists_all_sheets_in_opened(excel_file):

    """Function to list all sheets in argument excel file."""

    path_to_file = path+excel_file
    current_workbook = xlrd.open_workbook(path_to_file)
    return current_workbook.sheet_names()


def inspect_cells_of_sheet_and_determine_model_existence(excel_file, worksheet):

    """Function which inspects every single cell of excel sheet. Cell content is checked whether is possible material number.
    If yes, material number is extended by assembly model extension (.asm) and is determined whether such 3d model exists in database."""

    path_to_file = path + excel_file
    input_workbook = xlrd.open_workbook(path_to_file)
    input_worksheet = input_workbook.sheet_by_name(worksheet)
    num_cols = input_worksheet.ncols  # Number of columns
    for row_idx in range(0, input_worksheet.nrows):  # Iterate through rows
        for col_idx in range(0, num_cols):  # Iterate through columns
            cell_obj = input_worksheet.cell(row_idx, col_idx)  # Get cell object by row, col
            text_cel = str(cell_obj)
            if 'number:' in text_cel[0:7]:
                mat = text_cel.replace('number:', '')
                # conversion of cell content
                mat = float(mat)
                mat = int(mat)
                mat = str(mat)
                # Length of material number
                if 6 < len(mat) < 9:
                    mat = mat + '.asm'
                    try:
                        existing_material_numbers = open("existing.txt", "a")
                        creopyson.file_open(creo_client, file_=mat)
                        existing_material_numbers.write(mat + '\n')
                        existing_material_numbers.close()
                    except:
                        non_existing = open("non_existing.txt", "a")
                        non_existing.write(mat+'\n')
                        non_existing.close()


if __name__ == "__main__":

    creoson_setup()
    for each_excel in list_all_excels():
        for each_sheet in lists_all_sheets_in_opened(each_excel):
            inspect_cells_of_sheet_and_determine_model_existence(each_excel, each_sheet)
