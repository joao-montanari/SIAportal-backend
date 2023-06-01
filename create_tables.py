import sqlalchemy

from config import DATABASE_URL, metadata
from models.aluno import Aluno
from models.curso import Curso
from models.livro import Livro
from models.materia import Materia
from models.notas import Notas
from models.professor import Professor
from models.turma import Turma
from models.usuario import Usuario

def config_database(database_url = DATABASE_URL):
    engine = sqlalchemy.create_engine(database_url)
    metadata.drop_all(engine)
    metadata.create_all(engine)

if __name__ == '__main__':
    config_database()