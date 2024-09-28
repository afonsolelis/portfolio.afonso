Aqui está um modelo de `README.md` que você pode usar para documentar seu projeto Streamlit. Sinta-se à vontade para ajustar conforme necessário!

```markdown
# Dashboard de Dados de Seguros

[https://github.com/afonsolelis/portfolio.afonso](https://github.com/afonsolelis/portfolio.afonso.git)

Este projeto é um aplicativo Streamlit que permite visualizar dados de seguros armazenados em um banco de dados Supabase. A aplicação oferece tabelas interativas, gráficos e filtros dinâmicos para análise dos dados.

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados:

- Python 3.7 ou superior
- Acesso à internet

## Instalação

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/seu_usuario/nome_do_repositorio.git
   cd nome_do_repositorio
   ```

2. **Crie um ambiente virtual** (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. **Instale as dependências**:
   ```bash
   pip install streamlit supabase
   ```

## Configuração

1. **Obtenha suas credenciais Supabase**:
   - Acesse seu projeto no Supabase e copie a URL e a chave da API.

2. **Atualize as configurações do Supabase**:
   - No arquivo Python (`app.py`), substitua a variável `SUPABASE_KEY` pela sua chave da API:
   ```python
   SUPABASE_KEY = "sua-chave-supabase"  # Substitua pela sua chave
   ```

## Executando o Projeto

Para iniciar o aplicativo, execute o seguinte comando no terminal:

```bash
streamlit run app.py
```

Isso abrirá o aplicativo no seu navegador padrão. Você poderá visualizar e interagir com os dados.

## Funcionalidades

- **Tabela Interativa**: Visualize os dados diretamente em uma tabela.
- **Gráficos de Linhas**: Analise a evolução das `charges` ao longo do tempo.
- **Gráficos de Barras**: Compare o status de fumantes.
- **Filtros Dinâmicos**: Filtre os dados por região.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto é licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.
```

### Como Usar

1. **Clone o repositório**: Use o comando `git clone` e forneça a URL do seu repositório.
2. **Instale as dependências**: Execute `pip install` para garantir que todas as bibliotecas necessárias estejam disponíveis.
3. **Configure as credenciais**: Não se esqueça de adicionar suas credenciais Supabase.
4. **Inicie o aplicativo**: Execute o comando `streamlit run app.py`.

Se você tiver mais informações específicas sobre o seu projeto, adicione ao README para torná-lo ainda mais informativo!