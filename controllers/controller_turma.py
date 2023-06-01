import ormar
from fastapi import APIRouter, Response

from models.turma import Turma
from models.requests.turma_update import TurmaUpdate

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
        return turma
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
    
@router.patch('/{turma_id}')
async def change_turma(turma_atualizada : TurmaUpdate, turma_id : int, response : Response):
    try:
        turma_salva = await Turma.objects.get(id = turma_id)
        props_atualizadas = turma_atualizada.dict(exclude_unset=True)
        await turma_salva.update(**props_atualizadas)
        return turma_salva
    except:
        response.status_code = 404
        return {'mensagem' : 'turma de id nao encontrado'}