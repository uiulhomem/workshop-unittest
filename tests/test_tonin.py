from app.tonin import Tonin


def test_profit():
    tonin = Tonin()

    output = tonin.crypto_investiment()

    assert output == False

def test_where():
    tonin = Tonin()

    output = tonin.where()

    assert output == 'BH'
