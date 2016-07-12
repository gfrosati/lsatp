# -*- coding: utf-8 -*-

from gensim import corpora, models, similarities
from os.path import isfile, join
from gensim.utils import simple_preprocess
from presidentes import *

import readline
import rlcompleter
import itertools
import re
import numpy, scipy.io

#Configura el autocompletar con tab en la consola
if 'libedit' in readline.__doc__:
    readline.parse_and_bind("bind ^I rl_complete")
else:
    readline.parse_and_bind("tab: complete")

#Cargar LSA (o LSI)
lsi = models.LsiModel.load('lsaWikipedia600.lsi')
dic = corpora.Dictionary.load_from_text('wikipedia.dict')

#frutas = ["Arándano","Aguacate","Banana","Coco","Ciruela","Cereza","Damasco","Durazno","Frambuesa","Fresa","Grosella","Higo","Kiwi","Limón","Mandarina","Mango","Manzana","Melón","Naranja","Pera","Piña","Pomelo","Sandía","Tomate","Uva"]
#animales = ["Abeja","Burro","Caballo","Elefante","Foca","Gato","Gallo","Jirafa","Kiwi","Koala","Liebre","Mariposa","Mosca","Oso","Oveja","Perro","Paloma","Rana","Serpiente","Sapo","Tiburón","Tortuga","Vaca","Zorro","Zebra"]

religion = ["pueblo", "cristianismo", "judaísmo", "islamismo", "budismo", "hinduismo", "dios", "demonio", "diablo", "fé", "religión"]
economia = ["mercado", "empresa", "privado", "moneda", "bonos", "inversión", "oferta", "demanda"]
politica = ["libertad", "socialismo", "comunismo", "populismo", "liberalismo", "anarquismo", "fascismo", "igualdad", "solidaridad", "fraternidad", "derechos", "gobierno", "democracia"]

def second(tupple_list):
    return [t[1] for t in tupple_list]

re = [second(lsi[dic.doc2bow(simple_preprocess(rel))]) for rel in religion]
ec = [second(lsi[dic.doc2bow(simple_preprocess(eco))]) for eco in economia]
po = [second(lsi[dic.doc2bow(simple_preprocess(pol))]) for pol in politica]

categorias = numpy.asarray(religion+economia+politica, dtype='object')
scipy.io.savemat('politica.mat', mdict={'religion': re, 'economia': ec, 'politica': po, 'categorias': categorias})
