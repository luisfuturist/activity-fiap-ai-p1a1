# activity-farmtech


## Introdução

Este projeto foi desenvolvido pela FarmTech Solutions para implementar soluções de Agricultura Digital em uma fazenda. O objetivo é aumentar a produtividade através do gerenciamento eficiente de dados agrícolas, incluindo cálculos de área de plantio e manejo de insumos.

## Estrutura do Projeto

- **diagrams/**: Contém diagramas de contexto, contêiner e componentes.
    - `component-context.dsl`
    - `container-context.dsl`
    - `system-context.dsl`
- **farm-tech-consulting/**: Diretório principal do código Python.
    - `agricultural_management.py`: Script principal da aplicação.
- **weather-r/**: Diretório para scripts em R.
    - `install_packages.R`: Script para instalação de pacotes necessários.
    - `weather.R`: Script para conexão com API meteorológica.
- **.gitignore**: Arquivo para ignorar arquivos desnecessários no controle de versão.

## Pré-requisitos

- **Software**:
    - Visual Code ou Google Colab
    - Python 3.8 ou superior
    - R
- **Bibliotecas Python**: Nenhuma biblioteca externa necessária.
- **Bibliotecas R**: `httr`, `jsonlite`, `dotenv`
- **Hardware**: Computador com acesso à internet para conexão com API.

## Configuração

1. **Clone o repositório**:
    
    ```bash
    git clone [repository_url]
    ```
    
2. **Instale as bibliotecas R**: Execute `install_packages.R` no Visual Code para instalar as bibliotecas necessárias.
3. **Configure a API**:
    - Crie um arquivo `.env` na pasta `weather-r` com a variável `OPEN_WEATHER_API_KEY`.

## Uso

### Python

- Execute o script principal:
    
    ```bash
    python farm-tech-consulting/agricultural_management.py
    ```
    
- Siga as instruções no menu para gerenciar dados agrícolas.

### R

- Execute `weather.R` no Visual Code para obter dados climáticos.

## Testes

- **Python**: Teste manual através do menu interativo.
- **R**: Verifique a saída no console para confirmar a obtenção de dados climáticos.

## Guia de Contribuição

- Fork o repositório e crie uma branch para suas alterações.
- Envie um pull request com uma descrição clara das mudanças.
- Siga as convenções de codificação do projeto.

## Contato

Para dúvidas ou suporte, entre em contato com os membros do grupo:

- Lucas Ferreira Hillesheim: [lucas.ferreira.hillesheim@gmail.com](mailto:lucas.ferreira.hillesheim@gmail.com)
- Luís Fillipe Emidio: [luisfuturist@gmail.com](mailto:luisfuturist@gmail.com)
- Ederson Luiz Badeca dos Santos: [edersonbadeca@gmail.com](mailto:edersonbadeca@gmail.com)
- Caio Rodrigues Castro: [caiorcastro@gmail.com](mailto:caiorcastro@gmail.com)
- Felipe Soares Nascimento: [consultor.casteliano@gmail.com](mailto:consultor.casteliano@gmail.com)