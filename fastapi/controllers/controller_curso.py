import ormar
from fastapi import APIRouter, Response

from models.curso import Curso

router = APIRouter()

@router.get('/')
async def list_cursos():
    return await Curso.objects.all()

@router.post('/')
async def add_curso(curso : Curso):
    await curso.save()
    return curso

@router.get('/{curso_id}')
async def view_curso(curso_id : int, response : Response):
    try:
        curso = await Curso.objects.get(id = curso_id)
        return await curso
    except:
        response.status_code = 404
        return {'mensagem' : 'curso de id não encontrado'}
    
@router.delete('/{curso_id}')
async def delete_curso(curso_id : int, response : Response):
    try:
        curso = await Curso.objects.get(id = curso_id)
        return await curso.delete()
    except:
        response.status_code = 404
        return {'mensagem' : 'curso de id não encontrado'}