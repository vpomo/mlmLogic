import pytest
from brownie import config

@pytest.fixture(scope="module")
def instance(Mlm, accounts):
    return Mlm.deploy(accounts[9], {'from': accounts[0]})
