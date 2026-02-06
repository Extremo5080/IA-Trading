class TrendAnalyzer:
    def __init__(self, df):
        self.df = df

    def analyze(self):
        last = self.df.iloc[-1]

        if last['ema50'] > last['ema200']:
            return "BULLISH"
        elif last['ema50'] < last['ema200']:
            return "BEARISH"
        return "RANGE"
