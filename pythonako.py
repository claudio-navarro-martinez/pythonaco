lista=[('a',1),('b',2),('c',3)]

df=pd.DataFrame(lista,columns=['col1','col2'])

df.groupby(['col1']).agg(['count','mean'])
