# OuluCampusRestaurantMenus &middot; ![Build Status](https://img.shields.io/travis/npm/npm/latest.svg?style=flat-square)[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/your/your-project/blob/master/LICENSE)

WIP Small python project for getting OAMK student restaurants menus. English menus coming soon.
It's currently showing Mara and Foodoo / Garden menus and their main courses. I'm working on adding in the future Oulu University student restaurants menus. Also maybe adding a option for showing dessert and showing the menu in a proper way as its listed on JSON : Lunch 1: Lunch 2: Veg etc.

> Finnish

Pieni python projekti minkä tarkoituksena näyttää opiskelijaravintoloiden ruokalistat.
Tällä hetkellä toimii Mara, Foodoo ja Foodoo Garden. Ideana lisätä tulevaisuudessa ehkä yliopiston opiskelijaravintoloita.

## Installing / Getting started

A quick introduction of the setup you need to get this project up &
running.

On Linux Ubuntu:

```shell
git clone https://github.com/jokkekoo/OuluCampusRestaurantMenus

```
If you want to install all requirements globally 
```shell
pip install -r requirements.txt
```
Recommended : make virtualenv
```shell
cd OuluCampusRestaurantMenus
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Test it out

It needs restaurants name as argument
```shell
python3 main.py foodoo
```
or
```shell
python3 main.py mara
```
