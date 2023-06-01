import ormar
from fastapi import APIRouter, Response

from models.turma import Turma

router = APIRouter()

@router.get('/')
async def list_turmas():
    return await Turma.objects.all()

@router.post('/')
async def add_turma(turma : Turma):
    await turma.save()
    return turma

@router.get('/{turma_id}')
async def view_turma(turma_id : int, response : Response):
    try:
        turma = await Turma.objects.get(id = turma_id)
        return await turma
    except:
        response.status_code = 404
        return {'mensagem' : 'turma de id não encontrado'}
    
@router.delete('/{turma_id}')
async def delete_turma(turma_id : int, response : Response):
    try:
        turma = await Turma.objects.get(id = turma_id)
        return await turma.delete()
    except:
        response.status_code = 404
        return {'mensagem' : 'turma de id não encontrado'}