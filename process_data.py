import json
import pandas as pd


with open(r'data\unique_authors_list_full.json') as json_file: 
    unique_authors = json.load(json_file) 
with open(r'data\n_unique_authors_full.json') as json_file: 
    n_unique_authors = json.load(json_file) 

print(f"Current len of unique authors : {len(unique_authors)}")
replacement={}
for key,val in unique_authors.items():
    if n_unique_authors[key]>50:
        replacement[key]=val
unique_authors=replacement
print(f"After removing len is {len(unique_authors)}")



for key, val in unique_authors.items():
    authors=val.split(",")
    unique_authors[key]=authors
labels=[]
columns=[]
strength_cols=[]
for key,val in unique_authors.items():
    strengths=[]
    column=[]

    labels.append(key)
    for key2,val2 in unique_authors.items():
        n_common=len(set(val).intersection(val2))
        strength=n_common/min(len(val),len(val2))
        column.append(n_common)
        strengths.append(strength)
    strength_cols.append(strengths)
    columns.append(column)

df_strengths=pd.DataFrame(strength_cols,index=labels,columns=labels)
df=pd.DataFrame(columns,index=labels,columns=labels)
with open(r'unique_authors_list_full.json', 'w') as fp:
    json.dump(data1, fp)

print("done")