import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import psycopg2

try:
    connection=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='1425',
        database='Proyecto_bd'
    ) 
    print("Conexion exitosa")

    cursor=connection.cursor()
    cursor.execute("select distinct Rango_de_costo_unitario, count(ium) as cantidad from medicamento group by(Rango_de_costo_unitario)")
    rows1=cursor.fetchall()
    cursor.execute("select distinct nombre_importador, count(id) as cantidad_solicitudes from importador inner join solicitud on solicitud.id_importador = importador.id group by(id,nombre_importador) having count(id)>80")
    rows2=cursor.fetchall()
    cursor.execute("select distinct nombre_comercial_imagen_comercial, count(ium_medicamento) as cantidad_solicitudes from medicamento inner join solicitud on solicitud.ium_medicamento = medicamento.ium group by(ium_medicamento,nombre_comercial_imagen_comercial ) having  count(ium_medicamento)>50")
    rows3=cursor.fetchall()
    cursor.execute("select distinct tipo_solicitud, count(tipo_solicitud) as cantidad from solicitud group by(tipo_solicitud)")
    rows4=cursor.fetchall()
   


    external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

    app=dash.Dash(__name__,external_stylesheets=external_stylesheets)
    fig = px.line(rows1,x=0,y=1,color_discrete_sequence=["#FF7433"],height=500,width=900,
                      title='Poligono de Frecuencias (Cantidad vs Costo)')
    fig.update_xaxes(title_text='Costo')
    fig.update_yaxes(title_text='Cantidad')
    
    fig1= px.pie(rows1,values=1,names=0,color_discrete_sequence=["#FF7433"],height=500,width=900,
                    title='Pie Graph(Cantidad vs Costo)')
    
    fig2 = px.bar(rows2,x=0,y=1,color_discrete_sequence=["#33FF6B"],height=500,width=900,
                      title='Bar Graph (Cantidad vs Nombre de importador)')
    fig2.update_xaxes(title_text='Nombre de importador')
    fig2.update_yaxes(title_text='Cantidad')
    
    fig3= px.pie(rows2,values=1,names=0,color_discrete_sequence=["#33FF6B"],height=500,width=900,
                      title='Pie Graph (Cantidad vs Nombre de importador)')

        
    fig4 = px.bar(rows3,x=0,y=1,color_discrete_sequence=["#33C4FF"],height=500,width=900,
                      title='Bar Graph (Cantidad vs Nombre comercial)')
    fig4.update_xaxes(title_text='Nombre comercial')
    fig4.update_yaxes(title_text='Cantidad')
    
    fig5= px.pie(rows3,values=1,names=0,color_discrete_sequence=["#33C4FF"],height=500,width=900,
                      title='Pie Graph (Cantidad vs Nombre comericial)')
     
    fig6 = px.bar(rows4,x=0,y=1,color_discrete_sequence=["#FF3386"],height=500,width=900,
                      title='Bar Graph (Cantidad vs Tipo de solicitud)')
    fig6.update_xaxes(title_text='Tipo de solicitd')
    fig6.update_yaxes(title_text='Cantidad')
    
    fig7= px.pie(rows4,values=1,names=0,color_discrete_sequence=["#FF3386"],height=500,width=1100,
                      title='Pie Graph (Cantidad vs Tipo de solicitud)')
    
    
    
    app.layout = html.Div([
        
        html.Div([
        html.H2('Dashboards')
        ],className='banner'),
        
        html.Div([
            html.H2('Rango de costos en el que se encuentra cada medicamento'),
            html.Div(),
                dcc.Graph(
                id='Grafica1',
                figure=fig
                ),
        ],className='container'),

        html.Div([
            html.Div(),
            dcc.Graph(
                id='Grafica2',
                figure=fig1
                ),
            html.H5('Podemos apreciar que los medicamentos más solicitados se sitúan en los rangos de costos de [10-20), [20-30) y [30-40). Por el contrario, aquellos con una demanda más baja se encuentran en los intervalos de [40-50) y [50-60).'),
    ],className='container'),
    
    html.Div([
            html.H2('Importadores que más solicitudes realizaron'),
            html.Div(),
                dcc.Graph(
                id='Grafica3',
                figure=fig2
                ),
        ],className='container'),

        html.Div([
            html.Div(),
            dcc.Graph(
                id='Grafica4',
                figure=fig3
                ),
            html.H5('Nos podemos percatar de que la empresa que presenta más solicitudes es Audifarma S.A, puede ser debido a que esta empresa dispensa medicamentos a varias de las principales E.P.S. del país.'),
        ],className='container'),
        
        
        html.Div([
            html.H2('Medicamentos más demandados'),
            html.Div(),
                dcc.Graph(
                id='Grafica5',
                figure=fig4
                ),
        ],className='container'),

        html.Div([
            html.Div(),
            dcc.Graph(
                id='Grafica6',
                figure=fig5
                ),
            html.H5('Podemos ver que el medicamento “Translarna” es el medicamento que tiene mayor solicitud y tiene menos disponibilidad.'),
        ],className='container'),
         
        html.Div([
            html.H2('Número de solicitudes de cada tipo de solicitud '),
            html.Div(),
            dcc.Graph(
                id='Grafica7',
                figure=fig6
                ),
        ],className='container'),
           
           

        html.Div([
            html.Div(),
            dcc.Graph(
                id='Grafica8',
                figure=fig7
                   ),
            html.H5('Identificamos que los medicamentos mayormente solicitados son para más de un paciente, luego para urgencia clínica y los medicamentos con menor solicitud son para un paciente especifico.'),
        ],className='container')
    ])    
    
    if __name__ == '__main__':
         app.run_server(debug = True, use_reloader=False)
         
except Exception as ex:
    print(ex)

finally:
    
    connection.close()
    print("Conexion finalizada.")