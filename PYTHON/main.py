
from coneccion import Connection 
import consultas as sql
import pandas as pd

con = Connection()
con.openConnection()

#CONSULTA DE NUMERO DE CASOS POR MUNICIPIO 
query = pd.read_sql_query(sql.casosPorMunicipio(), con.connection)
dfCases = pd.DataFrame(query, columns=["num_casos", "nombre_municipio"])
print(dfCases.head(125))

#CONSULTA DE CASOS DE MUJERES MAYORES A OCHENTA ANOS 
query = pd.read_sql_query(sql.CasosDeMuejeresMayoresDe80anos(), con.connection)
dfCases = pd.DataFrame(query, columns=["caso_id", "paciente_id", "inicio_sintomas", "tipo_contagio", "estado", "edad", "sexo"])
print(dfCases.head(7561))

#EXTRANJEROS FALLECIDOS
query = pd.read_sql_query(sql.ExtranjerosFallecidos(), con.connection)
dfCases = pd.DataFrame(query, columns=["pais_nomrbe", "paciente_id", "fecha_notificacion", "fecha_muerte", "municipio"])
print(dfCases.head(13))

#CONSULTA DE CONTAGIADOS EXTRANGEROS POR MUNICIPIO 
query = pd.read_sql_query(sql.ExtrangerosPorMunicipio(), con.connection)
dfCases = pd.DataFrame(query, columns=["num_casos", "nacionalidad", "nombre_municipio"])
print(dfCases.head(225))

con.closeConnection()