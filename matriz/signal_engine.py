from modelo.analysis_result import AnalysisResult

class SignalEngine:
    def __init__(self, trend, smc, visual):
        self.trend = trend
        self.smc = smc
        self.visual = visual

    def evaluate(self):
        if (
            self.trend == "BULLISH"
            and self.smc["bos"]
            and self.smc["order_block"]
            and self.visual["visual_trend"] == "BULLISH"
            and self.visual["impulse"]
        ):
            return AnalysisResult(
                "POSIBLE COMPRA",
                "SMC alcista confirmado por análisis visual"
            )

        if (
            self.trend == "BEARISH"
            and self.smc["bos"]
            and self.smc["order_block"]
            and self.visual["visual_trend"] == "BEARISH"
            and self.visual["impulse"]
        ):
            return AnalysisResult(
                "POSIBLE VENTA",
                "SMC bajista confirmado por análisis visual"
            )

        return AnalysisResult(
            "NO TRADE",
            "El contexto visual no confirma la estructura SMC"
        )
