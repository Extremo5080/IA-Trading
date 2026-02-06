from core.data_loader import DataLoader
from core.trend_analyzer import TrendAnalyzer
from core.smc_analyzer import SMCAnalyzer
from core.signal_engine import SignalEngine

import MetaTrader5 as mt5

def main():
    loader = DataLoader("EURUSD", mt5.TIMEFRAME_H1)
    data = loader.get_data()

    trend = TrendAnalyzer(data).analyze()
    smc = SMCAnalyzer(data, trend).analyze()

    engine = SignalEngine(trend, smc)
    result = engine.evaluate()

    result.show()

if __name__ == "__main__":
    main()
