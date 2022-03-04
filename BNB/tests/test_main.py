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

    instance.incrementShiftTime(one_day*2 + 10) #all days = 2

    instance.newDeposit(accounts[8], {'from': accounts[1], 'value': "10 ether"})
    totalInvested = instance.totalInvested()/decimal
    print('totalInvested = ', totalInvested)
    assert totalInvested == 15
    totalReferralBonus = instance.totalReferralBonus()/decimal
    print('totalReferralBonus = ', totalReferralBonus)
    assert totalReferralBonus == 0.25

    print('getAllDeposits = ', instance.getAllDeposits(accounts[1]))

    calcAmount = instance.calculateReward(accounts[1])
    print('calcAmount[1] = ', calcAmount/decimal)
    #print('calculateRewardByIndex[1][0] = ', instance.calculateRewardByIndex(accounts[1], 0))
    #print('calculateRewardByIndex[1][1] = ', instance.calculateRewardByIndex(accounts[1], 1))
    assert calcAmount/decimal == 0.7 # 0.35*2

    instance.incrementShiftTime(one_day*2 + 10) #all days = 4
    calcAmount = instance.calculateReward(accounts[1])
    print('calcAmount[2] = ', calcAmount/decimal)
    assert calcAmount/decimal == 2.8 # 0.35*4 + 0.7 * 2 = 2.8


    instance.newDeposit(accounts[1], {'from': accounts[2], 'value': "5 ether"})
    totalReferralBonus = instance.totalReferralBonus()/decimal
    print('totalReferralBonus = ', totalReferralBonus)
    assert totalReferralBonus == 0.65

    print('getRefsWallet[8] = ', instance.getRefsWallet(accounts[8]))

    refAmounts = instance.getRefsAmount(accounts[8]) # 0.25, 0.15, 0, 0, 0 == 5%(5), 3%(5), 0, 0, 0
    print('getRefsAmount[8] = ', refAmounts)
    print('getRefsAmount[8] [0] = ', refAmounts[0]/decimal)

    print('getRefsWallet[1] = ', instance.getRefsWallet(accounts[1]))
    print('getRefsAmount[1] = ', instance.getRefsAmount(accounts[1]))
    refAmounts = instance.getRefsAmount(accounts[1]) #  0.25, 0, 0, 0, 0 == 5%(5), 0, 0, 0, 0
    print('getRefsAmount[1] [0] = ', refAmounts[0]/decimal)

    print('.'*20 + ' processing ... ' + '.'*20)


    instance.incrementShiftTime(one_day*6 + 10) #all days = 10

    days = instance.checkDaysWithoutReward(accounts[1], 0)
    print('days = ', days) #10
    assert days == 10

    calcAmount = instance.calculateReward(accounts[1])
    print('calcAmount[1] = ', calcAmount/decimal) #
    assert calcAmount/decimal == 9.1 # 0.35*10 + 0.7*8 = 9.1

    print('currentTime = ', instance.currentTime())

    tx = instance.getReward(0, {'from': accounts[1]})
    #print('tx.info() = ', tx.info())
    getAllDeposits = instance.getAllDeposits(accounts[1])
    print('getAllDeposits (0) = ', getAllDeposits)
    tx = instance.getRewardAll({'from': accounts[1]})
    #print('tx.info() = ', tx.info())
    getAllDeposits = instance.getAllDeposits(accounts[1])
    print('getAllDeposits (all) = ', getAllDeposits)


    instance.incrementShiftTime(one_day) #all days = 11

    days = instance.checkDaysWithoutReward(accounts[1], 0)
    print('days [0] = ', days)
    days = instance.checkDaysWithoutReward(accounts[1], 1)
    print('days [1] = ', days)
    calcAmount = instance.calculateReward(accounts[1])
    print('calcAmount[1] = ', calcAmount/decimal)
    assert calcAmount/decimal == 1.05 # 0.35*1 + 0.7 * 1 = 1.05

    tx = instance.getReward(1, {'from': accounts[1]})

    instance.newDeposit(accounts[2], {'from': accounts[3], 'value': "5 ether"})

    instance.newDeposit(accounts[3], {'from': accounts[4], 'value': "90 ether"})

    refAmounts = instance.getRefsAmount(accounts[1])
    print('getRefsAmount[1] = ', refAmounts) #0.25, 0.15, 1.35, 0, 0

    refAmounts = instance.getRefsAmount(accounts[2])
    print('getRefsAmount[2] = ', refAmounts)

    refAmounts = instance.getRefsAmount(accounts[8])
    print('getRefsAmount[8] = ', refAmounts)

    instance.incrementShiftTime(one_day*20)  #all days = 31
    days = instance.checkDaysWithoutReward(accounts[1], 0)
    print('days [0] + 20 = ', days)
    assert days == 20
    print('getAllDeposits = ', instance.getAllDeposits(accounts[1]))
    print('currentTime = ', instance.currentTime())

    tx = instance.getRewardAll({'from': accounts[1]})
    #print('tx.info() = ', tx.info())
    print('getAllDeposits = ', instance.getAllDeposits(accounts[1]))

    instance.incrementShiftTime(one_day*6)  #all days = 37
    days = instance.checkDaysWithoutReward(accounts[1], 0)
    print('days [0] + 6 = ', days)
    print('currentTime = ', instance.currentTime())

    calcAmount = instance.calculateReward(accounts[1])
    print('calcAmount[1] = ', calcAmount/decimal)
    tx = instance.getRewardAll({'from': accounts[1]})

    instance.incrementShiftTime(one_day)  #all days = 38
    days = instance.checkDaysWithoutReward(accounts[1], 0)
    print('days [0] + 1 = ', days)
    print('currentTime = ', instance.currentTime())

    instance.incrementShiftTime(one_day)  #all days = 39
    days = instance.checkDaysWithoutReward(accounts[1], 0)
    print('days [0] + 1 = ', days)
    print('currentTime = ', instance.currentTime())

    calcAmount = instance.calculateReward(accounts[1])
    print('calcAmount[1] = ', calcAmount/decimal)
