from menuslist import menusList
import argparse
from treelib import Node, Tree

# Argument parseriin -h niin näyttää vaihtoehdot ravintoloiden nimille
# -h mara, foodoo, garden

# Printtaus vierekkäin Foodoo | Mara | Garden
#                             |      |  
#                             |      | 
#                             |      |

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
    if(args.name == 'mara'):
        args.name = 'Ravintola Mara'
        printOneMenu(args.name, mara_url)
    elif(args.name == 'foodoo'):
        args.name = 'Foodoo Reilu'
        printOneMenu(args.name, foodoo_url)
    elif(args.name == 'garden'):
        args.name = 'Foodoo Garden'
        printOneMenu(args.name, foodoo_url)

    if(args.name == 'all'):
        printAllMenus('fi')
if __name__ == '__main__':
    main()
