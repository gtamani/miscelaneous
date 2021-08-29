import gspread, json
import gspread_dataframe as gdf
import pandas as pd


class Gspread_handler():
    def __init__(self):
        try:
            gc = gspread.service_account(filename="credentials.json")
            self.sh = gc.open("Gastos")
            self.tab = self.sh.get_worksheet(0)
        except FileNotFoundError:
            raise Exception("Credentials not found. Make sure to put them in 'credentials.json'")
        
    def update_sheet(self,df):
        """ Update a DataFrame in Google Sheets """
        gdf.set_with_dataframe(self.tab,df,row=1,col=1)

    def load_data(self):
        """ Load DataFrame from Google Sheets """
        data = gdf.get_as_dataframe(self.tab,parse_dates=True,usecols=[x for x in range(4)])
        data = data.dropna()
        data = data.to_dict(orient="index")
        
        d = {}
        for i in range(len(data.values())):
            v = data[i]
            d[i] = [str(x) for x in v.values()]
        return d


if __name__ == "__main__":
    g = Gspread_handler()
    #g.load_data()