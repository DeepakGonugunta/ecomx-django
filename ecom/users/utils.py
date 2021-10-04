import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np
import pandas as pd
from django_pandas.io import read_frame



def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,5))
    plt.title('sales')
    z=np.array([x,y])   
    label='men','women'
    myexplode = [0.1, 0]

    plt.pie(z,labels=label,shadow=True,explode=myexplode)
    plt.xticks(rotation=45)
    plt.tight_layout()
    graph=get_graph()
    return graph

def bar(x):
    t=sh=tr=0
    df=pd.DataFrame(x.values())
    men=df[df['parent']=='men']
    tshirts=men[men['category']=='tshirts']
    shirts=men[men['category']=='shirts']
    jeans=men[men['category']=='jeans']
    trousers=men[men['category']=='trousers']
    print(shirts)


    c=len(tshirts)
    d=len(shirts)
    e=len(jeans)
    f=len(trousers)
    print(c,d)
    z=['tshirts','shirts','jeans','trousers']
    b=[c,d,e,f]
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,5))
    plt.title('men-sales')
    plt.bar(z,b)
    plt.xticks(rotation=45)
    plt.xlabel('type')
    plt.ylabel('number of products sold')
    plt.tight_layout()
    graph=get_graph()
    return graph

def fbar(x):
    t=sh=tr=0
    df=pd.DataFrame(x.values())
    female=df[df['parent']=='women']
    tshirts=female[female['category']=='tshirts']
    shirts=female[female['category']=='shirts']
    jeans=female[female['category']=='jeans']

    print(shirts)


    c=len(tshirts)
    d=len(shirts)
    e=len(jeans)
    print(c,d)
    z=['tshirts','shirts','jeans']
    b=[c,d,e]
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,5))
    plt.title('women-sales')
    plt.bar(z,b)
    plt.xticks(rotation=45)
    plt.xlabel('type')
    plt.ylabel('number of products sold')
    plt.tight_layout()
    graph=get_graph()
    return graph


       
        

    
def payment_type(x):
    df=pd.DataFrame(x.values())
    print(df)
    cod=df[df['method']=='cod']
    c=len(cod)
    online=df[df['method']=='online']
    o=len(online)
    z=['cash_on_delivery','online']
    b=[c,o]
    plt.switch_backend('AGG')
    plt.figure(figsize=(4,5))
    plt.title('types of payment')
    plt.bar(z,b)
    plt.xticks(rotation=45)
    plt.xlabel('paymnent method')
    plt.ylabel('count')
    plt.tight_layout()
    graph=get_graph()
    return graph





