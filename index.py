import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import sqlite3

# import from folders
from app import *
from components import home, sidebar
from sql_beta import df_proc, df_adv

# Criar estrutura para Store intermediária ==============



# =========  Layout  =========== #
app.layout = dbc.Container([
    # Store e Location
    dcc.Location(id='url'), # Definindo localização do projeto
    dcc.Store(id='store_intermedio', data={}),
    dcc.Store(id='store_adv', data=df_adv.to_dict()),
    dcc.Store(id='store_proc', data=df_proc.to_dict()),
    html.Div(id='div_fantasma'),

    # Layout
    # Criando uma sidebar
    dbc.Row([
        dbc.Col([
            sidebar.layout
        ], md=2, style={'padding': '0px'}),
        # Criando um container com o restante da tela
        dbc.Col([
            dbc.Container(id='page-content', fluid=True, style={'height': '100%', 'width': '100%', 'padding-left': '14px'})
        ], md=10, style={'padding': '0px'})
    ])
    

], fluid=True)

# ======= Callbacks ======== #
# URL callback to update page content
@app.callback(
    Output('page-content', 'children'), # Definindo o output
    Input('url', 'pathname'), # Definindo o input
)
def render_page(pathname):
    if pathname == '/home' or pathname == '/':
        return home.layout
    else:
        return dbc.Container([
            html.H1('404 Not Found', className="Text-Danger"), # Definindo o texto
            html.Hr(), # Pulando Linha
            html.P(f'O caminho "{pathname}" nao foi encontrado'),
            html.P(f'Use a Navbar para navegar no site.')
        ])


# Dcc.Store back to file
@app.callback(
    Output('div_fantasma', 'children'), # criando div_fastasma para armazenar os dados
    Input('store_adv', 'data'), # Definindo 'store_adv' como input
    Input('store_proc', 'data'), # Definindo 'store_proc' como input
)
def update_file(adv_data, proc_data):
    df_adv_aux = pd.DataFrame(adv_data)
    df_proc_aux = pd.DataFrame(proc_data)

    # Preencher com o SQL
    conn = sqlite3.connect('sistema.db')
    df_proc_aux.to_sql('processos', conn, if_exists='replace', index=False)
    conn.commit()
    df_adv_aux.to_sql('advogados', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()
    return []



if __name__ == '__main__':
    app.run(debug=True)
