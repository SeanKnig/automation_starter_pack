import datetime
import os
import sys

import threading
from datetime import date


import threading
class getSet():
    def __init__(self):
        print('init')

    def getTrainingSet(self, totalBank, timerange, strategy, configuration,  hyperopt, hyperoptLoss, epoch, timeframe):
        #threading.Timer(120, self.getTrainingSet).start()
        backtesting = "freqtrade backtesting --config %s.json -s %s --timerange=%s --dry-run-wallet %s --timeframe %s"%(configuration,strategy,timerange,totalBank, timeframe)
        hyperoptimization = "freqtrade hyperopt --hyperopt %s --hyperopt-loss %s --spaces all --strategy %s --config %s.json -e %s --timerange=%s --dry-run-wallet %s --timeframe %s"%(hyperopt,hyperoptLoss,strategy,configuration,epoch,timerange,totalBank, timeframe)
        data = "freqtrade download-data --config %s.json --timeframe %s"%(configuration, timeframe)
        trade = "freqtrade trade --config %s.json -s %s --dry-run-wallet %s"%(configuration,strategy, totalBank)
        print(backtesting)
        print(hyperoptimization)
        print(data)
        print(trade)


if __name__ == "__main__":
    bot = getSet()
    today = date.today()

    timeframes = ['5m','30m', '1h','4h','1d']
    interval = {'1 Year': 365, '6 Months': 182.5, '3 months':91.25, '1 Month': 30, '2 Weeks': 14, '1 Week' : 7, '1 day': 1}
    for k,v in interval.items():
        prior = datetime.datetime.today() - datetime.timedelta(days=v)
        form_ = prior.strftime("%Y%m%d-")
        print("__________________________________FROM %s_________________________________"%k)
        for time in timeframes:

            print(time)
            #getTrainingSet('0.005', '20210101-', 'HeraclesDOGEBTCBULL', 'configDOGEBTC', 'HeraclesHo', 'SharpeHyperOptLossDaily', '100', time)
            #getTrainingSet('0.005', '20210101-', 'Heracles', 'configDOGEBTC', 'HeraclesHo', 'SharpeHyperOptLossDaily', '100', time)
            #getTrainingSet('2.5', '20210319-20210401', 'Quickie', 'configAltEth', 'mabStraHo', 'SharpeHyperOptLossDaily', '100', time)
            #getTrainingSet('2.5', '20210322-20210410', 'BbandRsi', 'configAltEth2Bull', 'HeraclesHo', 'SharpeHyperOptLossDaily', '100', time)
            #getTrainingSet('0.05', '20210322-20210410', 'mabStra', 'configAltBTCMabStra', 'mabStraHo', 'SharpeHyperOptLossDaily', '100', time)
            #getTrainingSet('2.5', '20210101-', 'GodHeracles', 'configAltEth2Bull', 'HeraclesHo', 'SharpeHyperOptLossDaily', '100', time)
            #getTrainingSet('0.07', '20210201-', 'Heracles', 'configAltBTCBull', 'HeraclesHo', 'SharpeHyperOptLossDaily', '100', time)
            #getTrainingSet('2.5', '20210101-', 'TameHeracles', 'configAltEth2Bull', 'HeraclesHo', 'SharpeHyperOptLossDaily', '100', time)
            #getTrainingSet('1.0', '20210415-', 'GodStra', 'configAltEth', 'mabStraHo', 'SharpeHyperOptLossDaily', '100', time)
            #getTrainingSet('0.07', '20210201-', 'Heracles', 'configAltEthAll', 'HeraclesHo', 'SharpeHyperOptLossDaily', '100', time)
            #getTrainingSet('1.5', '20190606-20200417', 'mabStra', 'configAltEthAll', 'mabStraHo', 'SharpeHyperOptLossDaily', '100', time)
            bot.getTrainingSet('1500', '%s'%(form_), 'mabStra', 'configUSDTLINK', 'mabStraHo', 'SharpeHyperOptLossDaily', '100', time)

            #USDT
            #getTrainingSet('200', '20210511-', 'mabStra', 'configUSDTBTC', 'mabStraHO', 'SharpeHyperOptLossDaily', '100', time)


            #ETH BINANCE
            #Download all
            #getTrainingSet('2.5', '20210201-', 'Heracles', 'configBinance', 'HeraclesHo', 'SharpeHyperOptLossDaily', '100', time)
