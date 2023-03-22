import pytest

from src.generator.player import Player
from src.generator.player_locale import Locale


@pytest.mark.parametrize(
    'status', ['ACTIVE', 'INACTIVE', 'DELETED']
)
def test_bilder(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize('del_key', [
    'status',
    'balance',
    'localize',
    'avatar'
]
                         )
def test_delet(del_key, get_player_generator):
    json_obj = get_player_generator.build()
    del json_obj[del_key]
    print(json_obj)

@pytest.mark.parametrize('local',
                         ['fr', 'de', 'ch'])
def test_update(get_player_generator, local):
    json_obj = get_player_generator.update_inner_value(
        ['localize', local], Locale('fr_FR').build()).build()
    print(json_obj)
