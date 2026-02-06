import MetaTrader5 as mt5
import pandas as pd
import pandas_ta as ta

class DataLoader:
    def __init__(self, symbol, timeframe, bars=1500):
        self.symbol = symbol
        self.timeframe = timeframe
        self.bars = bars

    def get_data(self):
        if not mt5.initialize():
            raise RuntimeError("No se pudo inicializar MT5")

        rates = mt5.copy_rates_from_pos(
            self.symbol,
            self.timeframe,
            0,
            self.bars
        )

        df = pd.DataFrame(rates)
        df['time'] = pd.to_datetime(df['time'], unit='s')

        # Indicadores base
        df['ema50'] = ta.ema(df['close'], 50)
        df['ema200'] = ta.ema(df['close'], 200)

        df.dropna(inplace=True)
        return df
