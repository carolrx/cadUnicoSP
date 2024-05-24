# Feito por Gustavo José da Silva Castro
# gustavocastro20042002@gmail.com

import streamlit as st
from streamlit_echarts import st_echarts
import pandas as pd

# Função para criar os dicionários de opções para cada gráfico
def CriarOpcoesGrafico(titulo, nome, data, tipoGrafico):
    #options = 
    if tipoGrafico == 'Donut':
        options = {
                    "title": {"text": titulo, "left": "center"},
                    "tooltip": {"trigger": "item",
                                "formatter": "<b>{a} <br/>{b}: {c} ({d}%)</b>"}, #Sem essa linha ele não mostra a porcentagem, mas perde a bolinha com a cor que é bonito                    
                    "legend": {"top": "5%", "left": "center"},
                    "series": [{
                        "name": nome,
                        "type": "pie",
                        "radius": ["40%", "70%"],
                        "avoidLabelOverlap": False,
                        "itemStyle": {
                            "borderRadius": 10,
                            "borderColor": "#fff",
                            "borderWidth": 2,
                        },
                        "label": {"show": False, "position": "center"},
                        "emphasis": {
                            "label": {"show": True, "fontSize": "40", "fontWeight": "bold"}
                        },
                        "labelLine": {"show": False},
                        "data": data
                    }]
                  }
    elif tipoGrafico == 'Pizza':
        options = {
                    "title": {"text": titulo, "left": "center"},
                    "tooltip": {"trigger": "item",
                                "formatter": "<b>{a} <br/>{b}: {c} ({d}%)</b>"}, #Sem essa linha ele não mostra a porcentagem, mas perde a bolinha com a cor que é bonito
                    "legend": {"top": "5%", "left": "center"},
                    "series": [{
                                "name": nome,
                                "type": "pie",
                                "radius": "50%",
                                "data": data,
                                "emphasis":{
                                            "itemStyle":{
                                                        "shadowBlur": 10,
                                                        "shadowOffsetX": 0,
                                                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                                                        }
                                            },
                            }     
                            ],
                    }
    elif tipoGrafico == 'Barra':
        options = {
                    "title": {"text": titulo, "left": "center"},
                    "tooltip": {
                                "trigger": "item",
                                "formatter": "<b>{a}<br/>{b} anos: {c} pessoas </b>"
                               },
                    "legend": {"top": "5%", "left": "center"},
                    "xAxis": {
                                "type": "category",
                                "data": data[0],
                             },
                    "yAxis": {
                                "type": "value"
                             },
                    "series": [{
                                "name": nome,
                                "data": data[1], 
                                "type": "bar"
                              }],
                  }
    else:
        options = {
                    "title": [
                                {"text": titulo, "left": "center"},
                            ],
                    "dataset": [{
                                "source": [
                                            data       
                                            ]
                                },
                                {
                                "transform": {
                                            "type": "boxplot",
                                            "config": {"itemNameFormatter": ""},
                                            }
                                },
                                {"fromDatasetIndex": 1, "fromTransformResult": 1},
                            ],
                    "tooltip": {"trigger": "item", "axisPointer": {"type": "shadow"}},
                    "grid": {"left": "10%", "right": "10%", "bottom": "15%"},
                    "xAxis": {
                                "type": "category",
                                "boundaryGap": True,
                                "nameGap": 30,
                                "splitArea": {"show": False},
                                "splitLine": {"show": False},
                            },
                    "yAxis": {
                                "type": "value",
                                "name": nome,
                                "splitArea": {"show": True},
                            },
                    "series": [
                                {"name": "boxplot", "type": "boxplot", "datasetIndex": 1},
                                {"name": "outlier", "type": "scatter", "datasetIndex": 2},
                            ],
                }
    return options

