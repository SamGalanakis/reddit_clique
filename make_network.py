import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import json


df=pd.read_csv("data//n_common_df.csv",index_col="Unnamed: 0")
df_strengths=pd.read_csv("data//strengths_df.csv",index_col="Unnamed: 0")
with open('data//n_unique_authors_full.json') as json_file: 
    n_unique_authors = json.load(json_file) 

labels=list(df.index)
labels.remove("Music")
nodes=[]
G=nx.Graph()
for key, val in n_unique_authors.items():
    if val<1000 or key=="Music":
        pass
    else:
        nodes.append(key)
        G.add_node(key,authors=val)


for node1 in nodes:
    for node2 in nodes:
        if node1==node2:
            continue
        
        strength=df_strengths.loc[node1,node2]
        if strength<0.05:
            continue
        G.add_edge(node1,node2,weight=strength)


nx.write_gexf(G, "graph.gexf")
position = nx.spring_layout(G,iterations=1000,scale=1.25)
nx.draw(G, with_labels=True, node_color="skyblue",pos=position,font_size=8)
plt.show()
