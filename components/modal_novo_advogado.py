import dash
import plotly.express as px
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd

from app import app

# ========= Layout ========= #
layout = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle('Adicione Um Advogado')),
    dbc.ModalBody([
        dbc.Row([
            dbc.Col([
                dbc.Label('OAB'),
                dbc.Input(id='adv_oab', placeholder='Apenas números, referente a OAB...', type='number')
            ], sm=12, md=6),
            dbc.Col([
                dbc.Label('CPF'),
                dbc.Input(id='adv_cpf', placeholder='Apenas números, CPF...', type='number')
            ], sm=12, md=6),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Label('Advogado'),
                dbc.Input(id='adv_nome', placeholder='Nome completo do advogado...', type='text')
            ]),
        ]),
        html.H5(id='div_erro2')
    ]),
    dbc.ModalFooter([
        dbc.Button('Cancelar', id='cancel_buttom_novo_advogado', color='danger'),
        dbc.Button('Salvar', id='save_buttom_novo_advogado', color='success')
    ])

], id='modal_new_lawyer', size='lg', is_open=False)



# ======= Callbacks ======== #
# Callback para adicionar novos advogados
@app.callback(
    Output('store_adv', 'data'), # Definindo 'store_adv' como output
    Output('div_erro2', 'children'), # Definindo mensagem de erro
    Output('div_erro2', 'style'), # Definindo estilo da mensagem de erro
    Input('save_buttom_novo_advogado', 'n_clicks'), # Definindo 'save_buttom_novo_advogado' como input
    State('store_adv', 'data'), # Definindo tabela
    State('adv_nome', 'value'), # Definindo nome
    State('adv_oab', 'value'), # Definindo oab
    State('adv_cpf', 'value') # Definindo cpf
)

def novo_adv(n, dataset, nome, oab, cpf):
    erro = []
    style = {}

    if n:
        if None in [nome, oab, cpf]:
            return dataset, ['Todos os dados são obrigatórios!'], {'margin-bottom': '15px', 'color': 'red'}
        
        df_adv = pd.DataFrame(dataset)
        # Garante as colunas certas mesmo se o DataFrame estiver vazio ou com colunas erradas
        if df_adv.empty or not all(col in df_adv.columns for col in ['Advogado', 'OAB', 'CPF']):
            df_adv = pd.DataFrame(columns=['Advogado', 'OAB', 'CPF'])
        # Condicões para verificar se dados existem no sistema
        if oab in df_adv['OAB'].values:
            return dataset, ['OAB ja cadastrado!'], {'margin-bottom': '15px', 'color': 'red'}
        if cpf in df_adv['CPF'].values:
            return dataset, ['CPF ja cadastrado!'], {'margin-bottom': '15px', 'color': 'red'}
        elif nome in df_adv['Advogado'].values:
            return dataset, ['Nome ja cadastrado!'], {'margin-bottom': '15px', 'color': 'red'}
        
        # Criando estrutura para o Dataframe
        df_adv.loc[df_adv.shape[0]] = [nome, oab, cpf] # Estrutura do Dataframe
        dataset = df_adv.to_dict()

        return dataset, ['Advogado cadastrado com sucesso!'], {'margin-bottom': '15px', 'color': 'green'}
    return dataset, erro, style