def Filtragem(filtroSexo, filtroRaca, filtroDeficiencia, filtroIdade, filtroRenda, cidadesSelecionadas):
    if filtroSexo != 'Sem Filtro':
    #cod_sexo_pessoa
    #Sexo
    #1 - Masculino
    #2 - Feminino
        if filtroSexo == 'Masculino':
            for i in range(0, len(cidadesSelecionadas)):
                cidadesSelecionadas[i]['Base'] = cidadesSelecionadas[i]['Base'][cidadesSelecionadas[i]['Base']['cod_sexo_pessoa'] == 1]        
            
        if filtroSexo == 'Feminino':
           for i in range(0, len(cidadesSelecionadas)):
                cidadesSelecionadas[i]['Base'] = cidadesSelecionadas[i]['Base'][cidadesSelecionadas[i]['Base']['cod_sexo_pessoa'] == 2]  
    
    if filtroRaca != 'Sem Filtro':
        #cod_raca_cor_pessoa
        #Cor ou raça
        #1 - Branca
        #2 - Preta
        #3 - Amarela
        #4 - Parda
        #5 - Indígena
        if filtroRaca == 'Branca':
           for i in range(0, len(cidadesSelecionadas)):
                cidadesSelecionadas[i]['Base'] = cidadesSelecionadas[i]['Base'][cidadesSelecionadas[i]['Base']['cod_raca_cor_pessoa'] == 1]  

        if filtroRaca == 'Preta':
            for i in range(0, len(cidadesSelecionadas)):
                cidadesSelecionadas[i]['Base'] = cidadesSelecionadas[i]['Base'][cidadesSelecionadas[i]['Base']['cod_raca_cor_pessoa'] == 2]  

        if filtroRaca == 'Amarela':
           for i in range(0, len(cidadesSelecionadas)):
                cidadesSelecionadas[i]['Base'] = cidadesSelecionadas[i]['Base'][cidadesSelecionadas[i]['Base']['cod_raca_cor_pessoa'] == 3]  

        if filtroRaca == 'Parda':
            for i in range(0, len(cidadesSelecionadas)):
                cidadesSelecionadas[i]['Base'] = cidadesSelecionadas[i]['Base'][cidadesSelecionadas[i]['Base']['cod_raca_cor_pessoa'] == 4]

        if filtroRaca == 'Indigena':
            for i in range(0, len(cidadesSelecionadas)):
                cidadesSelecionadas[i]['Base'] = cidadesSelecionadas[i]['Base'][cidadesSelecionadas[i]['Base']['cod_raca_cor_pessoa'] == 5]        
    
    if filtroDeficiencia != 'Sem Filtro':
        #cod_deficiencia_memb
        #Pessoa tem deficiência?
        #1 - Sim
        #2 - Não
        if filtroDeficiencia == 'Possui Deficiência':
            for i in range(0, len(cidadesSelecionadas)):
                cidadesSelecionadas[i]['Base'] = cidadesSelecionadas[i]['Base'][cidadesSelecionadas[i]['Base']['cod_deficiencia_memb'] == 1]              

        if filtroDeficiencia == 'Não Possui Deficiência':
            for i in range(0, len(cidadesSelecionadas)):
                cidadesSelecionadas[i]['Base'] = cidadesSelecionadas[i]['Base'][cidadesSelecionadas[i]['Base']['cod_deficiencia_memb'] == 2]  

    if filtroIdade != 'Sem Filtro':
        #idade
        #Idade calculada a partir da diferença entre a data de nascimento da pessoa e a data de referência da base
        #Dado inteiro de tamanho até 3
        if filtroIdade == 'Primeira Infância (0-5 anos)':
           for i in range(0, len(cidadesSelecionadas)):
                cidadesSelecionadas[i]['Base'] = cidadesSelecionadas[i]['Base'][cidadesSelecionadas[i]['Base']['idade'] <= 5]  

        if filtroIdade == 'Segunda Infância (6-12 anos)':
            for i in range(0, len(cidadesSelecionadas)):
                cidadesSelecionadas[i]['Base'] = cidadesSelecionadas[i]['Base'][(cidadesSelecionadas[i]['Base']['idade'] >= 6) & (cidadesSelecionadas[i]['Base']['idade'] <= 12)]

        if filtroIdade == 'Adolescência Inicial (13-15 anos)':
            for i in range(0, len(cidadesSelecionadas)):
                cidadesSelecionadas[i]['Base'] = cidadesSelecionadas[i]['Base'][(cidadesSelecionadas[i]['Base']['idade'] >= 13) & (cidadesSelecionadas[i]['Base']['idade'] <= 15)]    

        if filtroIdade == 'Adolescência Tardia (16-18 anos)':
            for i in range(0, len(cidadesSelecionadas)):
                cidadesSelecionadas[i]['Base'] = cidadesSelecionadas[i]['Base'][(cidadesSelecionadas[i]['Base']['idade'] >= 16) & (cidadesSelecionadas[i]['Base']['idade'] <= 18)]

        if filtroIdade == 'Juventude Inicial (19-24 anos)':
            for i in range(0, len(cidadesSelecionadas)):
                cidadesSelecionadas[i]['Base'] = cidadesSelecionadas[i]['Base'][(cidadesSelecionadas[i]['Base']['idade'] >= 19) & (cidadesSelecionadas[i]['Base']['idade'] <= 24)]            

        if filtroIdade == 'Juventude Plena (25-30 anos)':
            for i in range(0, len(cidadesSelecionadas)):
                cidadesSelecionadas[i]['Base'] = cidadesSelecionadas[i]['Base'][(cidadesSelecionadas[i]['Base']['idade'] >= 25) & (cidadesSelecionadas[i]['Base']['idade'] <= 30)]

        if filtroIdade == 'Adulto (31-45 anos)':
            for i in range(0, len(cidadesSelecionadas)):
                cidadesSelecionadas[i]['Base'] = cidadesSelecionadas[i]['Base'][(cidadesSelecionadas[i]['Base']['idade'] >= 31) & (cidadesSelecionadas[i]['Base']['idade'] <= 45)]
            
        if filtroIdade == 'Meia-idade (46-60 anos)':
            for i in range(0, len(cidadesSelecionadas)):
                cidadesSelecionadas[i]['Base'] = cidadesSelecionadas[i]['Base'][(cidadesSelecionadas[i]['Base']['idade'] >= 46) & (cidadesSelecionadas[i]['Base']['idade'] <= 60)]        

        if filtroIdade == 'Idoso (60-75 anos)':
            for i in range(0, len(cidadesSelecionadas)):
                cidadesSelecionadas[i]['Base'] = cidadesSelecionadas[i]['Base'][(cidadesSelecionadas[i]['Base']['idade'] >= 60) & (cidadesSelecionadas[i]['Base']['idade'] <= 75)]            

        if filtroIdade == 'Idade Avançada (75 anos ou mais)':
            for i in range(0, len(cidadesSelecionadas)):
                cidadesSelecionadas[i]['Base'] = cidadesSelecionadas[i]['Base'][cidadesSelecionadas[i]['Base']['idade'] >= 75]
            
    if filtroRenda != 'Sem Filtro':
        #val_renda_bruta_12_meses_memb
        #Valor de remuneração bruta no formato NNNNN (sem casas decimais). Ex. Uma remuneração de R$ 125,00 constará na base como 125. 
        if filtroRenda == '0 a 85 Reais':
            for i in range(0, len(cidadesSelecionadas)):
                cidadesSelecionadas[i]['Base'] = cidadesSelecionadas[i]['Base'][(cidadesSelecionadas[i]['Base']['val_renda_bruta_12_meses_memb'] / 12) <= 85]    

        if filtroRenda == '85,01 a 170 Reais':
            for i in range(0, len(cidadesSelecionadas)):
                cidadesSelecionadas[i]['Base'] = cidadesSelecionadas[i]['Base'][((cidadesSelecionadas[i]['Base']['val_renda_bruta_12_meses_memb'] / 12) > 85) & ((cidadesSelecionadas[i]['Base']['val_renda_bruta_12_meses_memb'] / 12) <= 170)]
            
        if filtroRenda == '170,01 a 477 Reais':
            for i in range(0, len(cidadesSelecionadas)):
                cidadesSelecionadas[i]['Base'] = cidadesSelecionadas[i]['Base'][((cidadesSelecionadas[i]['Base']['val_renda_bruta_12_meses_memb'] / 12) > 170) & ((cidadesSelecionadas[i]['Base']['val_renda_bruta_12_meses_memb'] / 12) <= 477)]
           
        if filtroRenda == 'A partir de 477,01 Reais':
            for i in range(0, len(cidadesSelecionadas)):
                cidadesSelecionadas[i]['Base'] = cidadesSelecionadas[i]['Base'][(cidadesSelecionadas[i]['Base']['val_renda_bruta_12_meses_memb'] / 12) > 477]
    
