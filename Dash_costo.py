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
    dfCases=cursor.execute('select distinct Rango_de_costo_unitario, count(ium) as cantidad from medicamento group by(Rango_de_costo_unitario)')
    
    rows=cursor.fetchall()
   


    external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

    app=dash.Dash(__name__,external_stylesheets=external_stylesheets)
    fig = px.line(rows,x=0,y=1,color_discrete_sequence=["#09777A"],height=500,width=900,
                      title='Poligono de Frecuencias(cantidad vs costo)')
    fig1= px.pie(rows,values=1,names=0,color_discrete_sequence=["#09777A"],height=500,width=900,
                      title='Pie Graph(cantidad vs costo)')
    
    
    app.layout = html.Div([
        
        html.Div([
        html.H2('Intervalos del costo de medicamentos'),
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