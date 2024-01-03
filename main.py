from register import register_page
from address_complete import add_address
import time

########    FAIL/OK STATUS OUTPUT > data.xlsx  ###########
def complete_check(row,accept):
    try:
        import openpyxl
        xfile = openpyxl.load_workbook('data_ex.xlsx')

        sheet = xfile.get_sheet_by_name('Sheet1')
        if accept == 1:
            sheet[f'K{row}'] = 'OK'
        elif accept == 0:
            sheet[f'K{row}'] = 'FAIL'




        xfile.save('data_ex.xlsx')
    except Exception as err:
        print("fail to updata complete status", err)

########    GET THE DATA  ###########
def excel_get_data():

    try:

        import pandas as pd
        df = pd.read_excel("data_ex.xlsx")
        for index, row in df.iterrows():
            #that is for OK and FAIL
            idx = index+2
            email = row["email"]
            password = row["password"]
            name = row["name"]
            last = row["last"]
            phone = row["phone"]
            province = row["province"]
            district = row["district"]
            street = row["street"]
            address = row["address"]
            address_name = row["address_name"]

            try:

                driver = register_page(email,password)
                time.sleep(2)
                data = {"name":name,
                        "last": last,
                        "phone":phone,
                        "province":province,
                        "district":district,
                        "street":street,
                        "address":address,
                        "address_name":address_name}


                add_address(driver, data=data)

                complete_check(idx,1)
            except Exception as err:
                complete_check(idx, 0)
                print("fail to register or add_address", err)


    except Exception as err:

        print("fail to get data from excel file",err)


excel_get_data()
