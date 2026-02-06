from models.analysis_result import AnalysisResult

class SignalEngine:
    def __init__(self, trend, smc):
        self.trend = trend
        self.smc = smc

    def evaluate(self):
        if (
            self.trend == "BULLISH"
            and self.smc["bos"]
            and self.smc["order_block"]
        ):
            return AnalysisResult(
                "POSIBLE COMPRA",
                "Tendencia alcista + BOS + Order Block confirmado"
            )

        if (
            self.trend == "BEARISH"
            and self.smc["bos"]
            and self.smc["order_block"]
        ):
            return AnalysisResult(
                "POSIBLE VENTA",
                "Tendencia bajista + BOS + Order Block confirmado"
            )

        return AnalysisResult(
            "NO TRADE",
            "No hay confluencia suficiente según SMC"
        )
