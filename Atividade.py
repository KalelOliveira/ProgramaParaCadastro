email="Não informado"
senha="Não informado"
idade="Não informado"
telefone="Não informado"
nome="Não informado"
a=0
while a==0:
    print("1-Cadastro\n2-Ler\n3-Deletar\n4-Atualizar\n5-Sair")
    op=int(input("Escolha a opção desejada: "))
    if op!=1 and op!=2 and op!=3 and op!=4 and op!=5:
        y=0
        while y==0:
            print("Escolha uma opção válida")
            op=int(input("Escolha a opção desejada: "))
            if op==1:
                y=1
                g=0
            if op==2:
                y=1
                f=0
            if op==3:
                y=1
                h=1
            if op==4:
                y=1
                hi=0
            if op==5:
                y=1
                miau=0
    if op==1:
        g=0
        while g==0:
            email=str(input("E-mail: "))
            senha=str(input("Senha: "))
            idade=str(input("Idade: "))
            telefone=str(input("Telefone: "))
            nome=str(input("Nome completo: "))
            ki=0
            while ki==0:
                escolha=int(input("Digite 1 para confirmar dados ou 2 para não confirmar: "))
                if escolha==1:
                    print("Dados salvos\n")
                    g=1
                    ki=1
                if escolha==2:
                    ki=1
                    g=0
                if escolha!=1 and escolha!=2:
                    print("Escolha uma opção válida")
                    ki=0
    if op==2:
        f=0
        while f==0:
            print("_______Dados_______")
            print("E-mail: ",email)
            print("Senha: ",senha)
            print("Idade: ",idade)
            print("Telefone: ",telefone)
            print("Nome completo: ",nome,"\n")
            f=1
    if op==3:
        h=0
        while h==0:
            if email=="Não informado" and senha=="Não informado" and idade=="Não informado" and telefone=="Não informado" and nome=="Não informado":
                print("E-mail: ",email)
                print("Senha: ",senha)
                print("Idade: ",idade)
                print("Telefone: ",telefone)
                print("Nome completo: ",nome,"\n")
                print("Faça seu cadastro primeiro para depois deletar\n")
                h=1
            if email!="Não informado" or senha!="Não informado" or idade!="Não informado" or telefone!="Não informado" or nome!="Não informado":
                print("1-E-mail: ",email)
                print("2-Senha: ",senha)
                print("3-Idade: ",idade)
                print("4-Telefone: ",telefone)
                print("5-Nome completo: ",nome,)
                print("6-Deletar todos\n")
                k=0 
                while k==0:
                    deletado=int(input("O que você deseja deletar? "))
                    if deletado==1:
                        print("E-mail deletado\n")
                        email="Não informado"
                        k=1
                        h=1
                    if deletado==2:
                        print("Senha deletada\n")
                        senha="Não informado"
                        k=1
                        h=1
                    if deletado==3:
                        print("Idade deletada\n")
                        idade="Não informado"
                        k=1
                        h=1
                    if deletado==4:
                        print("Telefone deletado\n")
                        telefone="Não informado"
                        k=1
                        h=1
                    if deletado==5:
                        print("Nome completo deletado\n")
                        nome="Não informado"
                        k=1
                        h=1
                    if deletado==6:
                        print("Todos os campos foram deletados\n")
                        email="Não informado"
                        senha="Não informado"
                        idade="Não informado"
                        telefone="Não informado"
                        nome="Não informado"
                        k=1
                        h=1
                    if deletado!=1 and deletado!=2 and deletado!=3 and deletado!=4 and deletado!=5 and deletado!=6:
                        print("Escolha uma opção válida")
                        k=0
    if op==4:
        hi=0
        while hi==0:
            print("1-E-mail: ",email)
            print("2-Senha: ",senha)
            print("3-Idade: ",idade)
            print("4-Telefone: ",telefone)
            print("5-Nome completo: ",nome,)
            print("6-Atualizar todos\n")
            ni=0
            while ni==0:
                atualizado=int(input("O que você deseja atualizar? "))
                if atualizado==1:
                    v=0
                    while v==0:
                        email=str(input("E-mail: "))
                        ba=0
                        while ba==0:
                            atual=int(input("Digite 1 para confirmar ou 2 para não confirmar: "))
                            if atual==1:
                                print("E-mail atualizado\n")
                                ba=1
                                v=1
                                ni=1
                                hi=1
                            if atual==2:
                                ba=1
                                v=0
                            if atual!=1 and atual!=2:
                                print("Escolha uma opção válida")
                                ba=0
                if atualizado==2:
                    w=0
                    while w==0:
                        senha=str(input("Senha: "))
                        vo=0
                        while vo==0:
                            atual=int(input("Digite 1 para confirmar ou 2 para não confirmar: "))
                            if atual==1:
                                print("Senha atualizada\n")
                                vo=1
                                w=1
                                ni=1
                                hi=1
                            if atual==2:
                                vo=1
                                w=0
                            if atual!=1 and atual!=2:
                                print("Escolha uma opção válida")
                                vo=0
                if atualizado==3:
                    e=0
                    while e==0:
                        senha=str(input("Idade: "))
                        jo=0
                        while jo==0:
                            atual=int(input("Digite 1 para confirmar ou 2 para não confirmar: "))
                            if atual == 1:
                                print("Idade atualizada\n")
                                jo=1
                                e=1
                                ni=1
                                hi=1
                            if atual == 2:
                                jo = 1
                                e=0
                            if atual !=1 and atual != 2:
                                print("Escolha uma opção válida")
                                jo=0
                if atualizado==4:
                    t=0
                    while t==0:
                        senha=str(input("Telefone: "))
                        p=0
                        while p==0:
                            atual=int(input("Digite 1 para confirmar ou 2 para não confirmar: "))
                            if atual == 1:
                                print("Telefone atualizado\n")
                                p=1
                                t=1
                                ni=1
                                hi=1
                            if atual == 2:
                                p=1
                                t=0
                            if atual !=1 and atual != 2:
                                print("Escolha uma opção válida")
                                p=0
                if atualizado==5:
                    l=0
                    while l==0:
                        nome=str(input("Nome completo: "))
                        sa=0
                        while sa==0:
                            atual=int(input("Digite 1 para confirmar ou 2 para não confirmar: "))
                            if atual == 1:
                                print("Nome completo atualizado\n")
                                sa=1
                                l=1
                                ni=1
                                hi=1
                            if atual ==2:
                                sa=1
                                l=0
                            if atual !=1 and atual !=2:
                                print("Escolha uma opção válida")
                                sa=0
                if atualizado==6:
                    d=0
                    while d==0:
                        email=str(input("E-mail: "))
                        senha=str(input("Senha: "))
                        idade=str(input("Idade: "))
                        telefone=str(input("Telefone: "))
                        nome=str(input("Nome completo: "))
                        j=0
                        while j==0:
                            atual=int(input("Digite 1 para confirmar ou 2 para não confirmar: "))
                            if atual == 1:
                                print("Dados atualizados\n")
                                j=1
                                d=1
                                ni=1
                                hi=1
                            if atual == 2:
                                j=1
                                d=0
                            if atual !=1 and atual !=2:
                                print("Escolha uma opção válida")
                                j=0
                if atualizado!=1 and atualizado!=2 and atualizado!=3 and atualizado!=4 and atualizado!=5 and atualizado!=6:
                    print("Escolha uma opção válida\n")
                    ni=0
    if op==5:
        miau=0
        while miau==0:
            saida=int(input("Digite 1 para confirmar a saída ou 2 para não confirmar: "))
            if saida==1:
                print("_____Programa encerrado_____")
                miau=1
                a=1
            if saida==2:
                miau=1
                a=0
            if saida!=1 and saida!=2:
                print("Escolha uma opção válida")
                miau=0