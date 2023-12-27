# Api de Cadastro

## Breve Resumo:

Este é um Programa que cadastra um usuário no banco de dados mysql com o xampp.

no programa pode-se modificar alguns valores como seu nome, email e a senha

assim como tbm é possível deletar o usuário

## Tecnologias usadas:

- Python

- mysql

O banco de Dados utilizado foi um no localhost nomeado "python" com apenas uma tabela "user",

com suas respectivas colunas: id, nome, email e senha



Para utilizar o código é nescessário inicializar o mysql e criar um banco de dados nomeado "python".

Logo em seguida, criar uma tabela "user" com os seguintes valores: (`id` INT NOT NULL AUTO_INCREMENT, `Nome` VARCHAR(50) NOT NULL, `Email` VARCHAR(50) NOT NULL, `Senha` VARCHAR(10) NOT NULL, PRIMARY KEY (`id`))ENGINE = InnoDB;



IMPORTANTE USAR OS MESMOS VALORES CITADOS NAS INSTRUÇÕES ACIMA, PARA QUE O CÓDIGO FUNCIONE.


