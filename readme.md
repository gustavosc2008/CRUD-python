CRUD Básico em Python (JSON)
Este é um projeto simples de CRUD (Create, Read, Update, Delete) desenvolvido em Python, utilizando um arquivo JSON como forma de armazenamento.
A ideia inicial era criar um sistema básico sem depender de banco de dados externos, apenas com leitura e escrita em arquivo.

Contexto
Este projeto começou há algum tempo como um rascunho incompleto. A proposta era ter um CRUD funcional, mas só parte dele havia sido implementada.
Recentemente decidi retomar e concluir o projeto, deixando-o funcional e pronto para uso como exemplo de estudo.

Funcionalidades
Criar registros (nome e idade).

Listar todos os registros salvos.

Atualizar registros existentes pelo ID.

Deletar registros pelo ID.

Interface simples via menu no terminal.

Como funciona
Os dados são armazenados em um arquivo dados.json.

Cada registro possui:

id (gerado automaticamente)

nome

idade

O programa apresenta um menu interativo para inserir e gerenciar os registros.

Como executar
git clone <url do repositorio>
no terminal, execute main.py