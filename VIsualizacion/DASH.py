import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from coneccion import Connection
import consultas as sql
from dash import Input, Output

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])


#QUERYS
con = Connection()
con.openConnection()

query = pd.read_sql_query(sql.casosPorMunicipio(), con.connection)

query2 = pd.read_sql_query(sql.EdadPromedioDeMuertos(), con.connection)

query3 = pd.read_sql_query(sql.CasosTTotalesYMuertesPorMunicipio(), con.connection)

query4 = pd.read_sql_query(sql.origenCaso(), con.connection)

query5 = pd.read_sql_query(sql.casosPorDia2020(), con.connection)

query6 = pd.read_sql_query(sql.casosPorDia2021(), con.connection)

query7 = pd.read_sql_query(sql.tasaRecuperadosPorGenero(), con.connection)

con.closeConnection()


#DATAFRAMES
dfCasos = pd.DataFrame(query, columns=["num_casos", "nombre_municipio"])

dfPromMuertos = pd.DataFrame(query2, columns=["nombre_municipio", "promedio_edad"])

dfcasosmuer = pd.DataFrame(query3, columns=["nombre_municipio", "num_muertes", "num_casos"])

dfOrigen = pd.DataFrame(query4, columns=["numero_imports", "numero_rela", "numero_com", "nuemro_std" ,"nom_municipio" ])

dfCasosDia2020 = pd.DataFrame(query5, columns=["num_casos", "fecha"])

dfCasosDia2021 = pd.DataFrame(query6, columns=["num_casos", "fecha"])

dfTasaRecuperacion = pd.DataFrame(query7, columns=["tasa", "genero"])
#FIGURAS

######################################
#####################1################
######################################
dfCasos.loc[dfCasos["num_casos"] < 6000, "nombre_municipio"] = 'Otros municipios'
figCasos = px.pie(dfCasos, values="num_casos", names="nombre_municipio", 
                  color_discrete_sequence=px.colors.sequential.Aggrnyl)

figCasos2 = px.line(dfCasos, x="nombre_municipio", y="num_casos", 
                    color_discrete_sequence=px.colors.sequential.Aggrnyl)



######################################
#####################2################
######################################
figBar = px.bar(dfPromMuertos.head(20), x="nombre_municipio", y="promedio_edad", 
                color_discrete_sequence=px.colors.sequential.Blugrn)

figBar2 = px.scatter(dfPromMuertos, x="promedio_edad", y="nombre_municipio", 
                     color="nombre_municipio",hover_name="nombre_municipio", 
                     log_x=True, color_discrete_sequence=px.colors.sequential.Aggrnyl)


######################################
#####################3################
######################################
CasosVSmuertes = px.scatter(dfcasosmuer, x="num_casos", y="num_muertes",
 	                        size="num_casos", color="nombre_municipio",
                            hover_name="nombre_municipio", log_x=True, 
                            size_max=80, color_discrete_sequence=px.colors.sequential.Aggrnyl)


######################################
#####################4################
######################################

dfOrigen.loc[dfOrigen["numero_imports"] < 10, "nom_municipio"] = 'Otros municipios'
origen = px.pie(dfOrigen, values="numero_imports", names="nom_municipio", 
                color_discrete_sequence=px.colors.sequential.Aggrnyl)

dfOrigen.loc[dfOrigen["numero_rela"] < 800, "nom_municipio"] = 'Otros municipios'
origen2 = px.pie(dfOrigen, values="numero_rela", names="nom_municipio", 
                 color_discrete_sequence=px.colors.sequential.Aggrnyl)

dfOrigen.loc[dfOrigen["numero_com"] < 800, "nom_municipio"] = 'Otros municipios'
origen3 = px.pie(dfOrigen, values="numero_com", names="nom_municipio", 
                 color_discrete_sequence=px.colors.sequential.Aggrnyl)

dfOrigen.loc[dfOrigen["nuemro_std"] < 800, "nom_municipio"] = 'Otros municipios'
origen4 = px.pie(dfOrigen, values="nuemro_std", names="nom_municipio", 
                 color_discrete_sequence=px.colors.sequential.Aggrnyl)


######################################
#####################5################
######################################

fecha2020 = px.line(dfCasosDia2020, x="fecha", y="num_casos", range_x=['2020-01-01','2020-12-31'], color_discrete_sequence=px.colors.sequential.Aggrnyl)

fecha2021 = px.line(dfCasosDia2021, x='fecha', y='num_casos', range_x=['2020-12-31','2021-12-31'], color_discrete_sequence=px.colors.sequential.Aggrnyl)


######################################
#####################6################
######################################

fig5 = px.pie(dfTasaRecuperacion, values='tasa', names='genero', color_discrete_sequence=px.colors.sequential.Aggrnyl)
#Layout
app.layout = html.Div(children=[
    
    html.H1(children='Casos de COVID-19 en Antioquia', className ="text-center", style = {'color' : '#27A072',
                                                                                          'fontSize':70,
                                                                                          'font-family': 'sans-serif'}),   
    
    html.Div(className = "card-title", children=[   
        
        dcc.Tabs(id="tabs-example-graph", value='tabs', children=[
        dcc.Tab(label='Casos por municipio', value='CasosPorMunicipio'),
        dcc.Tab(label='Edad promedio en casos de muerte por municipio', value='Promedio'),
        dcc.Tab(label='Casos y muertes por municipio', value='Puntitops'),
        dcc.Tab(label='Tipos de contagio', value='origen'),
        dcc.Tab(label='Casos por fecha', value='fecha'),
        dcc.Tab(label='Tasa de recuperados por genero', value='Tasa de recuperados por genero'),
    ]),
    html.Div(id='tabs-content-example-graph')
    ])

])

