from brownie import Wei, reverts
import brownie
import time

def test_staked_token(chain, accounts, instance):
    print('='*20 + ' running ... ' + '='*20)
    decimal = 1e18
    one_day = 60*60*24
    minStakedTime = 30 * one_day

    timestamp = int(time.time())

    amount = 0.2*decimal

    startTime = instance.currentTime()
    print('startTime = ', startTime)

    instance.newDeposit(accounts[8], {'from': accounts[1], 'value': "5 ether"})

    instance.incrementShiftTime(one_day*2)

    instance.newDeposit(accounts[8], {'from': accounts[1], 'value': "10 ether"})
    print('totalInvested = ', instance.totalInvested()/decimal)

    print('getAllDeposits = ', instance.getAllDeposits(accounts[1]))

    calcAmount = instance.calculateReward(accounts[1])
    print('calcAmount[1] = ', calcAmount/decimal)

    instance.incrementShiftTime(one_day*2)

    instance.newDeposit(accounts[1], {'from': accounts[2], 'value': "5 ether"})

    print('getRefsWallet[8] = ', instance.getRefsWallet(accounts[8]))
    print('getRefsAmount[8] = ', instance.getRefsAmount(accounts[8]))
    refAmounts = instance.getRefsAmount(accounts[8])
    print('getRefsAmount[8] [0] = ', refAmounts[0]/decimal)

    print('getRefsWallet[1] = ', instance.getRefsWallet(accounts[1]))
    print('getRefsAmount[1] = ', instance.getRefsAmount(accounts[1]))
    refAmounts = instance.getRefsAmount(accounts[1])
    print('getRefsAmount[1] [0] = ', refAmounts[0]/decimal)

    instance.incrementShiftTime(one_day*6 + 10)

    days = instance.checkDaysWithoutReward(accounts[1], 0)
    print('days = ', days)
    calcAmount = instance.calculateReward(accounts[1])
    print('calcAmount[1] = ', calcAmount/decimal)
    print('currentTime = ', instance.currentTime())

    instance.incrementShiftTime(one_day)

    days = instance.checkDaysWithoutReward(accounts[1], 0)
    print('days = ', days)
    calcAmount = instance.calculateReward(accounts[1])
    print('calcAmount[1] = ', calcAmount/decimal)
    print('currentTime = ', instance.currentTime())

    instance.incrementShiftTime(one_day)

    tx = instance.reinvest(0, {'from': accounts[1]})
    print('tx.info() = ', tx.info())

    instance.incrementShiftTime(one_day)

    days = instance.checkDaysWithoutReward(accounts[1], 0)
    print('days [0] = ', days)
    days = instance.checkDaysWithoutReward(accounts[1], 1)
    print('days [1] = ', days)
    calcAmount = instance.calculateReward(accounts[1])
    print('calcAmount[1] = ', calcAmount/decimal)

    tx = instance.reinvest(1, {'from': accounts[1]})

    instance.newDeposit(accounts[2], {'from': accounts[3], 'value': "5 ether"})

    instance.newDeposit(accounts[3], {'from': accounts[4], 'value': "90 ether"})

    refAmounts = instance.getRefsAmount(accounts[1])
    print('getRefsAmount[1] = ', refAmounts)

    refAmounts = instance.getRefsAmount(accounts[2])
    print('getRefsAmount[2] = ', refAmounts)

    refAmounts = instance.getRefsAmount(accounts[8])
    print('getRefsAmount[8] = ', refAmounts)

    instance.incrementShiftTime(one_day*30)
    days = instance.checkDaysWithoutReward(accounts[1], 0)
    print('days [0] + 30 = ', days)
    print('getAllDeposits = ', instance.getAllDeposits(accounts[1]))
    print('currentTime = ', instance.currentTime())

    instance.incrementShiftTime(one_day*6)
    days = instance.checkDaysWithoutReward(accounts[1], 0)
    print('days [0] + 6 = ', days)
    print('currentTime = ', instance.currentTime())

    instance.incrementShiftTime(one_day)
    days = instance.checkDaysWithoutReward(accounts[1], 0)
    print('days [0] + 1 = ', days)
    print('currentTime = ', instance.currentTime())

    instance.incrementShiftTime(one_day)
    days = instance.checkDaysWithoutReward(accounts[1], 0)
    print('days [0] + 1 = ', days)
    print('currentTime = ', instance.currentTime())

    tx = instance.reinvestAll({'from': accounts[1]})
    print('tx.info() = ', tx.info())
    print('getAllDeposits = ', instance.getAllDeposits(accounts[1]))
