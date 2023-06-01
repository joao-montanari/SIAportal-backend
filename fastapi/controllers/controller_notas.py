import ormar
from fastapi import APIRouter, Response

from models.notas import Notas
from models.requests.notas_update import NotasUpdate

router = APIRouter()

@router.get('/')
async def list_notas():
    return await Notas.objects.all()

@router.post('/')
async def add_notas(notas : Notas):
    await notas.save()
    return notas

@router.get('/{notas_id}')
async def view_notas(notas_id : int, response : Response):
    try:
        notas = await notas.objects.get(id = notas_id)
        return notas
    except:
        response.status_code = 404
        return {'mensagem' : 'notas de id não encontrado'}
    
@router.delete('/{notas_id}')
async def delete_notas(notas_id : int, response : Response):
    try:
        notas = await Notas.objects.get(id = notas_id)
        return await notas.delete()
    except:
        response.status_code = 404
        return {'mensagem' : 'notas de id não encontrado'}
    
@router.patch('/{notas_id}')
async def change_notas(notas_atualizada : Notas, notas_id : int, response : Response):
    try:
        notas_salva = await Notas.objects.get(id = notas_id)
        props_atualizadas = notas_atualizada.dict(exclude_unset=True)
        await notas_salva.update(**props_atualizadas)
        return notas_salva
    except:
        response.status_code = 404
        return {'mensagem' : 'notas de id nao encontrado'}