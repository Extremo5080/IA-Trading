import cv2
import numpy as np

class VisualAnalyzer:
    def __init__(self, image):
        self.image = image
        self.gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def analyze(self):
        edges = cv2.Canny(self.gray, 50, 150)
        lines = cv2.HoughLinesP(
            edges,
            rho=1,
            theta=np.pi/180,
            threshold=100,
            minLineLength=100,
            maxLineGap=10
        )

        trend = self._detect_trend(lines)
        impulse = self._detect_impulse(edges)

        return {
            "visual_trend": trend,
            "impulse": impulse
        }

    def _detect_trend(self, lines):
        if lines is None:
            return "RANGE"

        slopes = []
        for line in lines:
            x1, y1, x2, y2 = line[0]
            if x2 != x1:
                slopes.append((y2 - y1) / (x2 - x1))

        if not slopes:
            return "RANGE"

        avg_slope = sum(slopes) / len(slopes)

        if avg_slope < -0.2:
            return "BULLISH"
        elif avg_slope > 0.2:
            return "BEARISH"
        return "RANGE"

    def _detect_impulse(self, edges):
        density = np.sum(edges > 0) / edges.size
        return density > 0.05
