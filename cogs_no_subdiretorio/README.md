# Cogs em Subdiretório

Exemplo didático em que os Cogs ficam dentro da pasta `cogs`.

```text
.
├── .env.example
├── cogs
│   └── ping.py
├── main.py
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

Neste exemplo, o `setup_hook` procura arquivos `.py` dentro de `cogs` e carrega cada arquivo como extensão.

Veja a explicação completa no [README principal](../README.md).
