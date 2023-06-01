import ormar
from fastapi import APIRouter, Response

from models.aluno import Aluno
from models.requests.aluno_update import AlunoUpdate

router = APIRouter()

@router.get('/')
async def list_alunos():
    return await Aluno.objects.all()

@router.post('/')
async def add_aluno(aluno : Aluno):
    await aluno.save()
    return aluno

@router.get('/{aluno_id}')
async def view_aluno(aluno_id : int, response : Response):
    try:
        aluno = await Aluno.objects.get(id = aluno_id)
        return aluno
    except:
        response.status_code = 404
        return {'mensagem' : 'aluno de id nao encontrado'}
    
@router.delete('/{aluno_id}')
async def delete_aluno(aluno_id : int, response : Response):
    try:
        aluno = await Aluno.objects.get(id = aluno_id)
        return await aluno.delete()
    except:
        response.status_code = 404
        return {'mensagem' : 'aluno de id nao encontrado'}
    
@router.patch('/{aluno_id}')
async def change_aluno(aluno_atualizado : AlunoUpdate, aluno_id : int, response : Response):
    try:
        aluno_salvo = await Aluno.objects.get(id = aluno_id)
        props_atualzadas = aluno_atualizado.dict(exclude_unset = True)
        await aluno_salvo.update(**props_atualzadas)
        return aluno_salvo
    except:
        response.status_code = 404
        return {'mensagem' : 'aluno de id nao encontrado'}