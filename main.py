import eikon
import pandas as pd
eikon.set_app_key('YOUR_APP_KEY')

def retrieve_bond_yield_data(start_date, end_date):
    bond_yield_data = pd.DataFrame({
        'Date': pd.date_range(start=start_date, end=end_date),
        'US_1Y': [0.02] * len(pd.date_range(start=start_date, end=end_date)),
        'US_4Y': [0.03] * len(pd.date_range(start=start_date, end=end_date)),
        'US_10Y': [0.04] * len(pd.date_range(start=start_date, end=end_date)),
        'US_30Y': [0.05] * len(pd.date_range(start=start_date, end=end_date))
    })
    return bond_yield_data

def clean_data(data):
    cleaned_data = data.dropna() 
    return cleaned_data

if __name__ == "__main__":
    start_date = '1995-01-01'
    end_date = '2024-04-13'
    bond_yield_data = retrieve_bond_yield_data(start_date, end_date)
    cleaned_data = clean_data(bond_yield_data)
