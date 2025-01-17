# 👻 Bot de Coleta de Informações para RP Sobrenatural no Discord (FiveM)
Este bot foi desenvolvido para ser utilizado no contexto de um roleplay (RP) sobrenatural no FiveM, especificamente dentro de servidores que envolvem investigações e cenários de terror. Ele coleta informações de jogadores no Discord por meio de reações em um menu, e envia os dados coletados para canais específicos. Cada categoria de evento tem um questionário com perguntas relacionadas ao cenário, como nome do investigador, relato do acontecimento, e envolvidos.

## 📋 Funcionalidades
- Menu de Reações:
    - O bot exibe um menu com reações que permitem ao usuário escolher entre diferentes categorias de relatos.
   - Reações disponíveis:
       - 🪓: Relatos envolvendo "Jason" (ameaça conhecida).
       - ☢️: Relatos de "Ameaça não identificada".
    - Questionário Interativo:
        - Após selecionar uma reação, o usuário responderá uma série de perguntas pré-definidas.
            As respostas são coletadas e exibidas de forma organizada no canal apropriado para cada tipo de relato.

    - Remoção de Mensagens:
        - Para manter o canal de coleta de informações limpo e organizado, tanto as perguntas quanto as respostas do usuário são automaticamente excluídas após o preenchimento.

    - Resumo do Relato:
        - Um resumo com todas as respostas é gerado e enviado a um canal específico para cada tipo de relato:
           - Resumos de relatos do Jason são enviados para um canal.
           - Resumos de ameaças desconhecidas são enviados para outro canal.

## 📜 Estrutura do Código
- Canais de Coleta e Resumo:
    - O bot utiliza IDs específicos de canais para o menu de reações e para o envio dos resumos.

    - Configuração do Bot:
       - O bot utiliza `discord.py` e precisa de permissões adequadas para ler mensagens, reagir, apagar mensagens e enviar mensagens.

## 🖲️ Como Usar
1. Configurando o Bot:
   - Acesse o [Portal de Desenvolvedores do Discord](https://discord.com/developers/applications) e crie um novo aplicativo.
   - No menu lateral, clique em "Bot" e adicione um bot ao seu aplicativo.
   - Copie o token do bot e substitua `'SEU TOKEN'` no código pelo token copiado.
2. Adicionando o Bot ao Servidor:
    - No Portal de Desenvolvedores, vá até a seção "OAuth2" e clique em "URL Generator".
    - Na lista de permissões, selecione as seguintes opções:
        - `bot` (na categoria "Scopes")
        - `Read Messages/View Channels`, `Send Messages`, `Manage Messages`, `Add Reactions` (na categoria "Bot Permissions")
    - Copie a URL gerada e acesse-a no navegador para adicionar o bot ao seu servidor.

3. Atualize as variáveis `MENU_CHANNEL_ID`, `SUMMARY_CHANNEL_ID_JASON`, e `SUMMARY_CHANNEL_ID_PRAGA` com os IDs dos canais desejados.

4. Execute o bot e aguarde a interação dos usuários com as reações no menu.

5. Os resumos serão automaticamente enviados para os canais apropriados após o preenchimento do questionário.

## 📚Requisitos
- Python 3.8+
- Biblioteca ```discord.py``` instalada (```pip install discord.py```)

## ✅ Executando o Bot
1. Clone o repositório para sua máquina local.
2. No terminal, navegue até o diretório do projeto.
3. Substitua 'SEU TOKEN' no código pelo token do seu bot no Discord.
