from modelo.analysis_result import AnalysisResult


class SignalEngine:

    def __init__(self, trend, smc, visual):
        self.trend = trend
        self.smc = smc
        self.visual = visual

    def evaluate(self):

        # ESCENARIO COMPRA
        if self.trend == "BULLISH" and self.smc == "BOS":
            explanation = "Tendencia alcista confirmada con ruptura de estructura."

            if self.visual == "ZONE_DETECTED":
                explanation += " Zona relevante detectada en el gráfico."

            return AnalysisResult(
                title="Contexto Alcista (Posible Compra)",
                explanation=explanation
            )

        # ESCENARIO VENTA
        if self.trend == "BEARISH" and self.smc == "CHoCH":
            explanation = "Cambio de carácter en tendencia bajista."

            if self.visual == "ZONE_DETECTED":
                explanation += " Precio reaccionando en zona clave."

            return AnalysisResult(
                title="Contexto Bajista (Posible Venta)",
                explanation=explanation
            )

        # SIN CONTEXTO
        return AnalysisResult(
            title="Sin oportunidad clara",
            explanation="No se cumplen condiciones de estructura ni tendencia."
        )
