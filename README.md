# Antenna Hullám Vizualizáló

**Verzió:** 1.0

3D-s, animált vizualizáció 2 portos antenna hullámainak megjelenítéséhez. Megjeleníti mindkét port hullámát és az eredő hullámot a térben, interaktív ki/be kapcsolással.

## Követelmények

```
pip install numpy matplotlib
```

## Futtatás

```
python antenna_viz.py
```

## Paraméterek

A program indításkor bekéri az alábbi értékeket (Enter-rel az alapértelmezett fogadható el):

| Paraméter | Alapértelmezett | Leírás |
|---|---|---|
| 1. port amplitúdója | 1.0 | Az 1. port hullámának amplitúdója |
| 1. port polarizációs szöge | 45° | Az 1. port rezgési iránya a Y-Z síkban |
| 2. port amplitúdója | 1.0 | A 2. port hullámának amplitúdója |
| 2. port polarizációs szöge | -45° | A 2. port rezgési iránya a Y-Z síkban |
| Fáziseltérés | 90° | A 2. port fáziseltolása az 1. porthoz képest |

## Megjelenítés

- **X tengely** — terjedési irány
- **Y tengely** — vízszintes polarizációs komponens
- **Z tengely** — függőleges polarizációs komponens
- 🔵 **Kék vonal** — 1. port hulláma
- 🔴 **Piros vonal** — 2. port hulláma
- 🟢 **Zöld vonal** — eredő hullám (a két port összege)

A jobb oldali **checkbox panelen** bármelyik hullám ki/be kapcsolható menet közben.

## Példák

| A1 | pol1 | A2 | pol2 | Δφ | Eredmény |
|---|---|---|---|---|---|
| 1.0 | 45° | 1.0 | -45° | 90° | Körpolarizált eredő |
| 1.0 | 45° | 1.0 | -45° | 0° | Lineárisan polarizált eredő |
| 1.0 | 45° | 0.5 | -45° | 90° | Elliptikusan polarizált eredő |
