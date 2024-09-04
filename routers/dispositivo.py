from fastapi import APIRouter
from models.dispositivo import DispositivoDB, UnidadeConsumidoraDB
from schemas.dispositivo import DispositivoCreate, DispositivoReadList, DispositivoReadOne, DispositivoUpdate

router = APIRouter(prefix='/dispositivos', tags=['DISPOSITIVOS'])

@router.post(path='', response_model=DispositivoReadOne)
def criar_dispositivo(novo_dispositivo: DispositivoCreate):
    dispositivo = DispositivoDB.create(**novo_dispositivo.model_dump())
    return dispositivo

@router.get(path='/unidade-consumidora/{unidade_consumidora_id}', response_model=DispositivoReadList)
def listar_dispositivo_da_unidade_de_consumo(unidade_consumidora_id: int):
    unidade_consumidora = UnidadeConsumidoraDB.get_or_none(UnidadeConsumidoraDB.id == unidade_consumidora_id)
    dispositivos = DispositivoDB.select().where(DispositivoDB.unidade_consumidora == unidade_consumidora)
    return {'dispositivos': dispositivos}

@router.get(path='/{dispositivo_id}', response_model=DispositivoReadOne)
def listar_dispositivo(dispositivo_id: int):
    dispositivo = DispositivoDB.get_or_none(DispositivoDB.id == dispositivo_id)
    return dispositivo

@router.patch(path='/{dispositivo_id}', response_model=DispositivoReadOne)
def atualizar_dispositivo(dispositivo_id: int, novo_dispositivo: DispositivoUpdate):
    dispositivo = DispositivoDB.get_or_none(DispositivoDB.id == dispositivo_id)
    dispositivo.nome = novo_dispositivo.nome
    dispositivo.tipo = novo_dispositivo.tipo
    dispositivo.consumo = novo_dispositivo.consumo
    dispositivo.uso_diario = novo_dispositivo.uso_diario
    dispositivo.dependencia = novo_dispositivo.dependencia
    dispositivo.unidade_consumidora = novo_dispositivo.unidade_consumidora
    dispositivo.save()
    return dispositivo

@router.delete(path='/{dispositivo_id}', response_model=DispositivoReadOne)
def excluir_dispositivo(dispositivo_id: int):
    dispositivo = DispositivoDB.get_or_none(DispositivoDB.id == dispositivo_id)
    dispositivo.delete_instance()
    return dispositivo
