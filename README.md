# OuluCampusRestaurantMenus &middot; ![Build Status](https://img.shields.io/travis/npm/npm/latest.svg?style=flat-square)[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/your/your-project/blob/master/LICENSE)

WIP Small python project for getting Oulu Linnanmaa campus student restaurants menus. 

> Finnish

Pieni python projekti minkä tarkoituksena näyttää opiskelijaravintoloiden ruokalistat.

## Installing / Getting started

A quick introduction of the setup you need to get this project up &
running.

On Linux :

```shell
git clone https://github.com/jokkekoo/OuluCampusRestaurantMenus

```
If you want to install all requirements globally 
```shell
cd OuluCampusRestaurantMenus
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
,-h to see available restaurants
```shell
python3 main.py -h
```
Give restaurants name
```shell
python3 main.py foodoo
```
