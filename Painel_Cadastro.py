from ConexaoCadastro import con, close, Error
from time import sleep
import os


# Painel Principal #
def menu_principal():
    # os.system("cls")
    print("+-------------------------------+")
    print("| O QUÊ DESEJA FAZER?           |")
    print("|-------------------------------|")
    print("| 1- Inserir um Registro.       |")
    print("| 2- Deletar um Registro.       |")
    print("| 3- Atualizar um Registro.     |")
    print("| 4- Buscar/Filtrar.            |")
    print("| 5- Listar todos os Registros. |")
    print("| 6- Sair.                      |")
    print("+-------------------------------+")

# Função para executar ações no banco de dados (INSERT, DELETE, UPDADE)
def query(sql):
    try:
        vcon = con()
        cursor = vcon.cursor()
        cursor.execute(sql)
        vcon.commit()
    except Error as er:
        print(er)
    finally:
        vcon.close()

# Função de exibir dados no banco de dados (SELECT)
def consultar(sql):
    try:
        vcon = con()
        cursor = vcon.cursor()
        cursor.execute(sql)
        linha = cursor.fetchall()
        return linha
    except:
        print("Erro na Função consultar")
    finally:
        vcon.close()


# Insere dados no banco de dados
def menu_inserir():

    while True:
        vnome = input("Nome: ")
        vemail = input("E-mail: ")
        vsenha = input("Senha (Maximo 10): ")

        if (len(vnome) == 0) or (len(vemail) == 0) or (len(vsenha) == 0):
            print("Argumentos Em Falta!\n")
        else:
            break
    sql = "INSERT INTO `user` VALUE (null,'"+vnome+"', '"+vemail+"', '"+vsenha+"');"
    ret = query(sql)
    if ret == None:
        print("Usuário Cadastrado Com Sucesso!\n")
    else:
        print("Falha Ao Cadastrar O Usuário.")


# Deleta o valor escolhido no banco de dados ||||| por usuario e senha
def menu_deletar():
    vcon = con()

    while True:
        vid = input("Digite Seu ID: ")
        vnome = input("Digite Seu Nome: ")
        vsenha = input("Digite Sua Senha: ")

        if (len(vid) == 0) or (len(vnome) == 0) or (len(vsenha) == 0):
            print("Argumentos Faltando.")
        else:
            break

    cursor = vcon.cursor()
    cursor.execute("SELECT * FROM `user` WHERE `id` = "+vid+" and `Nome` = '"+vnome+"' and `Senha` = '"+vsenha+"';")
    linha = cursor.fetchone()
    l = str(linha)

    if linha == None:
        print("Usuário Não Existe")
        os.system("pause")
    elif (vnome in l) and (vsenha in l) and (vid in l):
        linha = list(linha)
        # Informações do usuário
        print("Suas Informações ::\n")
        print(f"""
        ID: {linha[0]}
        Nome: {linha[1]}
        E-mail: {linha[2]}
        Senha: {linha[3]}\n
        """)

        print("Deseja Excluir Permanentemente Sua Conta?")
        print("1- Sim")
        print("2- Não")
        esc = int(input("> "))

        if esc == 1:
            vsql = "DELETE FROM `user` WHERE `id` = "+vid+" and `Nome` = '"+vnome+"' and `Senha` = '"+vsenha+"';"
            query(vsql)
            print("Sua Conta Foi Excluida!")
            sleep(1)
        elif esc == 2:
            print("Exclusão Cancelada")
            sleep(1)


