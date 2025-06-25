import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd

from dash import dash_table # Dispor dados em forma de tabela
from dash.dash_table.Format import Group # Dispor dados em forma de tabela

from app import app
from components import home

# ======== Layout ========= #
layout = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle('Cadastro de Advogados')),
    dbc.ModalBody([
        dbc.Row([
            dbc.Col([
                html.Div(id='table_adv', className='dbc')
            ])
        ])
    ]),
    dbc.ModalFooter([
        dbc.Button('Sair', id='quit_buttom', color='danger'),
        dbc.Button('Novo', id='new_adv_buttom', color='success'),

    ])
], id='modal_lawyers', size='lg', is_open=False)
            


# ====== Callbacks ======= #
# Tabela com os advogados da empresa
@app.callback(
    Output('table_adv', 'children'),
    Input('store_adv', 'data')
)
def table(data):
    df = pd.DataFrame(data)
    df = df.fillna('-')
    return [
        dash_table.DataTable(
            id='datatable',
            columns=[{'name': i, 'id': i} for i in df.columns],
            data = df.to_dict('records'),
            page_size=10,
            page_current=0
        )
    ]

