import streamlit as st
import pandas as pd
from supabase import create_client, Client

# Configurações do Supabase
SUPABASE_URL = ""
SUPABASE_KEY = ""  # Substitua pela sua chave


# Função para conectar ao Supabase
def get_supabase_client() -> Client:
	return create_client(SUPABASE_URL, SUPABASE_KEY)


# Função para obter dados da tabela
def get_data_from_supabase(supabase: Client):
	response = supabase.table("afonso").select("*").execute()
	return response.data


# Configurando a página
st.title("Dashboard de Dados de Seguros")

# Conectando ao Supabase
supabase_client = get_supabase_client()

# Obtendo dados
data = get_data_from_supabase(supabase_client)

if data:
	# Transformando os dados em DataFrame
	df = pd.DataFrame(data)

	# Expandindo a coluna 'data_linha' que contém dicionários
	df_data_linha = pd.json_normalize(df['data_linha'])
	df = pd.concat([df.drop(columns=['data_linha']), df_data_linha], axis=1)

	# Tabela interativa
	st.subheader("Tabela de Dados")
	st.dataframe(df)

	# Gráfico de Linhas: Charges ao longo do tempo (se a data_ingestao estiver presente)
	if 'data_ingestao' in df.columns:
		df['data_ingestao'] = pd.to_datetime(df['data_ingestao'])
		df.set_index('data_ingestao', inplace=True)
		st.subheader("Gráfico de Linhas de Charges ao longo do Tempo")
		st.line_chart(df['charges'])

	# Gráfico de Barras: Contagem de fumantes
	if 'smoker' in df.columns:
		smoker_counts = df['smoker'].value_counts()
		st.subheader("Gráfico de Barras por Status de Fumante")
		st.bar_chart(smoker_counts)

	# Filtros dinâmicos
	st.subheader("Filtros")
	region_filter = st.selectbox("Escolha uma região:", df['region'].unique())
	filtered_df = df[df['region'] == region_filter]
	st.dataframe(filtered_df)

else:
	st.warning("Nenhum dado encontrado.")
