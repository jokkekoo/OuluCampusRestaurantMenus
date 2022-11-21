from menuslist import menusList

# Ravintola Maru
# Ravintola Foodoo / Oikea Foodoo Reilu

# if (argparse = mara / Ravintola Mara // foodoo / Ravintola Foodoo
# hienommin teksti terminaaliin ja argparse + muut ravintolat

def main():
    mara_url = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/93077/49?lang=fi"
    foodooreilu_url = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/93077/48?lang=fi"

    mara = menusList(mara_url, 'Ravintola Mara')
    pvm = mara.getjsondays()

    mara_dict = mara.getjsonmenus()

    print(mara_dict['Maanantai'])
    print(mara_dict['Tiistai'])
    print(mara_dict['Keskiviikko'])
    print(mara_dict['Torstai'])
    print(mara_dict['Perjantai'])

if __name__ == '__main__':
    main()
