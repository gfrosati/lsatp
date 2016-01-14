# -*- coding: utf-8 -*-

#Este código agarra los 10.000 artículos de la wikipedia y genera el
#LSA en el archivo lsaWikipedia.lsi

import readline
import rlcompleter

#Configura el autocompletar con tab en la consola
if 'libedit' in readline.__doc__:
    readline.parse_and_bind("bind ^I rl_complete")
else:
    readline.parse_and_bind("tab: complete")

#Configura los mensajes que se muestran
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#Palabras que se descartan del español
STOPWORDS = ['a','al','algo','algunas','algunos','ante','antes','como','con','contra','cual','cuando','de','del','desde','donde','durante','e','el','ella','ellas','ellos','en','entre','era','erais','eran','eras','eres','es','esa','esas','ese','eso','esos','esta','estaba','estabais','estaban','estabas','estad','estada','estadas','estado','estados','estamos','estando','estar','estaremos','estará','estarán','estarás','estaré','estaréis','estaría','estaríais','estaríamos','estarían','estarías','estas','este','estemos','esto','estos','estoy','estuve','estuviera','estuvierais','estuvieran','estuvieras','estuvieron','estuviese','estuvieseis','estuviesen','estuvieses','estuvimos','estuviste','estuvisteis','estuviéramos','estuviésemos','estuvo','está','estábamos','estáis','están','estás','esté','estéis','estén','estés','fue','fuera','fuerais','fueran','fueras','fueron','fuese','fueseis','fuesen','fueses','fui','fuimos','fuiste','fuisteis','fuéramos','fuésemos','ha','habida','habidas','habido','habidos','habiendo','habremos','habrá','habrán','habrás','habré','habréis','habría','habríais','habríamos','habrían','habrías','habéis','había','habíais','habíamos','habían','habías','han','has','hasta','hay','haya','hayamos','hayan','hayas','hayáis','he','hemos','hube','hubiera','hubierais','hubieran','hubieras','hubieron','hubiese','hubieseis','hubiesen','hubieses','hubimos','hubiste','hubisteis','hubiéramos','hubiésemos','hubo','la','las','le','les','lo','los','me','mi','mis','mucho','muchos','muy','más','mí','mía','mías','mío','míos','nada','ni','no','nos','nosotras','nosotros','nuestra','nuestras','nuestro','nuestros','o','os','otra','otras','otro','otros','para','pero','poco','por','porque','que','quien','quienes','qué','se','sea','seamos','sean','seas','seremos','será','serán','serás','seré','seréis','sería','seríais','seríamos','serían','serías','seáis','sido','siendo','sin','sobre','sois','somos','son','soy','su','sus','suya','suyas','suyo','suyos','sí','también','tanto','te','tendremos','tendrá','tendrán','tendrás','tendré','tendréis','tendría','tendríais','tendríamos','tendrían','tendrías','tened','tenemos','tenga','tengamos','tengan','tengas','tengo','tengáis','tenida','tenidas','tenido','tenidos','teniendo','tenéis','tenía','teníais','teníamos','tenían','tenías','ti','tiene','tienen','tienes','todo','todos','tu','tus','tuve','tuviera','tuvierais','tuvieran','tuvieras','tuvieron','tuviese','tuvieseis','tuviesen','tuvieses','tuvimos','tuviste','tuvisteis','tuviéramos','tuviésemos','tuvo','tuya','tuyas','tuyo','tuyos','tú','un','una','uno','unos','vosotras','vosotros','vuestra','vuestras','vuestro','vuestros','y','ya','yo','él','éramos']

#Palabras que se descartan de inglés y otros idiomas
STOPWORDS += ['des','du','est','sciences','star','the','of','commons','and','wikimedia','fishes','wikispecies','wikipedia','www','gnu','unported','you','university','insee','music','school','org','love','sub','wars','science','one','king','live','list','society','angry','emelec','et','dans','au','pour','dee','page','to','in','creative','oil','polish','revenge','strikes','blu','phantom','bloom','agent','fellowship','avengers','zone','tails','pass','bear','heads']


UTF8STP = [unicode(x,'utf-8') for x in STOPWORDS]

# Algunas librerías para importar
from gensim.utils import simple_preprocess
from gensim.corpora.wikicorpus import filter_wiki
import gensim.corpora
from os import listdir
from os.path import isfile, join

#Buscar todos los archivos de la carpeta articulos
mypath = 'articulos'
allfiles = [join(mypath,f) for f in listdir(mypath) if isfile(join(mypath, f))]


# Corpus separado en palabras para cada documento y con diccionario de texto a id numérico

def tokenize(text):
    return [token for token in simple_preprocess(filter_wiki(text)) if token not in UTF8STP]

class MyCorpus(gensim.corpora.TextCorpus):
    def get_texts(self):
        for filename in self.input: # for each relevant file
            yield tokenize(open(filename).read())


mycorpus = MyCorpus(allfiles)

# Muestro el diccionario
print(mycorpus.dictionary)

# Filtro palabras que no aparezcan menos de 5 veces ni más del 50% del texto.
mycorpus.dictionary.filter_extremes()

print(mycorpus.dictionary)

#Guardar el diccionario
mycorpus.dictionary.save('wikipedia.dict')

#Si se quiere guardar el Corpus
#gensim.corpora.MmCorpus.serialize('corpusId.mm', mycorpus, mycorpus.dictionary)

#Para cargarlo
#corpus = corpora.MmCorpus('/tmp/corpus.mm')

#Generar LSA de 300 dimensiones
model = gensim.models.lsimodel.LsiModel(mycorpus, 300, mycorpus.dictionary)

#Grabar LSA
model.save('lsaWikipedia.lsi')

#Imprimir los primeros 100 topics
model.print_topics(100)

#Cargar LSA guardado
#lsi = models.LsiModel.load('lsaWikipedia.lsi')
