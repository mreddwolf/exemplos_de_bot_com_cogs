# Cogs em Subdiretórios de Cogs

Exemplo didático em que os Cogs ficam organizados em subpastas dentro de `cogs`.

```text
.
├── .env.example
├── cogs
│   └── ping
│       └── ping.py
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

Neste exemplo, o `setup_hook` percorre os subdiretórios de `cogs` e carrega os arquivos `.py` encontrados em cada módulo.

Veja a explicação completa no [README principal](../README.md).
