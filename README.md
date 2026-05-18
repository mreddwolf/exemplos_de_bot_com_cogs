# Exemplos de Bot Discord com Cogs

Projeto didático com três formas simples de organizar comandos de um bot Discord usando `discord.py` e Cogs.

Este repositório não tenta ser um bot completo de produção. A ideia é servir como referência pequena e fácil de copiar para quem está aprendendo a separar comandos em módulos, carregar extensões automaticamente e usar comandos por prefixo, slash e híbridos.

## O Que Este Projeto Demonstra

- Criação de bot com `commands.Bot`.
- Organização de comandos usando Cogs.
- Carregamento automático de extensões.
- Comandos por prefixo, slash commands e hybrid commands.
- Configuração por variáveis de ambiente.
- Estrutura simples para estudo e adaptação.

## Exemplos Disponíveis

| Pasta | O que demonstra |
| --- | --- |
| `cogs_no_diretorio_raiz` | Cogs no mesmo diretório do `main.py`. |
| `cogs_no_subdiretorio` | Cogs dentro da pasta `cogs`. |
| `cogs_no_subdiretorio_do_subdiretorio` | Cogs organizados em subpastas dentro de `cogs`. |

## Comandos Incluídos

Cada exemplo possui os mesmos comandos básicos:

| Comando | Tipo | Descrição |
| --- | --- | --- |
| `!oi` | Prefix command | Responde uma mensagem simples. |
| `/ola` | Slash command | Responde uma mensagem simples via slash. |
| `!ping` ou `/ping` | Hybrid command | Mostra a latência atual do bot. |
| `!servidor` ou `/servidor` | Hybrid command | Mostra um resumo simples do servidor. |

O exemplo `cogs_no_diretorio_raiz` também possui o comando `!sync`, restrito ao dono do bot, para sincronizar comandos manualmente.

## Estrutura Geral

```text
.
├── cogs_no_diretorio_raiz
│   ├── .env.example
│   ├── main.py
│   ├── ping.py
│   └── requirements.txt
├── cogs_no_subdiretorio
│   ├── .env.example
│   ├── cogs
│   │   └── ping.py
│   ├── main.py
│   └── requirements.txt
├── cogs_no_subdiretorio_do_subdiretorio
│   ├── .env.example
│   ├── cogs
│   │   └── ping
│   │       └── ping.py
│   ├── main.py
│   └── requirements.txt
├── LICENSE.md
├── README.md
└── requirements.txt
```

## Pré-requisitos

- Python 3.10 ou superior.
- Um bot criado no Discord Developer Portal.
- O intent `Message Content Intent` habilitado no portal do Discord para usar comandos por prefixo.

## Como Executar Um Exemplo

Escolha uma das pastas de exemplo:

```powershell
cd cogs_no_subdiretorio
```

Crie e ative um ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

Crie o arquivo `.env` a partir do modelo:

```powershell
Copy-Item .env.example .env
```

Edite o `.env` com os dados do seu bot:

```env
DISCORD_TOKEN=coloque_o_token_do_bot_aqui
GUILD_ID=123456789012345678
```

Execute o bot:

```powershell
python main.py
```

## Observações de Segurança

- O arquivo `.env` fica fora do Git.
- Use `.env.example` apenas como modelo.
- Nunca publique o token real do bot.
- O ID do servidor (`GUILD_ID`) também fica no ambiente para evitar valores fixos no código.

## Limites Intencionais

Este projeto foi mantido pequeno de propósito. Ele não inclui banco de dados, dashboard, deploy, filas, logs avançados ou sistema completo de permissões. Esses itens fazem sentido em um bot real, mas aqui o foco é ensinar a estrutura de Cogs sem excesso de abstração.

## Licença

Distribuído sob a licença MIT. Veja [LICENSE.md](LICENSE.md).
