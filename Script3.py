import pandas as pd
import requests
import bs4
import re

#%%

src_df = pd.read_csv('companies.csv')

Websites = src_df['Website'].to_list()

#%%
def get_phone(soup):
    try:
        phone = soup.select("a[href*=phone]")[0].text
        return phone
    except:
        pass
    
    try:
        phone = soup.select("a[href*=callto]")[0].text
        return phone
    except:
        pass    
    
    try:
        phone = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-][2-9][0-9]{2}[-][0-9]{4}\b', response.text)[0]
        return phone
    except:
        pass

    try:
       phone = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b', response.text)[-1]
       return phone
    except:
        print ('Phone number not found')
        phone = ''
        return phone



# def get_email(soup):
#     try:
#         email = re.findall(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', response.text)[-1]
#         return email
#     except:
#         pass

#     try:
#         email = soup.select("a[href*=mailto]")[-1].text
#     except:
#         print ('Email not found')
#         email = ''
#         return email


#%%
for i, row in enumerate(Websites):
    print(i)
    print(row)


#%%
for i, row in enumerate(Websites):
    try:
        response = requests.get(row)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
    except:
        print ('Unsucessful: ' + str(response))
        continue

    phone = get_phone(soup)
    #email = get_email(soup)

    src_df.loc[i,'Phone'] = phone
    #src_df.loc[i,'Email'] = email
    print (f'{i} website:%s\nphone: : %s\n' %(row, phone))

src_df.to_csv('Finaloutput.csv', index=False)