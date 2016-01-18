# -*- coding: utf-8 -*-

from gensim import corpora, models, similarities
from os.path import isfile, join
from gensim.utils import simple_preprocess
from presidentes import *

import readline
import rlcompleter
import itertools
import re

#Configura el autocompletar con tab en la consola
if 'libedit' in readline.__doc__:
    readline.parse_and_bind("bind ^I rl_complete")
else:
    readline.parse_and_bind("tab: complete")

#Cargar LSA (o LSI)
lsi = models.LsiModel.load('resources/lsaWikipedia.lsi')

#Cargar diccionario que convierte textos en indices de LSA
dic = corpora.dictionary.Dictionary.load('resources/wikipedia.dict')

def tokenize(text):
    return [token for token in simple_preprocess(text)]

#Carpeta de discursos
docPaths = 'discursos'
#Cargar documentos
documentos = [ join(docPaths, f+'.txt') for f in todos]
#Conversion a LSA
corpus = [lsi[dic.doc2bow(tokenize(open(filename).read()))] for filename in documentos]
#Indice de similitud
fullIndex = similarities.MatrixSimilarity(corpus)

def promedio_palabras(presidentes,palabras):
    sims = similarity(presidentes,palabras)
    values = map((lambda x: (x[1])),sims)
    return sum(values) / len(values)

def similarity(presidentes,palabras,encode=True):
    palabrasC = palabras
    if encode:
      palabrasC = [unicode(x,'utf-8') for x in palabrasC]

    palabrasC = lsi[dic.doc2bow(palabrasC)]

    index = fullIndex[palabrasC]
    res = [tup for tup in map((lambda x: (todos[x[0]],x[1])),enumerate(index)) if tup[0] in presidentes]
    return res

def analisis_global(presidentes,palabras,encode=True):
    sim = similarity(presidentes,palabras,encode)
    grouped = itertools.groupby(sim,(lambda x: re.match('.*/(.*)[0-9]{4}',x[0]).group(1)))
    res = []
    for key, group in grouped:
      values = map((lambda x: (x[1])),group)
      res.append((key,sum(values) / len(values)))
    for elem in sorted(res, key=lambda item: -item[1]):
      print(elem)
    print(sorted(sim, key=lambda item: -item[1]))
    return

def analisis_global_raw(presidentes,texto):
    palabras = tokenize(texto)
    analisis_global(presidentes,palabras,False)

def matrix_simetria():
    documentos = [ map((lambda x: join(docPaths, x+'.txt')),f) for f in todosAgrupados]
    gdocs = [ " ".join([open(doc).read() for doc in docs]) for docs in documentos ]
    corpus = [ lsi[dic.doc2bow(tokenize(doc))] for doc in gdocs]
    index = similarities.MatrixSimilarity(corpus)
    for sim in index:
        for i in sim:
            print(i)
    #for sim in index:
        #print(sim)
        #print(map((lambda x: (re.match('.*/(.*)[0-9]{4}',todosAgrupados[x[0]][0]).group(1),round(x[1],2))),list(enumerate(sim))))


analisis_global(todos,['enemigo','opositor'])

