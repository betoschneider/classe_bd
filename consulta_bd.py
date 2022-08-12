# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 11:29:33 2022

@author: Roberto Schneider
"""

#importando a classe
from classes.bd import BD


query = 'select sysdate FROM dual'

#objeto bd com todos os atributos
bd = BD()

#será criada uma exceção ao tentar exibir o valor do atributo __senha
try:
    print(bd.__senha)
    print(bd.usuario)
except:
    print(bd.usuario)

#dataframe com o resultado da consulta
df = bd.consulta(query)