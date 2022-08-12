# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 11:22:16 2022

@author: Roberto Schneider
"""

class BD:
    def __init__(self, homol = False):
        
        self.homol = homol
        
        #dados da conexao
        #produção
        self.usuario = 'usuario_bd'
        self.__senha = 'senha' #__ antes do atributo impede a visualização desse atributo ao instanciar um objeto
        self.host = 'nome_host'
        self.porta = '1521'
        self.servico = 'end_servico'
        
        if self.homol:
            #homologacao
            self.usuario = 'usuario_bd'
            self.__senha = 'senha'
            self.host = 'nome_host'
            self.porta = '1521'
            self.servico = 'end_servico'
    
    def consulta(self, query):
        '''str -> df'''
        #importa bibliotecas necessárias
        import pandas as pd
        import cx_Oracle
        
        #dados da conexao
        usuario = self.usuario
        senha = self.__senha
        host = self.host
        porta = self.porta
        servico = self.servico
        
        self.query = query
        
        #Configuração do DSN
        dsn = cx_Oracle.makedsn(
            host,
            porta,
            service_name = servico
        )
        
        #Configuração da Conexão
        conn = cx_Oracle.connect(
            user = usuario,
            password = senha,
            dsn = dsn,
            encoding = 'UTF-8',
            nencoding= 'UTF-8'
        )
        
        df = pd.read_sql(self.query, conn)
                
        conn.close()
        return df


if __name__ == '__main__':
    #para testar a classe
    bd = BD()
    try:
        print(bd.__senha)
    except:
        pass
    query = 'select sysdate FROM dual'
    tabela = bd.consulta(query)
