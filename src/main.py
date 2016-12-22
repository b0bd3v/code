#!/usr/bin/python

#Code 

import sys
import json

print "Procurando por template -> ", str(sys.argv[1])

template = open("../templates/" + sys.argv[1] + ".template")

if not template is None:
	print "Template carregado com sucesso."
else:
	print "Nao foi possivel carregar o template ", sys.argv[1]
	exit()

print "Procurando por arquivo de paramentros -> ", str(sys.argv[2])

params = open("../params/" + sys.argv[2] + ".params")

if not params is None:
	print "Arquivo de parametros carregado com sucesso."
else:
	print "Nao foi possivel carregar o arquivo de parametros"
	exit() 

data = json.load(params)

print str(data)
