import pandas as pd

customer_calls = pd.read_excel('17-01-2019 263951.xlsx')


customer_calls["Date Of Birth"] = pd.to_datetime(customer_calls["Date Of Birth"]).dt.strftime("%Y-%m-%d")
customer_calls.to_excel("17-01-2019 263951_YYYY_MM_DD.xlsx")