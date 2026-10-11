import os

base = os.path.dirname(os.path.abspath(__file__))
herramienta = "A_turtle edicotr"
excluir = {"generar_readme", herramienta}

scripts = sorted(
    f[:-3] for f in os.listdir(base)
    if f.endswith(".py") and f[:-3] not in excluir
)

lineas = [
    "# complex-turtle-art",
    "",
    "Colección de arte generativo programado en Python",
    "",
    "Canal de YouTube: https://youtube.com/@kek.studio-cp",
    "",
    "## Herramienta",
    "",
    "[Editor de turtle casi en tiempo real](A_turtle%20edicotr.py): el código se ejecuta unos 0.2 segundos después de escribirlo, para acelerar la creación de dibujos.",
    "",
    "## Galería",
    "",
]

for s in scripts:
    if os.path.exists(os.path.join(base, "imagenes", s + ".jpeg")):
        lineas += [f"### {s.replace('_', ' ')}", "", f"![{s}](imagenes/{s}.jpeg)", "", f"[Ver código]({s}.py)", ""]
    else:
        print("Sin imagen:", s)

with open(os.path.join(base, "README.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(lineas))

print("README.md generado con", len(scripts), "dibujos")