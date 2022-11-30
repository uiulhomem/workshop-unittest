import pytest
import pandas as pd
import numpy as np

from app.filter import FilterDisk


@pytest.fixture
def input_data():
    data = pd.DataFrame()
    data['equipment'] = [
        'QUALQUER_COISA_AQUI',
        'TANTO_FAZ',
        'ESSE_E_UM_DISCO_FI',
        'OI_LINDAO',
        'RICO_TRAPEZIO_MONSTRO_FI'
    ]
    data['duration'] = [np.random.randint(1, 30) for _ in range(5)]
    data['work'] = [np.random.randint(1, 10) for _ in range(5)]
    data['n_om'] = [np.random.randint(1, 300) for _ in range(5)]

    return data

@pytest.fixture
def filter():
    return FilterDisk()

def test_find_disks(input_data, filter):
    disk_data, remaining_data = filter._FilterDisk__identify_disks(input_data)
    
    assert disk_data.shape[0] == 2
    assert remaining_data.shape[0] == 3

def test_disk_unique(input_data, filter):
    filtered_data = filter.apply(input_data)
    find_disk = lambda x: 1 if 'FI' in x else 0
    
    compare = filtered_data['equipment'].apply(find_disk).values

    assert compare.sum() == 1
