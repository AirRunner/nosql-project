```sh
> SMEMBERS commerces:postcode:75017
  1) "7"
  2) "37"
  3) "38"
  4) "39"
  5) "40"
  6) "77"
  7) "110"
  8) "121"
  9) "127"
 10) "159"
 ...
```

```sh
> HGETALL commerces:commerce:3
1) "phone"
2) "06 19 32 84 23"
3) "name"
4) "restaurant indian house"
5) "id"
6) "3"
7) "description"
8) "Le restaurant indian house vous propose une cuisine gastronomique indienne \xc3\xa0 emporter au moins jusqu'au 20 janvier . nous disposons du click and collect sur  notre site"
```

```sh
> GEOPOS commerces:location 3
1) 1) "2.32645422220230103"
   2) "48.83428637998363797"
```

```sh
> GEODIST commerces:location 3 17 km
"4.8080"
```

```sh
> GEORADIUSBYMEMBER commerces:location 3 100 m
1) "3"
2) "1989"
3) "69"
4) "683"
5) "1501"
6) "1604"
7) "856"
```

```sh
> GEORADIUSBYMEMBER commerces:location 3 1 km COUNT 5 DESC
1) "330"
2) "163"
3) "1847"
4) "1620"
5) "1485"
```

```sh
> GEORADIUSBYMEMBER commerces:location 3 1 km COUNT 5 DESC WITHCOORD WITHDIST
1) 1) "330"
   2) "0.9862"
   3) 1) "2.32716768980026245"
      2) "48.82543259897407495"
2) 1) "163"
   2) "0.9844"
   3) 1) "2.31632083654403687"
      2) "48.82846919492295967"
3) 1) "1847"
   2) "0.9776"
   3) 1) "2.32976943254470825"
      2) "48.84280050835786824"
4) 1) "1620"
   2) "0.9776"
   3) 1) "2.32976943254470825"
      2) "48.84280050835786824"
5) 1) "1485"
   2) "0.9484"
   3) 1) "2.32652395963668823"
      2) "48.84281318196366328"
```