def GraficoRacas(cidadesSelecionadas, configuracoes):
    #cod_raca_cor_pessoa
    #Cor ou raça
    #1 - Branca
    #2 - Preta
    #3 - Amarela
    #4 - Parda
    #5 - Indígena

    def filtraDados(df):
        data = [
                    {"value": None, "name": "Branca"},
                    {"value": None, "name": "Preta"},
                    {"value": None, "name": "Amarela"},
                    {"value": None, "name": "Parda"},
                    {"value": None, "name": "Indígena"}
                ]
        for i in range(1, 6):
            data[i-1]['value'] = len(df[df['cod_raca_cor_pessoa'] == i])
        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Raça/Cor'      
    flag = False 
    for i in range(0, len(cidadesSelecionadas)):
        flag = True
        opcoes_graficos.append((str(cidadesSelecionadas[i]['Nome']), label, filtraDados(cidadesSelecionadas[i]['Base']), configuracoes[2]))

    if flag:
        st.header("Divisão de Raça/Cor da População")

    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def GraficoSexo(cidadesSelecionadas, configuracoes):
    #cod_sexo_pessoa
    #Sexo
    #1 - Masculino
    #2 - Feminino

    def filtraDados(df):
        data = [
                    {"value": None, "name": "Masculino"},
                    {"value": None, "name": "Feminino"}
                ]
        for i in range(1, 3):
            data[i-1]['value'] = len(df[df['cod_sexo_pessoa'] == i])
        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Sexo'
    flag = False  
    for i in range(0, len(cidadesSelecionadas)):
        flag = True
        opcoes_graficos.append((str(cidadesSelecionadas[i]['Nome']), label, filtraDados(cidadesSelecionadas[i]['Base']), configuracoes[2]))
    
    if flag:
        st.header("Divisão de Sexo da População")

    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def GraficoDeficiencia(cidadesSelecionadas, configuracoes):
    #cod_deficiencia_memb
    #Pessoa tem deficiência?
    #1 - Sim
    #2 - Não
    
    def filtraDados(df):
        data = [
                    {"value": None, "name": "Possui Deficiência"},
                    {"value": None, "name": "Não Possui Deficiência"}
                ]
        for i in range(1, 3):
            data[i-1]['value'] = len(df[df['cod_deficiencia_memb'] == i])
        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Possui Deficiência?'
    flag = False  
    for i in range(0, len(cidadesSelecionadas)):
        flag = True
        opcoes_graficos.append((str(cidadesSelecionadas[i]['Nome']), label, filtraDados(cidadesSelecionadas[i]['Base']), configuracoes[2]))
    
    if flag:
        st.header("Divisão de Deficiência da População")

    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def GraficoDistribuiçãoIdade(cidadesSelecionadas, configuracoes):
    #idade
    #Idade calculada a partir da diferença entre a data de nascimento da pessoa e a data de referência da base
    #Dado inteiro de tamanho até 3

    def filtraDados(df):
        data = []
        if configuracoes[2] == 'Boxplot':
            data = [int(x) for x in df['idade']]
            return data
        else:
            idades = df['idade'].value_counts().sort_index()
            
            data.append([int(x) for x in idades.index])
            data.append([int(x) for x in idades.values])
            return data
    
    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Idade'
    flag = False  
    for i in range(0, len(cidadesSelecionadas)):
        flag = True
        opcoes_graficos.append((str(cidadesSelecionadas[i]['Nome']), label, filtraDados(cidadesSelecionadas[i]['Base']), configuracoes[2]))
    
    if flag:
        st.header("Distribuição de Idade da População")
        st.text("Para visualizar melhor este gráfico, ajuste as configurações no menu lateral.")
    
    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                options = CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico)
                st_echarts(options=options, height=configuracoes[1])

