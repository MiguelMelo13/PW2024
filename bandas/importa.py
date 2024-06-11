from bandas.models import *
from datetime import datetime
import json

Banda.objects.all().delete()
Album.objects.all().delete()
Musica.objects.all().delete()

with open('bandas/json/bandasfile.json') as file:
    bandas = json.load(file)

    for info in bandas:
        Banda.objects.create(
            nome=info['nome'],
            genero_musical=info['genero_musical'],
            nacionalidade=info['nacionalidade'],
            ano=info['ano']
        )

with open('bandas/json/albunsfile.json') as filee:
    data = json.load(filee)

    for item in data:
        banda_name = item['banda']
        banda, _ = Banda.objects.get_or_create(nome=banda_name)
        album = Album.objects.create(
            titulo=item['titulo'],
            ano_lancamento= item['ano_lancamento'],
            banda=banda
        )

        for musica_data in item['musicas']:
            Musica.objects.create(
                titulo=musica_data['titulo'],
                album=album,
                duracao_minutos=musica_data['duracao_minutos'],
                data_lancamento = item['data_lancamento']
            )
    
