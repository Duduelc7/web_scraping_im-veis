
#%%
from numpy import arange
from pkg_resources import ensure_directory
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
# %%
url = 'https://www.vivareal.com.br/venda/parana/curitiba/apartamento_residencial/?pagina={}'
# %%
i = 1
ret = requests.get(url.format(i))
soup = bs(ret.text)
# %%
houses = soup.find_all('a', {'class': 'property-card__content-link js-card-title'})
qntd_imoveis = float(soup.find('strong', {'class': 'results-summary__count'}).text.replace('.',''))
# %%
house = houses[0]
# %%
df = pd.DataFrame(
    columns=[
        'descricao',
        'endereco',
        'area',
        'quartos',
        'wc',
        'vagas',
        'valor',
        'condominio',
        'link'

    ]
)
i = 0
while qntd_imoveis > df.shape[0]:
    i += 1
    print(f"valor i :{i} \t\t qntd_imoveis: {df.shape[0]}")
    ret = requests.get(url.format(i))
    soup = bs(ret.text)
    houses = soup.find_all('a', {'class': 'property-card__content-link js-card-title'})
    
    for house in houses:
        
        try:
            descricao = house.find('span', {'class': 'property-card__title'}).text.strip()
        except:
            descricao = None

        try:
            endereco = house.find('span', {'class': 'property-card__address'}).text.strip()
        except:
            endereco = None
        try:
            area = house.find('span', {'class': 'property-card__detail-area'}).text.strip()
        except:
            area = None
        try:
            quartos = house.find('li', {'class': 'property-card__detail-room'}).span.text.strip()
        except:
            quartos = None
        try:
            wc = house.find('li', {'class': 'property-card__detail-bathroom'}).span.text.strip()
        except:
            wc = None
        try:
            vagas  = house.find('li', {'class': 'property-card__detail-garage'}).span.text.strip()
        except:
            vagas = None
        try:
            valor = house.find('div',{'class': 'property-card__price'}).p.text.strip()
        except:
            valor = None
        try:
            condominio = house.find('strong',{'class': 'js-condo-price'}).text.strip()
        except:
            condominio = None
        try:
            link ='https://www.vivareal.com.br' + house['href']
        except:
            link = None
        df.loc[df.shape[0]] = [
            descricao,
            endereco,
            area,
            quartos,
            wc,
            vagas,
            valor,
            condominio,
            link

        ]
# %%
print(f"""{descricao}
    End: {endereco}
    Area: {area}m²
    Quartos: {quartos}
    Banheiros: {wc}
    Vagas: {vagas}
    Valor: {valor}
    Condominio: {condominio}
    Link: {link}""")
# %%

df
# %%
df.to_csv('banco_de_imoveis.csv', sep=';', index=False)
