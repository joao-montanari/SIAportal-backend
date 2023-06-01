import ormar
from fastapi import APIRouter, Response

from models.curso import Curso
from models.requests.curso_update import CursoUpdate

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
        return curso
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
    
@router.patch('/{curso_id}')
async def change_curso(curso_atualizado : CursoUpdate, curso_id : int, response : Response):
    try:
        curso_salvo = await Curso.objects.get(id = curso_id)
        props_atualizadas = curso_atualizado.dict(exclude_unset=True)
        await curso_salvo.update(**props_atualizadas)
        return curso_salvo
    except:
        response.status_code = 404
        return {'mensagem' : 'curso de id nao encontrado'}