import pytest
from brownie import config

@pytest.fixture(scope='module')
def deployer(accounts):
    return accounts[9]


@pytest.fixture(scope='module')
def refAdmin(accounts):
    return accounts[8]


@pytest.fixture(scope="module")
def instance(BnbMoney, deployer, refAdmin):
    return BnbMoney.deploy(deployer, refAdmin, {'from': deployer})
