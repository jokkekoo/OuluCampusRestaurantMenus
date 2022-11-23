# OuluCampusRestaurantMenus &middot; [![Build Status](https://img.shields.io/travis/npm/npm/latest.svg?style=flat-square)](https://travis-ci.org/npm/npm) [![npm](https://img.shields.io/npm/v/npm.svg?style=flat-square)](https://www.npmjs.com/package/npm) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/your/your-project/blob/master/LICENSE)

Small python project for getting OAMK student restaurants menus.
It's currently only showing Mara and Foodoo menus, I'm working on adding Foodoo Garden and in the future Oulu University student restaurants.

> Finnish

Pieni python projekti minkä tarkoituksena näyttää opiskelijaravintoloiden ruokalistat.
Tällä hetkellä toimii vain Mara ja Foodoo. Ideana lisätä vielä Foodoo Garden ja tulevaisuudessa ehkä yliopiston opiskelijaravintoloita.

## Installing / Getting started

A quick introduction of the setup you need to get this project up &
running.

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
source venv/bin/source
pip install -r requirements.txt
```
Test it out 
It needs restaurants name as argument
```shell
python3 main.py foodoo
```
