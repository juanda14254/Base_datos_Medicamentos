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
    dfCases=cursor.execute('select distinct tipo_solicitud, count(tipo_solicitud) as cantidad from solicitud group by(tipo_solicitud)')
    rows=cursor.fetchall()
   


    external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

    app=dash.Dash(__name__,external_stylesheets=external_stylesheets)
    
   



    fig = px.bar(rows,x=1,y=0,color_discrete_sequence=["#7c1313"], orientation = 'h',height=500,width=900,
                      title='Bar Graph horizontal (cantidad vs tipo_solicitud)')
    fig1= px.pie(rows,values=1,names=0,color_discrete_sequence=["#7c1313"],height=500,width=900,
                      title='Pie Graph (cantidad vs tipo_solicitud)')
    
    
    app.layout = html.Div([
        
        html.Div([
        html.H2('Tipos de solicitud'),
        html.Img(src="/assets/grafico.png")
        ],className='banner'),
        
        
        html.Div([
            
            html.Div([
                html.Div(),
                    dcc.Graph(
                    id='Grafica1',
                    figure=fig
                    ),
            ],className='row'),
           
           

            html.Div([
                html.Div(),
                dcc.Graph(
                    id='Grafica2',
                    figure=fig1
                    )
        
        ],className='row'),
        html.Div([
                html.H5("")
            ]),
    ],className='container')

    ])
    if __name__ == ('__main__'):
        app.run_server(debug=True)  
    

except Exception as ex:
    print(ex)

finally:
   
    
    connection.close()
    print("Conexion finalizada.")

