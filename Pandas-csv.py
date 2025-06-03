import pandas as pd

## Old Data
data = {"Name":["Mihan","Moon","Mim"],
        "Profeson":["Student","HousWife","Doctor"],
        "Salarry":[50000,10000,200000]}

## Make it a csv file
sheet = pd.DataFrame(data)
sheet.to_csv("Family_Data.csv",index=False)


###    NOW, TRY TO ADD NEW DATA IN THIS OLD CSV FILE   ###

## open old csv file as DataFrame
file = pd.read_csv("Family_Data.csv")

## New data and convert it into DataFrame
new_data = {"Name":["Aysha"],"Profeson":["HouseWife"],"Salarry":[15000]}
new_file = pd.DataFrame(new_data)

## Connect both old and new DataFrame with [ concat ] function
new_file = pd.concat([file, new_file],ignore_index=True) ## ignore_index=True >> it is mandetory otherwise its start new index from new added data

## write it as a csv file
new_file.to_csv("Family_Data_updated.csv",index=False)
