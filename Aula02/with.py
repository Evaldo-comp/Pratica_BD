import sqlite3
from contextlib import closing

dados = [
    ("João","111-111"),
    ("Edinara","222-222"),
    ("Jonas","333-333"),
    ("Raquel","444-444")
]

#busca = input("Digite um nome para buscar: ")
with sqlite3.connect("agenda2.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        # cursor.execute(
        #     """
        #     create table agenda2
        #     (
        #         nome text,
        #         telefone text
        #     )
        #     """
        # )
        # cursor.executemany(
        #     """
        #     insert into agenda2(nome, telefone) values(?,?)
        #     """,(dados)
        # )
        # busca
        # cursor.execute("select * from agenda2 where nome = ? ",(busca,))
        # while True:
        #     resultado = cursor.fetchone()
        #     if resultado is None:
        #         break
        #     print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")
        # cursor.execute(
        #     """
        #         update agenda2
        #         set telefone = '000-000'
        #         where nome = 'Jonas'
        #     """)
        cursor.execute(""" delete from agenda2
                            where nome = 'Jonas' """)
        print("Registros Deletados: ", cursor.rowcount)
        if cursor.rowcount == 2:
            conexao.commit()
            print("Alteração realizada")
        else:
            conexao.rollback()
            print("Abortar operação")
#conexao.commit()

