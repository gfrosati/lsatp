# LSA - Análisis de Discursos Presidenciales

Trabajo práctico para la materia [Introducción a la Neurociencia Computacional](http://www.dc.uba.ar/materias/incc), Departamento de Computación, Universidad de Buenos Aires.


### Indice

* En la carpeta **artículos** se encuentran los +10.000 artículos bajados aleatoriamente desde la Wikipedia en español para el experimento con el programa *article_fetcher* (Ruby)

* En la carpeta **discursos** se encuentran los discursos de apertura / toma de posesión analizados en el experimento.

* El archivo **generadorLSA.py** (Python) generea un LSA de 300 dimensiones utilizando [gensim](https://radimrehurek.com/gensim/) a partir de los artículos de la Wikipedia descargados que sirven como base para el experimento.

* En la carpeta **resources** se encuentra el [diccionario](https://github.com/sromano/lsatp/blob/master/resources/wikipedia.dict) y el [modelo de LSA](https://github.com/sromano/lsatp/blob/master/resources/lsaWikipedia.lsi) a partir de los 10000 artículos generados a partir del generadorLSA.py

* El archivo **analizador.py** tiene funciones útiles usadas para analizar los discursos.


Copyright 2016 Sergio Romano
