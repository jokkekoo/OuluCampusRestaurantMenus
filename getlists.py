#!/usr/bin/env python

"""
    Ärsytti hakea ravintolan lista monen linkin takaa netistä
    niin kehitin tällaisen tavan
"""

import requests, json
# Ravintola mara https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/93077/49?lang=fi
# my_json['value']['queryInfo']['creationTime'] # 1349724919000



# OAMK ruokalat = Restaurant FOODOO, Restaurant MARA, Restaurant FOODOO GARDEN kaikki Juvenes
# Tällä hetkellä ottaa vain MARA ruokalistan
mara_url = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/93077/49?lang=fi"
wjdata = requests.get(mara_url).json()

pvm = []
mealslist =  []

thisdict = {'Maanantai':[],
            'Tiistai':[],
            'Keskiviikko':[],
            'Torstai':[],
            'Perjantai':[]
            }

# Kalenteri päivät yyyymmdd muodossa
for date in wjdata[0]['menuTypes'][5]['menus'][0]['days']:
    pvm.append(date['date'])
#print(pvm)


def add_values_in_dict(sample_dict, key, list_of_values):
    ''' Append multiple values to a key in 
        the given dictionary '''
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict


# x on päivä (ma-pe), i on ruokalistalle (enintään 4 ruokalajia päivälle).
# API vaihtaa järjestystä, joten selvitetään missä on Ravintola Mara
check_for_mara_again = wjdata[0]['menuTypes'][5]['menuTypeName']
if(check_for_mara_again == 'Ravintola Mara'):
    for x in range(0,5):
        for i in range(0,4):
            for meals in wjdata[0]['menuTypes'][5]['menus'][0]['days'][x]['mealoptions'][i]['menuItems']:
                mealslist.append(meals['name'])
            i += 1
        if x==0:
            thisdict = add_values_in_dict(thisdict, 'Maanantai', mealslist)
        elif x==1:
            thisdict = add_values_in_dict(thisdict, 'Tiistai', mealslist)
        elif x==2:
            thisdict = add_values_in_dict(thisdict, 'Keskiviikko', mealslist)
        elif x==3:
            thisdict = add_values_in_dict(thisdict, 'Torstai', mealslist)
        elif x==4:
            thisdict = add_values_in_dict(thisdict, 'Perjantai', mealslist)
        mealslist.clear()
        x += 1

check_for_mara_again = wjdata[0]['menuTypes'][6]['menuTypeName']
if(check_for_mara_again == 'Ravintola Mara'):
    for x in range(0,5):
        for i in range(0,4):
            for meals in wjdata[0]['menuTypes'][6]['menus'][0]['days'][x]['mealoptions'][i]['menuItems']:
                mealslist.append(meals['name'])
            i += 1
        if x==0:
            thisdict = add_values_in_dict(thisdict, 'Maanantai', mealslist)
        elif x==1:
            thisdict = add_values_in_dict(thisdict, 'Tiistai', mealslist)
        elif x==2:
            thisdict = add_values_in_dict(thisdict, 'Keskiviikko', mealslist)
        elif x==3:
            thisdict = add_values_in_dict(thisdict, 'Torstai', mealslist)
        elif x==4:
            thisdict = add_values_in_dict(thisdict, 'Perjantai', mealslist)
        mealslist.clear()
        x += 1

#for i in range(0,10):
#    check_for_mara_again = wjdata[0]['menuTypes'][i]['menuTypeName']
#    if(check_for_mara_again == 'Ravintola Mara'):
#        x = 1
#        return x
# if check_for_correct_key == self.name)

def hae():
    for i in range(0,10):
        check_for_mara_again = wjdata[0]['menuTypes'][i]['menuTypeName']
        print(check_for_mara_again, i)
        if(check_for_mara_again == 'Ravintola Mara'):
            x = i
            return x

asd = hae()
print("HAE FUNKTION ARVOO !! :", asd)

print('Ravintola Mara ruokalista', pvm[0] , '-', pvm[4])
maanantai_lista = thisdict['Maanantai']
tiistai_lista = thisdict['Tiistai']
keskiviikko_lista = thisdict['Keskiviikko']
torstai_lista = thisdict['Torstai']
perjantai_lista = thisdict['Perjantai']
print('Maanantain ruoat : ',maanantai_lista)
print('Tiistain ruoat : ', tiistai_lista)
print('Keskiviikon ruoat : ', keskiviikko_lista)
print('Torstain ruoat : ', torstai_lista)
print('Perjantain ruoat : ', perjantai_lista)
