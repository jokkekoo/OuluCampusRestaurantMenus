#!/usr/bin/env python

import requests, json

#pvm = []
#mealslist = []
# Ravintola Maru
# Ravintola Foodoo / Oikea Foodoo Reilu


mara_url = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/93077/49?lang=fi"
foodooreilu_url = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/93077/48?lang=fi"
class menusList:
    def __init__(self, url, name):
        self.url = url
        self.name = name

    def getjsondays(self):
        pvm = []
        wjdata = requests.get(self.url).json()
        for date in wjdata[0]['menuTypes'][5]['menus'][0]['days']:
            pvm.append(date['date'])
        return pvm

    def add_values_in_dict(self, sample_dict, key, list_of_values):
        ''' Append multiple values to a key in 
            the given dictionary '''
        if key not in sample_dict:
            sample_dict[key] = list()
        sample_dict[key].extend(list_of_values)
        return sample_dict

    def getkeyID(self, json):
        for i in range(0,10):
            check_for_correct_key = json[0]['menuTypes'][i]['menuTypeName']
            if(check_for_correct_key == self.name):
                x = i
                return x

    def getjsonmenus(self):
        print('Fetching Data from Jamix API')
        thisdict = {'Maanantai':[],
                    'Tiistai':[],
                    'Keskiviikko':[],
                    'Torstai':[],
                    'Perjantai':[]
                    }
        pvm = []
        mealslist = []

        wjdata = requests.get(self.url).json()

        for date in wjdata[0]['menuTypes'][5]['menus'][0]['days']:
            pvm.append(date['date'])

        keyId = self.getkeyID(wjdata)
        print(keyId)
        #check_for_correct_key = wjdata[0]['menuTypes'][5]['menuTypeName']
        for x in range(0,5):
            for i in range(0,4):
                for meals in wjdata[0]['menuTypes'][keyId]['menus'][0]['days'][x]['mealoptions'][i]['menuItems']:
                    mealslist.append(meals['name'])
                i += 1
            if x==0:
                thisdict = self.add_values_in_dict(thisdict, 'Maanantai', mealslist)
            elif x==1:
                thisdict = self.add_values_in_dict(thisdict, 'Tiistai', mealslist)
            elif x==2:
                thisdict = self.add_values_in_dict(thisdict, 'Keskiviikko', mealslist)
            elif x==3:
                thisdict = self.add_values_in_dict(thisdict, 'Torstai', mealslist)
            elif x==4:
                thisdict = self.add_values_in_dict(thisdict, 'Perjantai', mealslist)
            mealslist.clear()
            x += 1
        return thisdict

mara = menusList(mara_url, 'Ravintola Mara')
pvm = mara.getjsondays()
#print(pvm)

mara_dictionary = mara.getjsonmenus()

print(mara_dictionary['Maanantai'])
print(mara_dictionary['Tiistai'])
print(mara_dictionary['Keskiviikko'])
print(mara_dictionary['Torstai'])
print(mara_dictionary['Perjantai'])

foodoo_reilu = menusList(foodooreilu_url, 'Foodoo Reilu')
foodooreilu_dictionary = foodoo_reilu.getjsonmenus()

print(foodooreilu_dictionary['Maanantai'])
print(foodooreilu_dictionary['Tiistai'])
print(foodooreilu_dictionary['Keskiviikko'])
print(foodooreilu_dictionary['Torstai'])
print(foodooreilu_dictionary['Perjantai'])


# 4, 6, 9, 9, 9 


