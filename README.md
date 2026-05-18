# Exemplo de Bot Discord com Cogs e comandos hibridos.

### O uso deste projeto requer atribuição, leia a [Licença MIT](https://github.com/MrEddwolf/exemplos_de_bot_com_cogs/blob/main/lisense.md) com atenção:

Este é um projeto basico, com **3 exemplo de bot Discord com cogs**, que desenvolvido em `Python` usando a biblioteca `discord.py`.

Os bots possui funcionalidades básicas, limitando-se a comandos que apenas retornam uma frase descrevendo o tipo de comando usado, e o comando ping.

Seu unico objetivo é trazer formas simples de uso dos Cogs e como bonus a possibilidade do uso de Comandos hibridos.

##### Porque criei este projeto?

Enquanto desenvolvia meu próprio bot discord, comecei a me deparar com uma série de dificuldades:

>- Meu código foi ficando cada vez mais extenso.
>- Encontrar partes especificas do código era muito demorado.
>- Ficou cada vez mais difícil realizar manutenções.

Com todos esses problemas diante de mim fui pesquisar uma solução, foi quando descobri a existencia dos cogs. No entanto meu problema não chegou ao fim, pois precisei pesquisar conteúdo extrangeiro para conseguir aprender a criar cogs.

Isso martelou em minha cabeça por meses, foi tão dificil que decidi criar este projeto para ajudar outras pessoas a entender o asunto, sem ter que passar por todos os perrengues que passei!

#### Funcionalidades:

- Carrega automaticamente todos os cogs.
- Executa comandos por prefixo ( **!** )
- Executa comandos de barra ( **/** )
- Executa Comandos hibridos ( **!** ) ou ( **/** )

### Bot com Cogs na pasta root (cogs_no_diretorio_raiz):

Todos os arquivos deste projeto estão na pasta raiz, e não existem subpastas. No entanto todos os comandos do bot estão em arquivos separados, num metodo denominado cogs.

Os arquivos deste projeto estão dispostos como na representação abaixo:

    📁root  
    ├─ 📋 README.md  
    ├─ 📄 requirements.txt  
    ├─ 🔒 .env  
    ├─ 🐍 main.py  
    └─ 🐍 ping.py  

#### Adicionando novos cogs:

 Para adicionar um novo cog basta criar o arquivo e adiciona-lo a pasta raiz.

    📁root  
    ├─ 📋 README.md  
    ├─ 📄 requirements.txt  
    ├─ 🔒 .env  
    ├─ 🐍 main.py  
    ├─ 🐍 ping.py 
    └─ 🐍 novo.py 

### Bot com Cogs na pasta cogs:

Os arquivos de configuração e o arquivo principal `main.py` deste projeto estão na pasta raiz, já os comandos estão no arquivo `ping.py` em `cogs_no_subdiretorio > cogs`.

Os arquivos deste projeto estão dispostos como na representação abaixo:

    📁root  
    ├─ 📋 README.md  
    ├─ 📄 requirements.txt  
    ├─ 🔒 .env  
    ├─ 🐍 main.py  
    └─📁cogs 
      └─ 🐍 ping.py

#### Adicionando novos cogs:

Para adicionar um novo cog basta criar o arquivo e adiciona-lo ao subdiretório cogs.

    📁root  
    ├─ 📋 README.md  
    ├─ 📄 requirements.txt  
    ├─ 🔒 .env  
    ├─ 🐍 main.py  
    └─📁cogs 
      ├─ 🐍 ping.py
      └─ 🐍 novo.py

### Bot com Cogs no subdiretório da pasta cogs :

Os arquivos de configuração e o arquivo principal `main.py` deste projeto estão na pasta raiz, já os comandos estão no arquivo `ping.py` em `cogs_no_subdiretorio_do_subdiretorio > cogs > ping`.

Os arquivos deste projeto estão dispostos como na representação abaixo:

    📁root  
    ├─ 📋 README.md  
    ├─ 📄 requirements.txt  
    ├─ 🔒 .env  
    ├─ 🐍 main.py  
    └─📁cogs
      └─📁ping
        └─ 🐍 ping.py

#### Adicionando novos cogs ao módulo ping:

 para adicionar um novo cog basta criar o arquivo e adiciona-lo ao diretório cogs.

    📁root  
    ├─ 📋 README.md  
    ├─ 📄 requirements.txt  
    ├─ 🔒 .env  
    ├─ 🐍 main.py  
    └─📁cogs
      └─📁ping
        ├─ 🐍 ping.py 
        └─ 🐍 novo.py

#### Adicionando um novo módulo aos cogs:

 para adicionar um novo modulo aos cogs basta criar o subdiretório dentro do diretório cogs e criar um novo cog dentro dele.

    📁root  
    ├─ 📋 README.md  
    ├─ 📄 requirements.txt  
    ├─ 🔒 .env  
    ├─ 🐍 main.py  
    └─📁cogs
      └─📁ping
      │ └─ 🐍 ping.py
      └─📁novo
         └─ 🐍 novo.py


### Pré-requisitos

- Python 3.7 ou superior
- Pacotes Python: `discord.py` e `dotenv`

### Instalação

1. Clone este repositório:

<pre>
  <code>
    <span>git clone https://github.com/MrEddwolf/exemplos_de_bot_com_cogs</span>
  </code>
</pre>

2. Navegue até o diretório do projeto:

<pre class="code">
  <code>
 <span>CD bot-discord (ou o caminho para seu diretório)</span>
  </code>
</pre>

3. Instale as dependências:

<pre>
  <code>
    <span>pip install -r requirements.txt</span>
  </code>
</pre>

4. Configure as variáveis de ambiente:

- Abra o arquivo `.env` do projeto e localize o seguinte conteúdo:

<pre>
  <code>
 <span>DISCORD_TOKEN =token-do-seu-bot</span>
  </code>
</pre>

- Substitua ***token-do-seu-bot*** pelo token do seu bot Discord.

- Abra o arquivo `main.py` em seu editor de texto favorito e localize o seguinte conteúdo.

<pre>
  <code>
 <span>server_id = discord.Object(id= seu_id_aqui)
  </code>
</pre>

- Substitua ***seu_id_aqui*** pelo id do Servidor Discord.

### Uso

#### Execute o arquivo `main.py` para iniciar o bot:

- digite o codigo a seguir no terminal:

<pre>
  <code>
 <span>py main.py</span>
  </code>
</pre>

- caso ocorra um erro  você pode tentar:

<pre>
  <code>
 <span>python main.py</span>
  </code>
</pre>

O bot se conectará ao servidor e estará pronto para edição e testes.

### Contribuição

Contribuições são bem-vindas! Se você encontrar problemas ou tiver sugestões, fique à vontade para abrir uma issue ou enviar um pull request.

### Licença: 

Este projeto está licenciado sob a [Licença MIT](https://github.com/MrEddwolf/exemplos_de_bot_com_cogs/blob/main/lisense.md).

Lembre-se de que este bot Discord está sujeito aos Termos de Serviço e Diretrizes da API do Discord. Você é responsável por cumprir todas as obrigações legais e diretrizes aplicáveis ao uso deste bot Discord.
