from menuslist import menusList
import argparse
from treelib import Node, Tree
# Ravintola Mara
# Ravintola Foodoo / Oikea Foodoo Reilu

# API joskus jättää viikosta esim maanantain pois
# Argument parseriin -h niin näyttää vaihtoehdot ravintoloiden nimille
# -h mara, foodoo, garden

# API joskus jättää viikosta esim maanantain pois
# Printtaus vierekkäin Foodoo | Mara | Garden
#                             |      |  
#                             |      | 
#                             |      |


def treeprint(pvm, x, rname):
    tree = Tree()
    tree.create_node(rname, "ravintola")
    tree.create_node(pvm, "paapaiva", parent="ravintola")  # root node
    for i, data in enumerate(x):
        tree.create_node(x[i], "ruoka" + str(i), parent="paapaiva")
    tree.show()

def printOneMenu(rname, url):
    if(rname == 'garden'):
        rname = 'Foodoo Garden'
    elif(rname == 'foodoo'):
        rname = 'Foodoo Reilu'
    elif(rname == 'mara'):
        rname = 'Ravintola Mara'
    obj = menusList(url, rname)
    pvm = obj.getjsondays()
    obj_dict = obj.getjsonmenus()
    treeprint(pvm[0], obj_dict['Maanantai'], rname)
    treeprint(pvm[1], obj_dict['Tiistai'], rname)
    treeprint(pvm[2], obj_dict['Keskiviikko'], rname)
    treeprint(pvm[3], obj_dict['Torstai'], rname)
    treeprint(pvm[4], obj_dict['Perjantai'], rname)

def printAllMenus(lang):
    obj_mara = menusList("https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/93077/49?lang=" + lang, 'Ravintola Mara')
    obj_foodoo =  menusList("https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/93077/48?lang=" + lang, 'Foodoo Reilu')
    obj_garden = menusList("https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/93077/48?lang=" + lang, 'Foodoo Garden')

    pvm_mara = obj_mara.getjsondays()
    pvm_foodoo = obj_foodoo.getjsondays()
    pvm_garden = obj_garden.getjsondays()

    obj_mara_dict = obj_mara.getjsonmenus()
    obj_foodoo_dict = obj_foodoo.getjsonmenus()
    obj_garden_dict = obj_garden.getjsonmenus()

    treeprint(pvm_mara[0], obj_mara_dict['Maanantai']  , 'Ravintola Mara')
    treeprint(pvm_mara[1], obj_mara_dict['Tiistai']    , 'Ravintola Mara')
    treeprint(pvm_mara[2], obj_mara_dict['Keskiviikko'], 'Ravintola Mara')
    treeprint(pvm_mara[3], obj_mara_dict['Torstai']    , 'Ravintola Mara')
    treeprint(pvm_mara[4], obj_mara_dict['Perjantai']  , 'Ravintola Mara')

    treeprint(pvm_foodoo[0], obj_foodoo_dict['Maanantai']  , 'Foodoo Reilu')
    treeprint(pvm_foodoo[1], obj_foodoo_dict['Tiistai']    , 'Foodoo Reilu')
    treeprint(pvm_foodoo[2], obj_foodoo_dict['Keskiviikko'], 'Foodoo Reilu')
    treeprint(pvm_foodoo[3], obj_foodoo_dict['Torstai']    , 'Foodoo Reilu')
    treeprint(pvm_foodoo[4], obj_foodoo_dict['Perjantai']  , 'Foodoo Reilu')

    treeprint(pvm_garden[0], obj_garden_dict['Maanantai']  , 'Foodoo Garden')
    treeprint(pvm_garden[1], obj_garden_dict['Tiistai']    , 'Foodoo Garden')
    treeprint(pvm_garden[2], obj_garden_dict['Keskiviikko'], 'Foodoo Garden')
    treeprint(pvm_garden[3], obj_garden_dict['Torstai']    , 'Foodoo Garden')
    treeprint(pvm_garden[4], obj_garden_dict['Perjantai']  , 'Foodoo Garden')


parser = argparse.ArgumentParser(description='get Oulu university restaurant menus')
#parser.add_argument('url', metavar='U', type=str,
#                    help='an integer for the accumulator')

parser.add_argument('name',
                    help='restaurants name = "restaurant mara" or "mara"')
args = parser.parse_args()
#restaurant = args.name

mara_url_en = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/93077/49?lang=en" 
foodooreilu_url_en = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/93077/48?lang=en"

mara_url = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/93077/49?lang=fi"
foodoo_url = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/93077/48?lang=fi"

def main():
    # args.name == || args.kaikki=true
    if(args.name == 'mara'):
        printOneMenu(args.name, mara_url)
    elif(args.name == 'foodoo'):
        printOneMenu(args.name, foodoo_url)
    elif(args.name == 'garden'):
        printOneMenu(args.name, foodoo_url)

    if(args.name == 'all'):
        printAllMenus('fi')
if __name__ == '__main__':
    main()
