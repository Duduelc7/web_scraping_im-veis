#%%
from numpy import arange
from pkg_resources import ensure_directory
import requests
from bs4 import BeautifulSoup as bs
import pandas
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
descricao = house.find('span', {'class': 'property-card__title'}).text.strip()
endereco = house.find('span', {'class': 'property-card__address'}).text.strip()
area = house.find('li', {'class': 'property-card__detail-area'}).text.strip()
quartos = house.find('span', {'class': 'property-card__detail-room'})


print(quartos)


# %%
descricao
endereco 
area 
quartos
wc 
vagas 
valor 
condominio 
link 
