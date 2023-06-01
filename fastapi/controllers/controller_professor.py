import ormar
from fastapi import APIRouter, Response

from models.professor import Professor

router = APIRouter()

@router.get('/')
async def list_professores():
    return await Professor.objects.all()

@router.post('/')
async def add_professor(professor : Professor):
    await professor.save()
    return professor

@router.get('/{professor_id}')
async def view_professor(professor_id : int, response : Response):
    try:
        professor = await Professor.objects.get(id = professor_id)
        return await professor
    except:
        response.status_code = 404
        return {'mensagem' : 'professor de id não encontrado'}
    
@router.delete('/{professor_id}')
async def delete_professor(professor_id : int, response : Response):
    try:
        professor = await Professor.objects.get(id = professor_id)
        return await professor.delete()
    except:
        response.status_code = 404
        return {'mensagem' : 'professor de id não encontrado'}