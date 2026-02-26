from analizador_lexico import AnalizadorLexico
from analizador_modelo import AnalizadorModelo


class AnalizadorFusion:

    def __init__(self, peso_lexico=0.4, peso_modelo=0.6):
        self.peso_lexico = peso_lexico
        self.peso_modelo = peso_modelo
        print("Cargando sistema...")
        self.lexico = AnalizadorLexico()
        self.modelo = AnalizadorModelo()
        print("Sistema listo\n")

    def analizar(self, texto):
        r_lex = self.lexico.analizar(texto)
        r_mod = self.modelo.analizar(texto)

        score_lex = r_lex["score"]
        score_mod = r_mod["score"]
        ironia = r_lex["ironia"]

        if ironia:
            peso_l, peso_m = 0.8, 0.2
        else:
            peso_l, peso_m = self.peso_lexico, self.peso_modelo

        score = max(-1.0, min(1.0, score_lex * peso_l + score_mod * peso_m))

        polaridad = self._polaridad(score, r_lex["polaridad"], r_mod["polaridad"])
        emociones = self._fusionar_emociones(r_lex.get("emociones", {}), r_mod.get("emociones", {}))

        intensidad_lex = r_lex.get("intensidad", 0)
        intensidad = min(1.0, intensidad_lex * peso_l + abs(score_mod) * peso_m)

        explicaciones = []
        explicaciones.append("Lexico:")
        for e in r_lex["explicaciones"]:
            explicaciones.append(f"  - {e}")
        explicaciones.append("Modelo:")
        for e in r_mod["explicaciones"]:
            explicaciones.append(f"  - {e}")
        explicaciones.append(
            f"Fusion: lexico({peso_l:.0%}) x {score_lex:+.4f} + modelo({peso_m:.0%}) x {score_mod:+.4f} = {score:+.4f}"
        )

        return {
            "texto": texto,
            "polaridad": polaridad,
            "score_polaridad": round(score, 4),
            "emociones": emociones,
            "intensidad": round(intensidad, 4),
            "ironia": ironia,
            "explicaciones": explicaciones,
        }

    def _polaridad(self, score, pol_lex, pol_mod):
        if pol_lex == pol_mod:
            return pol_lex
        if score > 0.2:
            return "positive"
        elif score < -0.2:
            return "negative"
        elif abs(score) <= 0.1:
            return "neutral"
        return "mixed"

    def _fusionar_emociones(self, emo_lex, emo_mod):
        resultado = {}
        todas = set(list(emo_mod.keys()) + list(emo_lex.keys()))
        for emo in todas:
            vm = emo_mod.get(emo, 0)
            vl = emo_lex.get(emo, 0)
            if vm > 0 and vl > 0:
                val = vm * 0.6 + vl * 0.4
            elif vm > 0:
                val = vm
            else:
                val = vl * 0.5
            if val > 0.01:
                resultado[emo] = round(val, 4)
        return resultado
