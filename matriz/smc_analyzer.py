class SMCAnalyzer:
    def __init__(self, df, trend):
        self.df = df
        self.trend = trend

    def analyze(self):
        return {
            "bos": self._detect_bos(),
            "order_block": self._detect_order_block(),
            "fvg": self._detect_fvg(),
            "liquidity": self._detect_liquidity()
        }

    def _detect_bos(self):
        if self.trend == "BULLISH":
            return self.df['close'].iloc[-1] > self.df['high'].iloc[-2]
        if self.trend == "BEARISH":
            return self.df['close'].iloc[-1] < self.df['low'].iloc[-2]
        return False

    def _detect_order_block(self):
        prev = self.df.iloc[-2]
        curr = self.df.iloc[-1]

        if self.trend == "BULLISH":
            return prev['close'] < prev['open'] and curr['close'] > curr['open']
        if self.trend == "BEARISH":
            return prev['close'] > prev['open'] and curr['close'] < curr['open']
        return False

    def _detect_fvg(self):
        high_2 = self.df['high'].iloc[-3]
        low_0 = self.df['low'].iloc[-1]
        return low_0 > high_2

    def _detect_liquidity(self):
        highs = self.df['high'].tail(10)
        lows = self.df['low'].tail(10)
        return highs.max() - highs.min() < (lows.max() - lows.min())
