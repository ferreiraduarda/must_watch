from models.database import DB_PATH, init_db
import sqlite3
from typing import Optional, Self
init_db()

def conectar():
    return sqlite3.connect(DB_PATH)

class Midia:
    def __init__(self, titulo, tipo, indicado_por=None, id_midia: Optional[int] =None) -> None:
        self.id_midia: Optional[int] =  id_midia
        self.titulo = titulo
        self.tipo = tipo
        self.indicado_por = indicado_por

    def salvar(self):
        with conectar() as con:
            con.execute(
                "INSERT INTO midias (titulo, tipo, indicado_por) VALUES (?, ?, ?)",
                (self.titulo, self.tipo, self.indicado_por)
            )

    def atualizar(self):
        if self.id_midia is None:
            return
        with conectar() as con:
            con.execute(
                "UPDATE midias SET titulo=?, tipo=?, indicado_por=? WHERE id=?",
                (self.titulo, self.tipo, self.indicado_por, self.id_midia)
            )

    def excluir(self):
        if self.id_midia is None:
            return
        with conectar() as con:
            con.execute("DELETE FROM midias WHERE id=?", (self.id_midia,))

    @classmethod
    def id(cls, id: int) -> Self:
        with conectar() as con:
            dado = con.execute("SELECT * FROM midias WHERE id=?", (id,)).fetchone()
        if dado is None:
            raise ValueError
        return cls(dado[1], dado[2], dado[3], dado[0])

    @staticmethod
    def obter_todos():
        with conectar() as con:
            dados = con.execute("SELECT * FROM midias").fetchall()
        return [Midia(d[1], d[2], d[3], d[0]) for d in dados]
