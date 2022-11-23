from menuslist import menusList
import argparse
from treelib import Node, Tree
# Ravintola Mara
# Ravintola Foodoo / Oikea Foodoo Reilu

# API joskus jättää viikosta esim maanantain pois

def treeprint(pvm, x):
    tree = Tree()
    tree.create_node(pvm, "paapaiva")  # root node
    for i, data in enumerate(x):
        tree.create_node(x[i], "ruoka" + str(i), parent="paapaiva")
    tree.show()

parser = argparse.ArgumentParser(description='get Oulu university restaurant menus')
#parser.add_argument('url', metavar='U', type=str,
#                    help='an integer for the accumulator')

parser.add_argument('name',
                    help='restaurants name = "restaurant mara" or "mara"')
args = parser.parse_args()

mara_url = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/93077/49?lang=fi"
foodooreilu_url = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/93077/48?lang=fi"

def main():
    # args.name == || args.kaikki=true
    if(args.name == 'mara'):
        args.name = 'Ravintola Mara'
        mara = menusList(mara_url, args.name)
        pvm = mara.getjsondays()
        mara_dict = mara.getjsonmenus()
        treeprint(pvm[0], mara_dict['Maanantai'])
        treeprint(pvm[1], mara_dict['Tiistai'])
        treeprint(pvm[2], mara_dict['Keskiviikko'])
        treeprint(pvm[3], mara_dict['Torstai'])
        treeprint(pvm[4], mara_dict['Perjantai'])

    elif(args.name == 'foodoo'):
        args.name = 'Foodoo Reilu'
        foodoo = menusList(foodooreilu_url, args.name)
        pvm = foodoo.getjsondays()
        foodoo_dict = foodoo.getjsonmenus()
        treeprint(pvm[0], foodoo_dict['Maanantai'])
        treeprint(pvm[1], foodoo_dict['Tiistai'])
        treeprint(pvm[2], foodoo_dict['Keskiviikko'])
        treeprint(pvm[3], foodoo_dict['Torstai'])
        treeprint(pvm[4], foodoo_dict['Perjantai'])

if __name__ == '__main__':
    main()
