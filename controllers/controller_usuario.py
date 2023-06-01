from fastapi import APIRouter, Response
import ormar

from models.usuario import Usuario
from models.requests.usuario_update import UsuarioUpdate

router = APIRouter()

@router.get('/')
async def list_usuarios():
    return await Usuario.objects.all()

@router.post('/')
async def add_usuario(usuario : Usuario):
    await usuario.save()
    return usuario

@router.get('/{usuario_id}')
async def view_usuario(usuario_id : int, response : Response):
    try:
        usuario = await Usuario.objects.get(id = usuario_id)
        return usuario
    except:
        response.status_code = 404
        return {'mensagem' : 'usuario de id nao encontrado'}
    
@router.delete('/{usuario_id}')
async def delete_usuario(usuario_id : int, response : Response):
    try:
        usuario = await Usuario.objects.get(id = usuario_id)
        return await usuario.delete()
    except:
        response.status_code = 404
        return {'mensagem' : 'usuario de id não encontrado'}

@router.patch('/{usuario_id}')
async def change_usuario(usuario_atualizado : UsuarioUpdate, usuario_id : int, response : Response):
    try:
        usuario_salvo = await Usuario.objects.get(id = usuario_id)
        props_atualizadas = usuario_atualizado.dict(exclude_unset=True)
        await usuario_salvo.update(**props_atualizadas)
        return usuario_salvo
    except:
        response.status_code = 404
        return {'mensagem' : 'usuario de id nao encontrado'}