import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import psycopg2

try:
   
    connection=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='130309',
        database='Proyecto_bd'
    ) 
    print("Conexion exitosa")

    cursor=connection.cursor()
    cursor.execute('SELECT version()')
    row=cursor.fetchone()
    print(row)
    dfCases=cursor.execute('select distinct nombre_importador, count(id) as cantidad_solicitudes from importador inner join solicitud on solicitud.id_importador = importador.id group by(id,nombre_importador) having count(id)>80')
    
    rows=cursor.fetchall()
   


    external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

    app=dash.Dash(__name__,external_stylesheets=external_stylesheets)
    fig = px.bar(rows,x=0,y=1,color_discrete_sequence=["#b52a64"],height=500,width=900,
                      title='Grafico_barras(cantidad vs nombre_importador)')
    fig1= px.pie(rows,values=1,names=0,color_discrete_sequence=["#b52a64"],height=500,width=900,
                      title='Pie Graph(cantidad vs nombre_importador)')
    
    
    app.layout = html.Div([
        
        html.Div([
        html.H2('Importadores que mas solicitan'),
        html.Img(src="/assets/grafico.png")
        ],className='banner'),
        
        html.Div([
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
                )
        
    ],className='container')
    
    ])
    
    if __name__ == '__main__':
        app.run_server(debug=True, use_reloader=False)

    
    dash_url = "http://127.0.0.1:8050"  
    if 'port' in app.server.config:
        dash_url = f"http://{app.server.host}:{app.server.config['port']}"

    print("Abre este enlace en tu navegador: {}".format(dash_url))


except Exception as ex:
    print(ex)

finally:
    connection.close()
    print("Conexion finalizada.")