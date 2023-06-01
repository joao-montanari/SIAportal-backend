import ormar
from fastapi import APIRouter, Response

from models.materia import Materia

router = APIRouter()

@router.get('/')
async def list_materias():
    return await Materia.objects.all()

@router.post('/')
async def add_materia(materia : Materia):
    await materia.save()
    return materia

@router.get('/{materia_id}')
async def view_materia(materia_id : int, response : Response):
    try:
        materia = await materia.objects.get(id = materia_id)
        return await materia
    except:
        response.status_code = 404
        return {'mensagem' : 'materia de id não encontrado'}
    
@router.delete('/{materia_id}')
async def delete_materia(materia_id : int, response : Response):
    try:
        materia = await Materia.objects.get(id = materia_id)
        return await materia.delete()
    except:
        response.status_code = 404
        return {'mensagem' : 'materia de id não encontrado'}