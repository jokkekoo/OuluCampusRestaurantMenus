from menuslist import menusList
import argparse
from argparse import RawTextHelpFormatter
from treelib import Node, Tree

# Printtaus vierekkäin Foodoo | Mara | Garden
#                             |      |  
#                             |      | 
#                             |      |

parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter,description='get Oulu university restaurant menus')
#parser.add_argument('url', metavar='U', type=str,
#                    help='an integer for the accumulator')
#'Name of the restaurant in lower case e.g. mara. -h for help'
parser.add_argument('name',
                    help='mara | foodoo | garden | medisiina | pekuri | kastari | napa | foodoosaladsoup | cafehub | herkku')
args = parser.parse_args()
#restaurant = args.name

mara_url_en = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/93077/49?lang=en" 
foodooreilu_url_en = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/93077/48?lang=en"

mara_url = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/93077/49?lang=fi"
foodoo_url = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/93077/48?lang=fi"

pekuri_url = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/95663/11?lang=fi"
#preludi_url = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/95663/8?lang=fi"
medisiina_url = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/95663/4?lang=fi"
kastari_url = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/95663/5?lang=fi"

def treeprint(pvm, dictionary, rname):
    tree = Tree()
    tree.create_node(rname, "ravintola") # root node
    for index, (key, value) in enumerate(dictionary.items()):
        tree.create_node(pvm[index], "paiva" + str(index), parent="ravintola")
        for x in range(len(value)):
            tree.create_node(value[x], "ruoka" + pvm[index] + str(x), parent="paiva"+str(index))
    tree.show()

def printOneMenu(rname, url):
    obj = menusList(url, rname)
    pvm = obj.getjsondays()
    obj_dict = obj.getjsonmenus()
    treeprint(pvm, obj_dict, rname)

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

    treeprint(pvm_mara, obj_mara_dict, 'Ravintola Mara')
    treeprint(pvm_foodoo, obj_foodoo_dict, 'Foodoo Reilu')
    treeprint(pvm_garden, obj_garden_dict, 'Foodoo Garden')

def main():
    if(args.name == 'mara'):
        args.name = 'Ravintola Mara'
        printOneMenu(args.name, mara_url)
    elif(args.name == 'foodoo'):
        args.name = 'Foodoo Reilu'
        printOneMenu(args.name, foodoo_url)
    elif(args.name == 'garden'):
        args.name = 'Foodoo Garden'
        printOneMenu(args.name, foodoo_url)
    elif(args.name == 'pekuri'):
        args.name = 'Ruokalista'
        printOneMenu(args.name, pekuri_url)
    elif(args.name == 'medisiina'):
        args.name = 'Ruokalista'
        printOneMenu(args.name, medisiina_url)
    elif(args.name == 'kastari'):
        args.name = 'Ruokalista'
        printOneMenu(args.name, kastari_url)
    elif(args.name == 'napa'):
        args.name = 'Napa Rohee'
        printOneMenu(args.name, foodoo_url)
    elif(args.name == 'foodoosaladsoup'):
        args.name = 'Foodoo Salad and soup'
        printOneMenu(args.name, foodoo_url)
    elif(args.name == 'cafehub'):
         args.name = 'Cafe Hub Salad and soup'
         printOneMenu(args.name, foodoo_url)
    elif(args.name == 'herkku'):
         args.name = 'Foodoo Herkku'
         printOneMenu(args.name, foodoo_url)

    if(args.name == 'all'):
        printAllMenus('fi')

if __name__ == '__main__':
    main()
