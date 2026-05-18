# Cogs no Diretório Raiz

Exemplo didático em que os Cogs ficam no mesmo diretório do `main.py`.

```text
.
├── .env.example
├── main.py
├── ping.py
└── requirements.txt
```

## Como Executar

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
python main.py
```

Antes de executar, edite o `.env`:

```env
DISCORD_TOKEN=coloque_o_token_do_bot_aqui
GUILD_ID=123456789012345678
```

Neste exemplo, o `setup_hook` procura arquivos `.py` no diretório atual e carrega cada arquivo como extensão, ignorando o próprio `main.py`.

Veja a explicação completa no [README principal](../README.md).