def GraficoLerEEscrever(cidadesSelecionadas, configuracoes):
    #cod_sabe_ler_escrever_memb
    #Pessoa sabe ler e escrever?
    #1 - Sim
    #2 - Não

    def filtraDados(df):
        data = [
                    {"value": None, "name": "Não é Analfabeto"},
                    {"value": None, "name": "É Analfabeto"}
                ]
        for i in range(1, 3):
            data[i-1]['value'] = len(df[df['cod_sabe_ler_escrever_memb'] == i])
        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'É Analfabeto?'
    flag = False  
    for i in range(0, len(cidadesSelecionadas)):
        flag = True
        opcoes_graficos.append((str(cidadesSelecionadas[i]['Nome']), label, filtraDados(cidadesSelecionadas[i]['Base']), configuracoes[2]))
    
    if flag:
        st.header("Analfabetismo na População")

    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def GraficoFrenquenciaEscola(cidadesSelecionadas, configuracoes):
    #ind_frequenta_escola_memb
    #Pessoa frequenta escola?
    #1 - Sim, rede pública
    #2 - Sim, rede particular
    #3 - Não, já frequentou
    #4 - Nunca frequentou

    def filtraDados(df):
        data = [
                    {"value": None, "name": "Sim, Frequenta"},
                    {"value": None, "name": "Não, já frequentou"},
                    {"value": None, "name": "Nunca Frequentou"}
                ]
        
        data[0]['value'] = len(df[(df['ind_frequenta_escola_memb'] == 1) | (df['ind_frequenta_escola_memb'] == 2)])
        data[1]['value'] = len(df[df['ind_frequenta_escola_memb'] == 3])
        data[2]['value'] = len(df[df['ind_frequenta_escola_memb'] == 4])

        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Frequenta a Escola?'
    flag = False  
    for i in range(0, len(cidadesSelecionadas)):
        flag = True
        opcoes_graficos.append((str(cidadesSelecionadas[i]['Nome']), label, filtraDados(cidadesSelecionadas[i]['Base']), configuracoes[2]))
    
    if flag:
        st.header("Frequência Escolar da População")

    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def GraficoEscolaPublicaParticular(cidadesSelecionadas, configuracoes):
    #ind_frequenta_escola_memb
    #Pessoa frequenta escola?
    #1 - Sim, rede pública
    #2 - Sim, rede particular
    #3 - Não, já frequentou
    #4 - Nunca frequentou

    def filtraDados(df):
        data = [
                    {"value": None, "name": "Escola Pública"},
                    {"value": None, "name": "Escola Particular"}
                ]
        
        data[0]['value'] = len(df[df['ind_frequenta_escola_memb'] == 1])
        data[1]['value'] = len(df[df['ind_frequenta_escola_memb'] == 2])
    
        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Qual tipo de Escola?'
    flag = False  
    for i in range(0, len(cidadesSelecionadas)):
        flag = True
        opcoes_graficos.append((str(cidadesSelecionadas[i]['Nome']), label, filtraDados(cidadesSelecionadas[i]['Base']), configuracoes[2]))
    
    if flag:
        st.header("Tipos de Escolas Frequentadas Pela População")

    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def GraficoNivelEscolar(cidadesSelecionadas, configuracoes):
    #cod_curso_frequentou_pessoa_memb
    # Curso mais elevado que a pessoa frequentou
    #1 - Creche 2 - Pré-escola (exceto CA) 3 - Classe de Alfabetização - CA 4 - Ensino Fundamental 1ª a 4ª séries, Elementar (Primário), Primeira fase do 1º grau 5 - Ensino Fundamental 5ª a 8ª séries, Médio 1º ciclo (Ginasial), Segunda fase do 1º grau 6 - Ensino Fundamental (duração 9 anos) 7 - Ensino Fundamental Especial 8 - Ensino Médio, 2º grau, Médio 2º ciclo (Científico, Clássico, Técnico, Normal) 9 - Ensino Médio Especial 10 - Ensino Fundamental EJA - séries iniciais (Supletivo 1ª a 4ª) 11 - Ensino Fundamental EJA - séries finais (Supletivo 5ª a 8ª) 12 - Ensino Médio EJA (Supletivo) 13 - Superior, Aperfeiçoamento, Especialização, Mestrado, Doutorado 14 - Alfabetização para Adultos (Mobral, etc.) 15 - Nenhum
    def filtraDados(df):
        data = [
                    {"value": None, "name": "Fundamental 1"},
                    {"value": None, "name": "Fundamental 2"},
                    {"value": None, "name": "Ensino Médio"},
                    {"value": None, "name": "Ensino Superior"}
                ]
        data[0]['value'] = len(df[(df['cod_curso_frequentou_pessoa_memb'] == 4) | (df['cod_curso_frequentou_pessoa_memb'] == 10)])
        data[1]['value'] = len(df[(df['cod_curso_frequentou_pessoa_memb'] == 5) | (df['cod_curso_frequentou_pessoa_memb'] == 6) | (df['cod_curso_frequentou_pessoa_memb'] == 7) | (df['cod_curso_frequentou_pessoa_memb'] == 11)])
        data[2]['value'] = len(df[(df['cod_curso_frequentou_pessoa_memb'] == 8) | (df['cod_curso_frequentou_pessoa_memb'] == 9) | (df['cod_curso_frequentou_pessoa_memb'] == 12)])
        data[3]['value'] = len(df[df['cod_curso_frequentou_pessoa_memb'] == 13]) 
        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Nível Escolar Mais Alto'
    flag = False  
    for i in range(0, len(cidadesSelecionadas)):
        flag = True
        opcoes_graficos.append((str(cidadesSelecionadas[i]['Nome']), label, filtraDados(cidadesSelecionadas[i]['Base']), configuracoes[2]))
    
    if flag:
        st.header("Maior Nível Escolar Frequentado Pela População")

    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def GraficoConclusaoCurso(cidadesSelecionadas, configuracoes):
    #cod_concluiu_frequentou_memb
    #A pessoa concluiu o curso?
    #1 - Sim
    #2 - Não

    def filtraDados(df):
        data = [
                    {"value": None, "name": "Sim, Concluiu o Curso"},
                    {"value": None, "name": "Não Concluiu o Curso"}
                ]
        for i in range(1, 3):
            data[i-1]['value'] = len(df[df['cod_concluiu_frequentou_memb'] == i])
        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Concluiu o Curso?'
    flag = False  
    for i in range(0, len(cidadesSelecionadas)):
        flag = True
        opcoes_graficos.append((str(cidadesSelecionadas[i]['Nome']), label, filtraDados(cidadesSelecionadas[i]['Base']), configuracoes[2]))
    
    if flag:
        st.header("Taxa de Conclusão do Maior Nível de Escolaridade da População")

    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def GraficoFormaDeEnsino(cidadesSelecionadas, configuracoes):
    #cod_curso_frequentou_pessoa_memb
    # Curso mais elevado que a pessoa frequentou
    #1 - Creche 2 - Pré-escola (exceto CA) 3 - Classe de Alfabetização - CA 4 - Ensino Fundamental 1ª a 4ª séries, Elementar (Primário), Primeira fase do 1º grau 5 - Ensino Fundamental 5ª a 8ª séries, Médio 1º ciclo (Ginasial), Segunda fase do 1º grau 6 - Ensino Fundamental (duração 9 anos) 7 - Ensino Fundamental Especial 8 - Ensino Médio, 2º grau, Médio 2º ciclo (Científico, Clássico, Técnico, Normal) 9 - Ensino Médio Especial 10 - Ensino Fundamental EJA - séries iniciais (Supletivo 1ª a 4ª) 11 - Ensino Fundamental EJA - séries finais (Supletivo 5ª a 8ª) 12 - Ensino Médio EJA (Supletivo) 13 - Superior, Aperfeiçoamento, Especialização, Mestrado, Doutorado 14 - Alfabetização para Adultos (Mobral, etc.) 15 - Nenhum
    def filtraDados(df):
        data = [
                    {"value": None, "name": "Ensino Normal"},
                    {"value": None, "name": "Ensino Especial"},
                    {"value": None, "name": "Ensino EJA"},
                ]
        data[0]['value'] = len(df[(df['cod_curso_frequentou_pessoa_memb'] == 3) | (df['cod_curso_frequentou_pessoa_memb'] == 4) | (df['cod_curso_frequentou_pessoa_memb'] == 5) | (df['cod_curso_frequentou_pessoa_memb'] == 6) | (df['cod_curso_frequentou_pessoa_memb'] == 8) | (df['cod_curso_frequentou_pessoa_memb'] == 13)])
        data[1]['value'] = len(df[(df['cod_curso_frequentou_pessoa_memb'] == 7) | (df['cod_curso_frequentou_pessoa_memb'] == 9) | (df['cod_curso_frequentou_pessoa_memb'] == 14)])
        data[2]['value'] = len(df[(df['cod_curso_frequentou_pessoa_memb'] == 10) | (df['cod_curso_frequentou_pessoa_memb'] == 11) | (df['cod_curso_frequentou_pessoa_memb'] == 12)])

        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Tipo de Ensino'
    flag = False  
    for i in range(0, len(cidadesSelecionadas)):
        flag = True
        opcoes_graficos.append((str(cidadesSelecionadas[i]['Nome']), label, filtraDados(cidadesSelecionadas[i]['Base']), configuracoes[2]))
    
    if flag:
        st.header("Forma de Ensino Utilizada Pela População")

    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def GraficoFuncaoTrabalho(cidadesSelecionadas, configuracoes):
    #cod_principal_trab_memb
    # Função principal
    #1 - Trabalhador por conta própria (bico, autônomo) 2 - Trabalhador temporário em área rural 3 - Empregado sem carteira de trabalho assinada 
    #4 - Empregado com carteira de trabalho assinada 5 - Trabalhador doméstico sem carteira de trabalho assinada 
    #6 - Trabalhador doméstico com carteira de trabalho assinada 
    #7 - Trabalhador não-remunerado 8 - Militar ou servidor público 9 - Empregador 10 - Estagiário 11 - Aprendiz

    def filtraDados(df):
        data = [
                    {"value": None, "name": "Trabalhador por conta própria (bico, autônomo)"},
                    {"value": None, "name": "Trabalhador temporário em área rural"},
                    {"value": None, "name": "Empregado sem carteira de trabalho assinada"},
                    {"value": None, "name": "Empregado com carteira de trabalho assinada"},
                    {"value": None, "name": "Trabalhador doméstico sem carteira de trabalho assinada"},
                    {"value": None, "name": "Trabalhador doméstico com carteira de trabalho assinada"},
                    {"value": None, "name": "Trabalhador não-remunerado"},
                    {"value": None, "name": "Militar ou servidor público"},
                    {"value": None, "name": "Empregador"},
                    {"value": None, "name": "Estagiário"},
                    {"value": None, "name": "Aprendiz"}
                ]
        for i in range(1, 12):
            data[i-1]['value'] = len(df[df['cod_principal_trab_memb'] == i])
        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Função Principal do Trabalho'
    flag = False  
    for i in range(0, len(cidadesSelecionadas)):
        flag = True
        opcoes_graficos.append((str(cidadesSelecionadas[i]['Nome']), label, filtraDados(cidadesSelecionadas[i]['Base']), configuracoes[2]))
    
    if flag:
        st.header("Funções Principais da População Com Trabalho")
        st.text("Para visualizar melhor este gráfico, ajuste as configurações no menu lateral.")

    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def GraficoFaixaRenda(cidadesSelecionadas, configuracoes):
    #val_renda_bruta_12_meses_memb
        #Valor de remuneração bruta no formato NNNNN (sem casas decimais). Ex. Uma remuneração de R$ 125,00 constará na base como 125. 
    def filtraDados(df):
        data = [
                    {"value": None, "name": "R$0,00 à R$85,00"},
                    {"value": None, "name": "R$85,01 à R$170,00"},
                    {"value": None, "name": "R$170,01 à R$477,00"},
                    {"value": None, "name": "À Partir de R$477,01"}
                ]
        data[0]['value'] = len(df[(df['val_renda_bruta_12_meses_memb'] / 12) <= 85])
        data[1]['value'] = len(df[((df['val_renda_bruta_12_meses_memb'] / 12) > 85) & ((df['val_renda_bruta_12_meses_memb'] / 12) <= 170)])
        data[2]['value'] = len(df[((df['val_renda_bruta_12_meses_memb'] / 12) > 170) & ((df['val_renda_bruta_12_meses_memb'] / 12) <= 477)])
        data[3]['value'] = len(df[(df['val_renda_bruta_12_meses_memb'] / 12) > 477])

        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Remuneração'
    flag = False  
    for i in range(0, len(cidadesSelecionadas)):
        flag = True
        opcoes_graficos.append((str(cidadesSelecionadas[i]['Nome']), label, filtraDados(cidadesSelecionadas[i]['Base']), configuracoes[2]))
    
    if flag:
        st.header("Porcentagem de Remuneração Mensal da População")
        st.text("Para visualizar melhor este gráfico, ajuste as configurações no menu lateral.")
    
    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def GraficoTrabalho12Meses(cidadesSelecionadas, configuracoes):
    #cod_trabalho_12_meses_memb
    #Pessoa com trabalho remunerado em algum período nos último 12 meses
    #1 - Sim
    #2 - Não
    def filtraDados(df):
        data = [
                    {"value": None, "name": "Sim, Trabalhou"},
                    {"value": None, "name": "Não Trabalhou"}
                ]
        
        data[0]['value'] = len(df[df['ind_frequenta_escola_memb'] == 1])
        data[1]['value'] = len(df[df['ind_frequenta_escola_memb'] == 2])
    
        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Trabalhou de Forma Remunerada nos Últimos 12 Meses?'
    flag = False
    flag = False  
    for i in range(0, len(cidadesSelecionadas)):
        flag = True
        opcoes_graficos.append((str(cidadesSelecionadas[i]['Nome']), label, filtraDados(cidadesSelecionadas[i]['Base']), configuracoes[2]))
    
    if flag:
        st.header("Trabalho Remunerado na População nos Últimos 12 Meses")

    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def TabelaPCDaS(dfPolisPCDaSSP, cidadesSelecionadas):    
    tabela = {
                'Cidade': [],
                'População': [],
                'Nascidos vivos': [],
                'Percentual de Mães 10-14 anos': [],
                'Percentual de Mães 15-17 anos': [],
                'Óbitos': [],
                'Percentual de óbitos': [],
                'Percentual de homicídios': [],
                'Número de suicídios': [],
                'Número de óbitos maternos': [],            
                'Internações hospitalares': [],
                'Percentual de internações atenção primária': [],
                'Percentual de internações saneamento': []
             }
    
    # Garantir que a coluna 'COD_IBGE' é tratada como string
    dfPolisPCDaSSP['COD_IBGE'] = dfPolisPCDaSSP['COD_IBGE'].astype(str)
    flag = False
    
    for i in range(0, len(cidadesSelecionadas)): 
        df = dfPolisPCDaSSP[dfPolisPCDaSSP['COD_IBGE'].str.startswith(str(cidadesSelecionadas[i]['Codigo'])[:6])]
        flag = True
       
        #Montando os dados da tabela
        tabela['Cidade'].append(cidadesSelecionadas[i]['Nome'])
        
        if df['POPULACAO_2019'].isna().all():
            tabela['População'].append('Sem dados')
        else:
            tabela['População'].append(df['POPULACAO_2019'].apply(lambda x: '{:,.0f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).values[0])

        if df['qtd_NASC_2019'].isna().all():
            tabela['Nascidos vivos'].append('Sem dados')
        else:
            tabela['Nascidos vivos'].append(df['qtd_NASC_2019'].apply(lambda x: '{:,.0f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).values[0])

        if df['tx_nasc_mae_10_14_2019'].isna().all():
            tabela['Percentual de Mães 10-14 anos'].append('Sem dados')
        else:
            tabela['Percentual de Mães 10-14 anos'].append(df['tx_nasc_mae_10_14_2019'].apply(lambda x: '{:,.2f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).values[0])

        if df['tx_nasc_mae_15_17_2019'].isna().all():
            tabela['Percentual de Mães 15-17 anos'].append('Sem dados')
        else:
            tabela['Percentual de Mães 15-17 anos'].append(df['tx_nasc_mae_15_17_2019'].apply(lambda x: '{:,.2f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).values[0])

        if df['qtd_OBITOS_2019'].isna().all():
            tabela['Óbitos'].append('Sem dados')
        else:
            tabela['Óbitos'].append(df['qtd_OBITOS_2019'].apply(lambda x: '{:,.0f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).values[0])

        if df['tx_obitos_2019'].isna().all():
            tabela['Percentual de óbitos'].append('Sem dados')
        else:
            tabela['Percentual de óbitos'].append(df['tx_obitos_2019'].apply(lambda x: '{:,.2f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).values[0])

        if df['tx_obitos_homicidio_2019'].isna().all():
            tabela['Percentual de homicídios'].append('Sem dados')
        else:
            tabela['Percentual de homicídios'].append(df['tx_obitos_homicidio_2019'].apply(lambda x: '{:,.2f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).values[0])

        if df['tx_obitos_suicidio_2019'].isna().all():
            tabela['Número de suicídios'].append('Sem dados')
        else:
            tabela['Número de suicídios'].append(df['tx_obitos_suicidio_2019'].apply(lambda x: '{:,.2f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).values[0])

        if df['qtd_obitos_maternos_2019'].isna().all():
            tabela['Número de óbitos maternos'].append('Sem dados')
        else:
            tabela['Número de óbitos maternos'].append(df['qtd_obitos_maternos_2019'].apply(lambda x: '{:,.2f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).values[0])

        if df['qtd_INTERNACOES_2019'].isna().all():
            tabela['Internações hospitalares'].append('Sem dados')
        else:
            tabela['Internações hospitalares'].append(df['qtd_INTERNACOES_2019'].apply(lambda x: '{:,.0f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).values[0])

        if df['tx_interdrsai_2019'].isna().all():
            tabela['Percentual de internações atenção primária'].append('Sem dados')
        else:
            tabela['Percentual de internações atenção primária'].append(df['tx_interdrsai_2019'].apply(lambda x: '{:,.2f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).values[0])

        if df['tx_intersap_2019'].isna().all():
            tabela['Percentual de internações saneamento'].append('Sem dados')
        else:
            tabela['Percentual de internações saneamento'].append(df['tx_intersap_2019'].apply(lambda x: '{:,.2f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).values[0])

    if flag:
        tabela['Cidade'].append('Descrição')
        tabela['População'].append('População para o ano de 2019')
        tabela['Nascidos vivos'].append('Quantidade de nascidos vivos para o ano de 2019')
        tabela['Percentual de Mães 10-14 anos'].append('Participação percentual de meninas de 10 a 14 anos (inclusive) que tiveram filhos nascidos vivos no total de nascidos vivos para o ano de 2019')
        tabela['Percentual de Mães 15-17 anos'].append('Participação percentual de adolescentes de 15 a 17 anos (inclusive) que tiveram filhos nascidos vivos no total nascidos vivos para o ano de 2019')
        tabela['Óbitos'].append('Quantidade de óbitos para o ano de 2019')
        tabela['Percentual de óbitos'].append('Percentual do total de óbitos no total da população para o ano de 2019')
        tabela['Percentual de homicídios'].append('Percentual de óbitos por homicídio no total da população para o ano de 2019')
        tabela['Número de suicídios'].append('Número de óbitos por suicídio, por 100.000 habitantes para o ano de 2019')
        tabela['Número de óbitos maternos'].append('Número de óbitos maternos diretos, por 100.000 nascidos vivos para o ano de 2019')
        tabela['Internações hospitalares'].append('Quantidade de internações hospitalares no ano de 2019')
        tabela['Percentual de internações atenção primária'].append('Participação percentual de internações hospitalares por condições sensíveis à atenção primária no total de internações hospitalares no ano de 2019')
        tabela['Percentual de internações saneamento'].append('Participação percentual de internações hospitalares por doenças relacionadas ao saneamento ambiental inadequado no total de internações hospitalares no ano de 2019')
    
        df = pd.DataFrame(tabela)
        
        # Definindo a coluna 'Cidade' como índice do DataFrame
        df.set_index('Cidade', inplace=True)
        
        df_invertido = df.transpose()
        
        st.header('Dados da Saúde Pólis PCDaS')
        st.text('Dados de saúde e socioeconômicos municipais reunidos e construídos pela Plataforma de Ciência de Dados aplicada à Saúde (PCDaS)')
        # Exibindo a tabela no Streamlit
        st.dataframe(df_invertido)   

def main():
    dfCadUnicoSP = pd.read_csv('CadUnicoSP.csv')
    dfCidadesSPIBGE = pd.read_csv('CidadesSPIBGE.csv')
    dfPolisPCDaSSP = pd.read_csv('PolisPCDaSSP.csv')

    #Substituindo os NaNs da coluna por 0
    dfCadUnicoSP['val_renda_bruta_12_meses_memb'] = dfCadUnicoSP['val_renda_bruta_12_meses_memb'].fillna(0)

    st.set_page_config(
        page_title="CadUnico São Paulo",
        page_icon="📊",
        initial_sidebar_state="expanded",
        layout="wide",
        menu_items={
                    'Get Help': 'https://www.extremelycoolapp.com/help',
                    'Report a bug': "https://www.extremelycoolapp.com/bug",
                    'About': "# This is a header. This is an *extremely* cool app!"
                    }
    )

    with st.sidebar:
        st.markdown("<h1 style='text-align: center;'>Filtros</h1>", unsafe_allow_html=True)        
        
        cidadesSP = dfCidadesSPIBGE.set_index('Nome_Município')['Código Município Completo'].to_dict()
    
        # Lista de nomes de cidades
        nomesCidadesSP = list(cidadesSP.keys())

        # Criação da lista de seleção múltipla
        selecionadas = st.multiselect(f"Escolha uma ou mais cidades", nomesCidadesSP,default = 'São Paulo', placeholder="Escolha uma ou mais cidades")
        st.text('Cuidado! Quanto mais cidades, menor a velocidade da página!')
        
        # Criando uma lista de dicionários com os nomes das cidades e seus respectivos códigos    
        cidadesSelecionadas = [{'Nome': value} for value in selecionadas]
        
        #Adicionando o código ibge das cidades no dicionario
        for dicionario, new_value in zip(cidadesSelecionadas, [cidadesSP[cidade] for cidade in selecionadas]):
            dicionario['Codigo'] = new_value
        
        st.text("Marque os temas que deseja ver:")
        checkDadosGerais = st.checkbox("Dados Gerais", value = True)
        checkEducacao = st.checkbox("Educação")
        checkRendaFinanceira = st.checkbox("Renda Financeira")
        checkSaude = st.checkbox("Saúde")

        st.text("Marque os filtros que deseja aplicar aos dados:")
        with st.expander("Sexo"):
            filtroSexo = st.radio("Qual filtro você deseja aplicar?", ['Sem Filtro', 'Feminino', 'Masculino'])

        with st.expander("Raça/Cor"):
            filtroRaca = st.radio("Qual filtro você deseja aplicar?", ['Sem Filtro', 'Branca', 'Preta', 'Amarela', 'Parda', 'Indígena'])

        with st.expander("Deficiência"):
            filtroDeficiencia = st.radio("Qual filtro você deseja aplicar?", ['Sem Filtro', 'Não Possui Deficiência', 'Possui Deficiência'])

        with st.expander("Idade"):
            filtroIdade = st.radio("Qual faixa de idade você deseja aplicar?", ['Sem Filtro', 'Primeira Infância (0-5 anos)', 'Segunda Infância (6-12 anos)', 'Adolescência Inicial (13-15 anos)', 'Adolescência Tardia (16-18 anos)', 'Juventude Inicial (19-24 anos)', 'Juventude Plena (25-30 anos)', 'Adulto (31-45 anos)', 'Meia-idade (46-60 anos)', 'Idoso (60-75 anos)', 'Idade Avançada (75 anos ou mais)'])

        with st.expander("Renda Mensal"):
            filtroRenda = st.radio("Qual filtro você deseja aplicar?", ['Sem Filtro', '0 a 85 Reais', '85,01 a 170 Reais', '170,01 a 477 Reais', 'A partir de 477,01 Reais'])

        with st.expander("Configurações dos Gráficos"):
            # Definir o número máximo de gráficos por linha e o tamanho inicial dos gráficos
            maxGraficosPorLinha = st.slider("Número máximo de gráficos por linha", min_value=1, max_value=4, value=4)
            tamanhoGrafico = st.slider("Tamanho dos gráficos", min_value=350, max_value=1000, value=350)
            tipoGraficoDonutPizza = st.radio("Qual tipo de gráfico você prefere?", ['Donut', 'Pizza'])
            tipoGraficoBarraBoxplot = st.radio("Qual tipo de gráfico você prefere?", ['Barra', 'Boxplot'])

    for i in range(0, len(cidadesSelecionadas)):
        cidadesSelecionadas[i]['Base'] = dfCadUnicoSP[dfCadUnicoSP['cd_ibge'] == cidadesSelecionadas[i]['Codigo']]

    Filtragem(filtroSexo, filtroRaca, filtroDeficiencia, filtroIdade, filtroRenda, cidadesSelecionadas)
    
    st.markdown("<h1 style='text-align: center;'>Amostra CadÚnico 2018</h1>", unsafe_allow_html=True)

    if checkDadosGerais:
        configuracoes = [maxGraficosPorLinha, tamanhoGrafico, tipoGraficoDonutPizza]

        GraficoRacas(cidadesSelecionadas, configuracoes)
        GraficoSexo(cidadesSelecionadas, configuracoes)
        GraficoDeficiencia(cidadesSelecionadas, configuracoes)
        GraficoDistribuiçãoIdade(cidadesSelecionadas, [maxGraficosPorLinha, tamanhoGrafico, tipoGraficoBarraBoxplot])        
    
    if checkEducacao:
        configuracoes = [maxGraficosPorLinha, tamanhoGrafico, tipoGraficoDonutPizza]

        GraficoLerEEscrever(cidadesSelecionadas, configuracoes)
        GraficoFrenquenciaEscola(cidadesSelecionadas, configuracoes)
        GraficoEscolaPublicaParticular(cidadesSelecionadas, configuracoes)
        GraficoNivelEscolar(cidadesSelecionadas, configuracoes)
        GraficoConclusaoCurso(cidadesSelecionadas, configuracoes)
        GraficoFormaDeEnsino(cidadesSelecionadas, configuracoes)

    if checkRendaFinanceira:
        configuracoes = [maxGraficosPorLinha, tamanhoGrafico, tipoGraficoDonutPizza]

        GraficoFuncaoTrabalho(cidadesSelecionadas, configuracoes)
        GraficoFaixaRenda(cidadesSelecionadas, configuracoes)
        GraficoTrabalho12Meses(cidadesSelecionadas, configuracoes)
    if checkSaude:
        TabelaPCDaS(dfPolisPCDaSSP, cidadesSelecionadas)
main()