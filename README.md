Plongez dans l'infinité des plans, où chaque monde est différant dans une histoire mélangeant fantaisie, moderne et science-fiction. 
## Objectif :
Ce git a pour but de canaliser l'ensembles des règles, histoires et ressources au même en droit.

## Indexe :
- [Les règles](règles/index.md)

## Mes inspirations :
- [the dark tower (2017)](https://www.allocine.fr/film/fichefilm_gen_cfilm=146417.html)
- [heavy metal (1981)](https://www.allocine.fr/film/fichefilm_gen_cfilm=1086.html)
- [doctor who](https://fr.wikipedia.org/wiki/Doctor_Who)
- [stargate movie (1994)](https://www.allocine.fr/film/fichefilm_gen_cfilm=11478.html)
- [rick and morty (2013)](https://www.allocine.fr/series/ficheserie_gen_cserie=11561.html)
- [Dark (2017)](https://www.allocine.fr/series/ficheserie_gen_cserie=20328.html)
- [Fallout 2 (1997)](https://fr.wikipedia.org/wiki/Fallout_2)
- [Half-Life 2 (2004)](https://fr.wikipedia.org/wiki/Half-Life_2)
- [il était une fois l'espace (1982)](https://www.allocine.fr/series/ficheserie_gen_cserie=4537.html)
- [Warhammer 40k (1987)](https://fr.wikipedia.org/wiki/Warhammer_40,000_(jeu_de_figurines))

## Les sites qui m'on bien aidé :
- [Aidedd](https://www.aidedd.org/) : un site regroupent les règles de base de DnD.
- [OBSIDIAN TTRPG Tutorials](https://obsidianttrpgtutorials.com/Obsidian+TTRPG+Tutorials/Obsidian+TTRPG+Tutorials) : un site qui propose un tuto d'utilisation d'obsidian pour le ttrpg

# Information d'utilisation 
Ce git est fait avec l'application [obsidian](https://obsidian.md/) et requière des extensions. La pages [[book]] est fait via le site [homebrewery](https://homebrewery.naturalcrit.com/).

Utilise le OBSIDIAN TTRPG
[Obsidian TTRPG Tutorials](https://obsidianttrpgtutorials.com/Obsidian+TTRPG+Tutorials/Obsidian+TTRPG+Tutorials)
## Extensions obsidian :
- [advence canvas](https://github.com/Developer-Mike/obsidian-advanced-canvas)
- [dialogue](https://forum.obsidian.md/t/dialogue-plugin/27982)
- [markdown prettifier](https://github.com/cristianvasquez/obsidian-prettify)
- [Leaflet](https://github.com/javalent/obsidian-leaflet?tab=readme-ov-file)
- [Iconize](https://florianwoelki.github.io/obsidian-iconize/)
- [Dice Roller](https://github.com/javalent/dice-roller)
- [Excalidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin)
- [Fantasy Statblocks](https://obsidianttrpgtutorials.com/Obsidian+TTRPG+Tutorials/Plugin+Tutorials/The+Plugin+List)
- [Templater](https://github.com/SilentVoid13/Templater)
- [Timelines](https://github.com/George-debug/obsidian-timeline)
- BRAT
- [Zoom Map](https://github.com/Jareika/zoom-map)(installer via brat ^)


### Leaflet : une extension pour les maps
structure de base :

````
```
leaflet
id: leaflet-map
image: [[Image.jpg]]
height: 500px
lat: 50
long: 50
minZoom: 1
maxZoom: 10
defaultZoom: 5
unit: meters
scale: 1
marker: default, 39.983334, -82.983330, [[Note]]
darkMode: true
```
````

### Zoom Map
````
```zoommap
image: Assets/Map.jpg
# markers is optional; defaults to <image>.markers.json
# markers: Assets/Map.jpg.markers.json

# Map view limits
minZoom: 0.3
maxZoom: 8

# Size & interactivity
height: 560px
width: 100%
resizable: true
resizeHandle: native     # left | right | both | native
render: canvas           # or: dom

# Responsive display (fit into width, no wheel/pinch/dblclick pan/zoom)
responsive: false        # true → always fit; disables pan/zoom gestures

# Storage (optional)
# storage: note          # default is json; use "note" to store markers inline
# id: map-1              # optional stable id for inline storage (per code block)

# Alignment / wrapping (optional)
align: right             # left | center | right
wrap: true               # wrap text; useful with left/right alignment
```
```` 


![Obsidian - Working with Encounter Maps](https://www.youtube.com/watch?v=pTJGWO25le0&list=PLV5XWfKkFpk7MJTKv5YdSSpT9b-vLslWu&index=18)
![Obsidian - Working with Regional Maps](https://www.youtube.com/watch?v=G_Fw5mau-tA&t=247s)
