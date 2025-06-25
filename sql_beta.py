import pandas as pd
import sqlite3

# Criando o Conn
conn = sqlite3.connect('sistema.db')
c = conn.cursor()

# Criando tabela de Processos
c.execute(""" CREATE TABLE IF NOT EXISTS processos (
          'No Processo' number,
          Empresa text,
          Tipo text,
          Ação text,
          Vara text,
          Fase text,
          Instância number,
          'Data Inicia' text,
          'Data Final' text,
          'Processo Concluido' number,
          'Processo Vencido' number,
          Advogados text,
          Cliente text,
          'cpf Cliente' number,
          'Descrição' text)""")

# Criando tabela de Advogados
c.execute(""" CREATE TABLE IF NOT EXISTS advogados (
          Advogado text,
          OAB number,
          CPF number)""")

df_adv = pd.read_sql("SELECT * FROM advogados", conn)
df_proc = pd.read_sql("SELECT * FROM processos", conn)

conn.commit()
conn.close()

