import gspread
import gspread_dataframe as gdf
import datetime
import pandas as pd


class Gspread_handler():
    def __init__(self):
        try:
            gc = gspread.service_account(filename="credentials.json")
            self.sh = gc.open("Gastos")
            self.tab = self.sh.get_worksheet(0)
        except FileNotFoundError:
            raise Exception("Credentials not found. Make sure to put them in 'credentials.json'")
        
    def update_sheet(self,data):
        """ Update a DataFrame in Google Sheets """
        df = pd.DataFrame(data)
        df.columns = ["Fecha","Categoría","Concepto","Monto"]
        gdf.set_with_dataframe(self.tab,df,row=1,col=1)

    def load_data(self):
        """ Load DataFrame from Google Sheets """
        data = gdf.get_as_dataframe(self.tab,parse_dates=True,usecols=[x for x in range(4)])
        data = data.dropna()
        data = data.to_dict(orient="index")
        
        d = []
        for i in range(len(data.values())):
            v = data[i]
            d.append([str(x) for x in v.values()])
        return d

    def update_cell(self,cell,content):
        self.tab.update_acell(cell,content)


class Main_sheet():
    def __init__(self):
        
        gc = gspread.service_account(filename="credentials.json")
        self.sh = gc.open("Gastos desde Ago2018")
        
        self.aux = {
            "total_spendings":"G1",
            "total_income":"G2"
        }

        self.update_month(2021,9)

    def update_month(self,year,month):
        base = datetime.datetime(2021,1,28)
        analized = datetime.datetime(year,month,28)
        dif = (analized.year * 12 + analized.month) - (base.year * 12 - base.month) - 3
        
        self.main = {
            "total_spendings":"AB"+str(33+dif),
            "total_income":"AC"+str(33+dif)
        }

    def update_spending_sheet(self,spendings,income):
        """ Update spending sheet """
        tab = self.sh.get_worksheet(2)
        tab.update_acell(self.main["total_spendings"],spendings)
        tab.update_acell(self.main["total_income"],income)

if __name__ == "__main__":
    g = Gspread_handler()
    g.load_data()


    
    