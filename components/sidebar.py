import dash
from dash import html, dcc, callback_context
from dash.dependencies import Input, Output, State, ALL
import dash_bootstrap_components as dbc

import json
import pandas as pd

from components import modal_novo_processo, modal_novo_advogado, modal_advogados
from app import app

# ========= Layout ========= #
layout = dbc.Container([
    modal_advogados.layout,
    modal_novo_advogado.layout,
    modal_novo_processo.layout,
    dbc.Container([
        # Primeira linha chamada "ASIMOV" com cor amarela
        dbc.Row([
            dbc.Col([
                html.H1('ASIMOV', style={'color': 'yellow'})
            ])
        ]),
        # Segunda Linha 'ASSOCIETES' com cor branca
        dbc.Row([
            dbc.Col([
                html.H3('ASSOCIETES', style={'color': 'white'})
            ])
        ])
    ], style={'padding': '50px', 'margin-bottom': '100px'}, className='text-center'),
    html.Hr(),
    # Criando botões de Navegação
    dbc.Row([
        dbc.Col([
            dbc.Nav([
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-home dbc'), '\tINÍCIO'], href='/home', active=True, style={'text-align': 'left'})),
                html.Br(),
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-plus-circle dbc'), '\tPROCESSOS'], href='/', id='processo_button', active=True, style={'text-align': 'left'})),
                html.Br(),
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-user-plus dbc'), '\tADVOGADOS'], href='/', id='lawyers_buttom', active=True, style={'text-align': 'left'})),
            ], vertical='lg', pills=True, fill=True)
        ])
    ])

], style={'height': '100vh', 'padding': '0px', 'position': 'sticky', 'top': '0px', 'background-color': '#232423'})  

# ======= Callbacks ======== #
# Abrir Modal New Lawyer


# Abrir Modal Lawyers
@app.callback(
    Output('modal_lawyers', 'is_open'),
    Input('lawyers_buttom', 'n_clicks'),
    Input('quit_buttom', 'n_clicks'),
    Input('new_adv_buttom', 'n_clicks'), # new_adv_buttom seria o botão de novo advogado
    State('modal_lawyers', 'is_open') # State no contexto modal_lawyers seria o estado do modal_lawyers
)
def toggle_modal(n, n1, n2, is_open):
    if n or n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output('modal_new_lawyer', 'is_open'),
    Input('new_adv_buttom', 'n_clicks'),
    Input('cancel_buttom_novo_advogado', 'n_clicks'),
    State('modal_new_lawyer', 'is_open')
)
def toggle_modal(n, n1, is_open):
    if n or n1:
        return not is_open
    return is_open