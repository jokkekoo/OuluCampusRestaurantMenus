from menuslist import menusList
import argparse
# Ravintola Maru
# Ravintola Foodoo / Oikea Foodoo Reilu

# if (argparse = mara / Ravintola Mara // foodoo / Ravintola Foodoo
# hienommin teksti terminaaliin ja argparse + muut ravintolat
# Pitää muuttaa, että 

# tämän päivän ruokalista

parser = argparse.ArgumentParser(description='get Oulu university restaurant menus')
#parser.add_argument('url', metavar='U', type=str,
#                    help='an integer for the accumulator')

parser.add_argument('name',
                    help='restaurants name = "restaurant mara" or "mara"')
args = parser.parse_args()

print(args.name)


mara_url = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/93077/49?lang=fi"
foodooreilu_url = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/93077/48?lang=fi"

def main():
    # args.name == || args.kaikki=true
    if(args.name == 'mara'):
        args.name = 'Ravintola Mara'
        mara = menusList(mara_url, args.name)
        pvm = mara.getjsondays()
        mara_dict = mara.getjsonmenus()
        print(mara_dict['Maanantai'])
        print(mara_dict['Tiistai'])
        print(mara_dict['Keskiviikko'])
        print(mara_dict['Torstai'])
        print(mara_dict['Perjantai'])

    elif(args.name == 'foodoo'):
        args.name = 'Foodoo Reilu'
        foodoo = menusList(foodooreilu_url, args.name)
        pvm = foodoo.getjsondays()
        foodoo_dict = foodoo.getjsonmenus()
        print(foodoo_dict['Maanantai'])
        print(foodoo_dict['Tiistai'])
        print(foodoo_dict['Keskiviikko'])
        print(foodoo_dict['Torstai'])
        print(foodoo_dict['Perjantai'])



if __name__ == '__main__':
    main()
