from matriz.data_loader import DataLoader
from matriz.trend_analyzer import TrendAnalyzer
from matriz.smc_analyzer import SMCAnalyzer
from matriz.signal_engine import SignalEngine

from vision.screen_reader import ScreenReader
from vision.chart_cropper import ChartCropper
from vision.visual_analyzer import VisualAnalyzer

import MetaTrader5 as mt5


def main():
    # 1. Datos del mercado
    loader = DataLoader("EURUSD", mt5.TIMEFRAME_H1)
    data = loader.get_data()

    # 2. Análisis lógico
    trend = TrendAnalyzer(data).analyze()
    smc = SMCAnalyzer(data, trend).analyze()

    # 3. Análisis visual
    screen = ScreenReader().capture()
    chart = ChartCropper(
        x=200,   # AJUSTA a tu pantalla
        y=100,
        width=900,
        height=600
    ).crop(screen)

    visual = VisualAnalyzer(chart).analyze()

    # 4. Motor de decisión
    engine = SignalEngine(trend, smc, visual)
    result = engine.evaluate()

    # 5. Resultado
    result.show()


if __name__ == "__main__":
    main()
