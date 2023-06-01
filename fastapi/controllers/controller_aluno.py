import ormar
from fastapi import APIRouter, Response

from models.aluno import Aluno

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
        return await aluno
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