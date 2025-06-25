from logging import exception
import dash
import plotly.express as px
from dash import html, dcc, callback_context
from dash.dependencies import Input, Output, State, ALL
import dash_bootstrap_components as dbc
from datetime import timedelta, date

import json
import pandas as pd

from app import app

col_centered_style={'display': 'flex', 'justify-content': 'center'}

# ========= Layout ========= #
layout = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle('Adicione Um Processo')),
    dbc.ModalBody([
        # Linha 1
        dbc.Row([
            # Coluna 1
            dbc.Col([
                # Empresa
                dbc.Label("Empresa", html_for='empresa_matriz'),
                dcc.Dropdown(id='empresa_matriz', clearable=False, className='dbc',
                             options=['Escritório Matriz', 'Filial Porto Alegre', 'Filial Curitiba', 'Filial Itaquera']),
                # Tipo de Processo
                dbc.Label('Tipo de Processo', html_for='tipo_processo'),
                dcc.Dropdown(id='tipo_processo', clearable=False, className='dbc',
                             options=['Civil', 'Criminal', 'Previdenciário', 'Trabalhista', 'Vara da Família'])
            ], sm=12, md=4),
            # Coluna 2
            dbc.Col([
                dbc.Label("Descrição", html_for='input_desc'), # Esta linha tem a função de criar um label para o textarea
                dbc.Textarea(id='input_desc', placeholder='Escreva aqui observações sobre o processo...', style={'height': '80%'}), # Criando o textarea
            ], sm=12, md=8),
        ])
    ])
],id='modal_processo', size='lg', is_open=True)



# ======= Callbacks ======== #
# Callback para abrir o modal


# Callback para CRUD de processos


# Callback pra atualizar o dropdown de advogados
