#!/usr/bin/env python

import requests, json
from datetime import datetime

class menusList:
    def __init__(self, url, name):
        self.url = url
        self.name = name

    def getjsondays(self):
        pvm = []
        wjdata = requests.get(self.url).json()
        for date in wjdata[0]['menuTypes'][5]['menus'][0]['days']:
            pvm.append(date['date'])
        pvm = [str(x) for x in pvm]
        for i, date in enumerate(pvm):
            pvm[i] = datetime.strptime(date, '%Y%m%d').strftime('%d.%m.%Y')
            asd = pvm[i]
            asd = datetime.strptime(asd, '%d.%m.%Y')
            asd = asd.strftime("%a")
            pvm[i] = asd + ' ' + pvm[i]
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
        mealslist = []

        wjdata = requests.get(self.url).json()

        keyId = self.getkeyID(wjdata)
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

if __name__ == '__main__':
    main()