@app.callback(Output('tabs-content-example-graph', 'children'),Input('tabs-example-graph', 'value'))
def caso1(tab):    
    if tab == 'CasosPorMunicipio':
        return html.Div([
            html.H2('Casos por municipio', style = {'textAlign' : 'left',
                                                    'color' : '#18735B',
                                                    'fontSize':65,
                                                    'font-weight' : 'bold',
                                                    'font-family': 'sans-serif'}),
                dcc.Graph(
                id='CasosPorMunicipio',
                figure=figCasos
                ),
                dcc.Graph(
                id='CasosPorMunicipio2',
                figure=figCasos2
                )
        ])
    if tab == 'Promedio':
        return html.Div([
          html.H2('Edad promedio en casos de muerte por municipio', 
                     style = {'textAlign' : 'left',
                              'color' : '#18735B',
                              'fontSize':65,
                              'font-weight' : 'bold',
                              'font-family': 'sans-serif'}),
                dcc.Graph(
                id='PromedioMuertes',
                figure=figBar
                ),
                dcc.Graph(
                id='PromedioMuertes2',
                figure=figBar2
                )
        ])
    elif tab == 'Puntitops':
        return html.Div([
          html.H2('Casos y muertes por municipio', 
                     style = {'textAlign' : 'left',
                              'color' : '#18735B',
                              'fontSize':65,
                              'font-weight' : 'bold',
                              'font-family': 'sans-serif'}),
               dcc.Graph(
                id='Puntitops',
                figure=CasosVSmuertes
                )
        ])
    elif tab == 'origen':
        return html.Div([
          html.H2('Cantidad de diferentes tipos de contagio por municipio', 
                   style = {'textAlign' : 'left',
                             'color' : '#18735B',
                             'fontSize':60,
                             'font-weight' : 'bold',
                             'font-family': 'sans-serif'}),
          
          html.Div([
              dbc.Card([
              dbc.CardBody([html.H4("¿Cuales son los tipos de contagio?", 
                                    className="card-title"),html.P("importado: Son los casos en los que el paciente "
                                                                               "contragió el virus en otro país y al regresar "
                                                                               "es confirmado como positivo para COVID-19."),                                                                           
                                                                  
                                                            html.P("Relacionados: Son los casos en los que el paceinte "
                                                                                  "no sale del país y contrae el virus "
                                                                                  "de un caso importado."),
                                                                       
                                                            html.P("Comunitarios: Son los casos en los que el paciente "
                                                                   "es contagiado por personas que no han salido del país "
                                                                   "y no han tenido contacto directo con un caso relacionado."),
                                                                       
                                                            html.P("En estudio: Casos en los que se está estudiando en qué "
                                                                   "categoría clasificarlo."),
                  ])
              ])
         ]),
          
                   
          html.Div([
              html.H3('Numero de casos de origen importado por municipio', 
                         style = {'textAlign' : 'left',
                                  'color' : '#18735B',
                                  'fontSize':45,
                                  'font-family': 'sans-serif'}),
                   dcc.Graph(
                    id='origen',
                    figure=origen
                    ),
             html.H3('Numero de casos de origen realacionado por municipio', 
                         style = {'textAlign' : 'left',
                                  'color' : '#18735B',
                                  'fontSize':45,
                                  'font-family': 'sans-serif'}),
                   dcc.Graph(
                   id='origen2',
                    figure=origen2
                    ),
            html.H3('Numero de casos de origen comunitario por municipio', 
                         style = {'textAlign' : 'left',
                                  'color' : '#18735B',
                                  'fontSize':45,
                                  'font-family': 'sans-serif'}),
                   dcc.Graph(
                   id='origen3',
                    figure=origen3
                    ),
            html.H3('Numero de casos en estado de estudio por municipio', 
                         style = {'textAlign' : 'left',
                                  'color' : '#18735B',
                                  'fontSize':45,
                                  'font-family': 'sans-serif'}),
                   dcc.Graph(
                   id='origen4',
                    figure=origen4
                    )
            ])
        ])
    elif tab == 'fecha':
        return html.Div([
          html.H2('Casos por fecha', 
                     style = {'textAlign' : 'left',
                              'color' : '#18735B',
                              'fontSize':65,
                              'font-weight' : 'bold',
                              'font-family': 'sans-serif'}),
            html.H3('Numero de casoso por dia en 2020', 
                     style = {'textAlign' : 'left',
                               'color' : '#18735B',
                               'fontSize':50,
                               'font-family': 'sans-serif'}),               
               dcc.Graph(
               id='fecha2020',
               figure=fecha2020
               ),

            html.H3('Numero de casoso por dia en 2021', 
                     style = {'textAlign' : 'left',
                               'color' : '#18735B',
                               'fontSize':50,
                               'font-family': 'sans-serif'}),                 
               dcc.Graph(
               id='fecha2021',
               figure=fecha2021
               )
        ])
    if tab == 'Tasa de recuperados por genero':
        return html.Div([
          html.H2('Tasa de recuperados por genero', 
                     style = {'textAlign' : 'left',
                              'color' : '#18735B',
                              'fontSize':65,
                              'font-weight' : 'bold',
                              'font-family': 'sans-serif'}),
               dcc.Graph(
                id='Tasa de recuperados por genero',
                figure=fig5
                )
        ])

if __name__== '__main__' :
    app.run_server(debug = True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    