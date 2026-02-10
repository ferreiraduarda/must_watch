from typing import Optional

import sqlite3

DB = "data/mustwatch.db"


def conectar():
    return sqlite3.connect(DB)

class Midia:

    def __init__(self, titulo: str, tipo: str, indicado_por: str, id: Optional[int] = None):
        self.id = id
        self.titulo = titulo
        self.tipo = tipo
        self.indicado_por = indicado_por


    def salvar(self):
        con = conectar()

        con.execute(
            "INSERT INTO midias (titulo, tipo, indicado_por) VALUES (?, ?, ?)",
            (self.titulo, self.tipo, self.indicado_por)
        )

        con.commit()
        con.close()


    @staticmethod
    def obter_todos():
        con = conectar()

        dados = con.execute("SELECT * FROM midias").fetchall()

        con.close()
        return dados


    @staticmethod
    def id(id):
        con = conectar()

        dado = con.execute(
            "SELECT * FROM midias WHERE id=?",
            (id,)
        ).fetchone()

        con.close()

        return Midia(dado[1], dado[2], dado[3], dado[0])


    def excluir(self):
        con = conectar()

        con.execute("DELETE FROM midias WHERE id=?", (self.id,))

        con.commit()
        con.close()


    def atualizar(self):
        con = conectar()

        con.execute(
            "UPDATE midias SET titulo=?, tipo=?, indicado_por=? WHERE id=?",
            (self.titulo, self.tipo, self.indicado_por, self.id)
        )

        con.commit()
        con.close()
