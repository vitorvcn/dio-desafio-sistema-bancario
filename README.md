# dio-desafio-sistema-bancario
Desafio para a DIO de criar um sistema bancario em python


## Desafio Versão V1

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: deposito, saque e extrato.

### Operação de depósito

Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de saque

O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.


### Operação de extrato

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: `Não foram realizados movimentações.`

Os valores devem ser exibidos utilizando o formato `R$ xxx.xx`.

Exemplo:
1500.45 = R$ 1500.45


## Desafio Versão V2

1. Separar as funções existentes de saque, depósito e extrato em funções.
2. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária


Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar extrato. ALem disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário).

### Separar em funções

Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos neste módulo, cada função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamados, pode ser definida por você da forma que achar melhor.

### Função Saque

A função saque deve receber os argumentos apenas por nome (keyword only).
Sugestão de argumentos:
1. saldo
2. valor
3. extrato
4. limite
5. numero_saques
6. limite_saques

Sugestão de retorno:
1. Saldo e extrato

### Função Depósito

A função depósito deve receber os argumentos apenas por posição (positional only). 
Sugestão de argumentos:
1. Saldo
2. Valor
3. Extrato

Sugestão de retorno:
1. Saldo e extrato

### Função Extrato

A função extrato deve receber os argumentos por posição e nome (positional only e keyword only).
Argumentos posicionais:
1. Saldo

Argumentos nomeados:
1. Extrato

### Novas funções

Precisamos criar duas novas funções:
1. Criar usuário 
2. Criar conta corrente

Fique a vontade para criar novas funções, exemplo:
listar contas

### Criar usuário (Cliente)

O programa deve armazenar os usuários em uma lista, um usuário é composto por:
1. nome
2. data de nascimento
3. CPF - deve ser armazenado apenas os números do CPF, não podemos cadastrar 2 usuários com o mesmo CPF 
4. Endereço - é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado.

### Criar conta corrente

O programa deve armazenar contas em uma lista, uma conta é composta por:
1. Agência - fixo em "0001"
2. Número da conta - é sequencial, iniciando em 1
3. Usuário - um usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

### Dica

Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.