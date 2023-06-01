import ormar
from fastapi import APIRouter, Response

from models.livro import Livro

router = APIRouter()

@router.get('/')
async def list_livros():
    return await Livro.objects.all()

@router.post('/')
async def add_livros(livro : Livro):
    await livro.save()
    return livro

@router.get('/{livro_id}')
async def view_livro(livro_id : int, response : Response):
    try:
        livro = await Livro.objects.get(id = livro_id)
        return await livro
    except:
        response.status_code = 404
        return {'mensagem' : 'livro de id não encontrado'}
    
@router.delete('/{livro_id}')
async def delete_livro(livro_id : int, response : Response):
    try:
        livro = await Livro.objects.get(id = livro_id)
        return await livro.delete()
    except:
        response.status_code = 404
        return {'mensagem' : 'livro de id não encontrado'}