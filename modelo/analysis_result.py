class AnalysisResult:
    def __init__(self, title, explanation):
        self.title = title
        self.explanation = explanation

    def show(self):
        print("\n📊 RESULTADO DEL ANÁLISIS")
        print("━━━━━━━━━━━━━━━━━━━━━━")
        print(f"🔍 Señal: {self.title}")
        print(f"🧠 Justificación: {self.explanation}\n")
