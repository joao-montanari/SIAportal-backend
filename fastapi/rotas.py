from fastapi import APIRouter

from controllers import controller_aluno as aluno
from controllers import controller_curso as curso
from controllers import controller_livro as livro
from controllers import controller_materia as materia
from controllers import controller_notas as notas
from controllers import controller_professor as professor
from controllers import controller_turma as turma
from controllers import controller_usuario as usuario

router = APIRouter()

router.include_router(aluno.router, prefix = '/alunos')
router.include_router(curso.router, prefix = '/cursos')
router.include_router(livro.router, prefix = '/livros')
router.include_router(materia.router, prefix = '/materias')
router.include_router(notas.router, prefix = '/notas')
router.include_router(professor.router, prefix = '/professores')
router.include_router(turma.router, prefix = '/turmas')
router.include_router(usuario.router, prefix = '/usuarios')