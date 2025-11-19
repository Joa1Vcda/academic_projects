import matplotlib.pyplot as plt
import numpy as np

def montar_grafico_fatoracao(calculo_tempo_lu, calculo_tempo_gauss, tamanhos_N):
    
    tempo_ref = calculo_tempo_gauss[-1]
    n_ref = tamanhos_N[-1]
    c_teorico = tempo_ref / (n_ref**3)
    n_teorico = np.linspace(tamanhos_N[0], tamanhos_N[-1], 100)

    tempo_teorico_cubico = c_teorico * (n_teorico**3)

    plt.figure(figsize=(8, 6))
    plt.plot(
        n_teorico,
        tempo_teorico_cubico,
        label=f"Como uma função n³ se comportaria\n(c={c_teorico:.2e})",
        color="red",
        linestyle=":",
        linewidth=2.5,
    )

    plt.plot(
        tamanhos_N,
        calculo_tempo_lu,
        label="Tempo da fatoração LU",
        marker="o",
        markersize=8,
        linestyle="-",
        linewidth=3,
    )

    plt.plot(
        tamanhos_N,
        calculo_tempo_gauss,
        label="Tempo da eliminação de Gauss",
        marker="o",
        markersize=8,
        linestyle="-",
        linewidth=3,
    )

    plt.xlabel("Tamanho da Matriz (N)", fontsize=12)
    plt.ylabel("Tempo Gasto Total (s)", fontsize=12)
    plt.title(
        "Gráfico de Escalabilidade: Fatoração LU vs. Eliminação de Gauss", fontsize=16
    )
    plt.legend()

    plt.grid(True, which="both", linestyle="--", linewidth=0.5)

    plt.show()