# Atualiza um ou mais dados
def menu_atualizar():
    # Atualização de conta #
    # Pesquisa por 'ID' e 'SENHA'#
    vid = input("Digite O ID:")
    vsenha = input("Digite Sua Senha: ")
    mostrar = "SELECT * FROM `user` WHERE `id` = "+vid+" and `Senha` = '"+vsenha+"';"
    res = consultar(mostrar)
    res = str(res)
    print("\n",res,"\n")

    try:
        if vid in res and vsenha in res:
            print("Oque Deseja Atualizar?")
            print("1- [Nome]")
            print("2- [E-mail]")
            print("3- [Senha]")
            print("4- [Alterar Tudo]")
            esc = input("> ")

            # Alteração de Nome
            if esc == '1':
                escN = input("Alterar Nome Para: ")
                sql = "UPDATE `user` SET `Nome` = '"+escN+"' WHERE `id` = "+vid+";"
                query(sql)

            # Alteração de email
            elif esc == '2':
                escE = input("Alterar E-mail Para: ")
                sql = "UPDATE `user` SET `Email` = '"+escE+"' WHERE `id` = "+vid+";"
                query(sql)

            # Alteração da senha
            elif esc == '3':
                escS = input("Alterar Senha Para: ")
                sql = "UPDATE `user` SET `Senha` = '"+escS+"' WHERE `id` = "+vid+";"
                query(sql)

            # Alteração de tudo
            elif esc == '4':
                print("Alterar Tudo: ")
                escN = input("Nome: ")
                sql = "UPDATE `user` SET `Nome` = '"+escN+"' WHERE `id` = "+vid+";"
                query(sql)

                escE = input("Email: ")
                sql = "UPDATE `user` SET `Nome` = '"+escN+"' WHERE `id` = "+vid+";" 
                query(sql)

                escS = input("Senha: ")
                sql = "UPDATE `user` SET `Nome` = '"+escN+"' WHERE `id` = "+vid+";"
                query(sql)
            else:
                os.system("cls")
                print("Saindo")
                os.system("pause")
                esc = None
                return esc
    except:
        print("Não Foi Possível Atualizar")
        print("Usuário Inválido Ou Não Existe!")
        os.system("pause")


def menu_buscar():
    opcB = '0'
    while opcB != '3':

        os.system("cls")
        print("Usar Um Filtro Ou Fazer Uma Busca Rapida?")
        print("""
            1- Busca Rapida (ID)
            2- Filtragem (Nome)
            3- Sair
        """)
        opcB = input("> ")

        # Busca Rapida Por ID
        if opcB == '1':

            escB = '0'
            while escB != '2':
                vid = input("ID: ")
                sql = "SELECT * FROM `user` WHERE `id` = "+vid+";"
                ret = consultar(sql)
                res = str(ret)

                if vid in res:
                    os.system("cls")
                    print(f"ID:      {ret[0][0]}")
                    print(f"Nome:    {ret[0][1]}")
                    print(f"E-mail:  {ret[0][2]}")
                    print(f"Senha:   {ret[0][3]}")
                    os.system("pause")
                else:
                    print("O ID Informado Não Existe!\n")
                    os.system("pause")

                # esc = '0'
                while escB != '2':
                    print("\nDeseja Fazer Outra Busca Rapida?")
                    print("1- Sim")
                    print("2- Não")
                    escB = input("> ")

                    if escB == '1':
                        break
                    elif escB == '2':
                        break
                    else:
                        print("Opção Não Encontrada.")
                        sleep(1)
                        os.system("cls")
                        continue

        # Filtragem Por Nomes
        elif opcB == '2':

            escF = '0'
            while escF != '2':
                os.system("cls")
                vnome = input("Nome: ")
                sql = "SELECT * FROM `user` WHERE `Nome` = '"+vnome+"';"
                ret = consultar(sql)
                res = str(ret)

                if vnome in res:
                    for i in ret:
                        print(" ID: {0:_<3} | Nome: {1:_<30} | Email: {2:_<30} | Senha: {3:_<10} \n".format( i[0],i[1],i[2],i[3] ))
                else:
                    print("O Usuário Informado Não Existe")


                while escF != '2':    
                    print("Deseja Fazer Outra Filtragem?")
                    print("1- Sim")
                    print("2- Não")
                    escF = input(">")

                    if escF == '1':
                        break
                    elif escF == '2':
                        continue
                    else:
                        print("Opção Não Encontrada")
                        sleep(1)
                        continue

        # Sai da Função
        elif opcB == '3':
            print("Saindo")
            sleep(0.6)
            break
        else:
            print("Opção não encontrada.")
            sleep(1)
            os.system("cls")


def menu_mostrar():
    sql = "SELECT * FROM `user`"
    ret = consultar(sql)
    os.system('cls')
    for i in ret:
        print(" ID: {0:_<3} | Nome: {1:_<30} | Email: {2:_<30} | Senha: {3:_<10} \n".format( i[0],i[1],i[2],i[3] ))
        sleep(0.06)


esc= ''
while esc != '6':

    menu_principal()
    esc = input("Escolha: ")

    if esc == '1':
        os.system("cls")
        menu_inserir()
    elif esc == '2':
        os.system("cls")
        menu_deletar()
    elif esc == '3':
        os.system("cls")
        menu_atualizar()
    elif esc == '4':
        os.system("cls")
        menu_buscar()
    elif esc == '5':
        os.system("cls")
        menu_mostrar()
    elif esc == '6':
        print("\nFinalizando programa!")
    else:
        print("Opção não encontrada.")
        sleep(0.6)
        os.system("cls")

os.system("pause")
