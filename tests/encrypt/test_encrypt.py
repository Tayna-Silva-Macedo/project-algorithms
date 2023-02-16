import pytest

from challenges.challenge_encrypt_message import encrypt_message

VALID_MESSAGE = "Mensagem secreta"
INVALID_MESSAGE = 7

VALID_KEY = 5
INVALID_KEY = "1"

BIG_KEY = 50
PAIR_KEY = 4
ODD_KEY = 3


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(VALID_MESSAGE, INVALID_KEY)

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(INVALID_MESSAGE, VALID_KEY)

    result_big_key = encrypt_message(VALID_MESSAGE, BIG_KEY)
    result_pair_key = encrypt_message(VALID_MESSAGE, PAIR_KEY)
    result_odd_key = encrypt_message(VALID_MESSAGE, ODD_KEY)

    assert result_big_key == "aterces megasneM"
    assert result_pair_key == "aterces mega_sneM"
    assert result_odd_key == "neM_aterces megas"
