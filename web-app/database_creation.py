import sqlite3
import pandas as pd 


con = sqlite3.connect('exoplanet.db')
c = con.cursor()
c.execute('''DROP table exoplanet_table''').fetchall()



df = pd.read_csv("../cumulative_2021.csv")

df.to_sql("exoplanet_table", con=con)

