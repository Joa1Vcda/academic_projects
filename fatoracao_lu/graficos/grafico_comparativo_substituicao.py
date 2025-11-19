import matplotlib.pyplot as plt
import numpy as np

def montar_grafico_substituicao(grafico_tempo_lu, grafico_tempo_gauss, tamanhos_N):

    tempo_ref = grafico_tempo_lu[-1]
    n_ref = tamanhos_N[-1]

    c_teorico = tempo_ref / (n_ref**2)

    n_teorico = np.linspace(tamanhos_N[0], tamanhos_N[-1], 100)

    tempo_teorico_quadratico = c_teorico * (n_teorico**2)
    plt.figure(figsize=(8, 6))

    plt.plot(
        n_teorico,
        tempo_teorico_quadratico,
        label=f"Curva Teórica O(N²)\n(c={c_teorico:.2e})",
        color="red",
        linestyle=":",
        linewidth=2.5,
    )

    plt.plot(
        tamanhos_N,
        grafico_tempo_lu,
        label="Solução via LU (Subst. Direta+Reversa)",
        marker="o",
        markersize=8,
        linestyle="-",
        linewidth=3,
    )

    plt.plot(
        tamanhos_N,
        grafico_tempo_gauss,
        label="Solução via Gauss (Subst. Reversa)",
        marker="o",
        markersize=8,
        linestyle="-",
        linewidth=3,
    )

    plt.xlabel("Tamanho da Matriz (N)", fontsize=12)
    plt.ylabel("Tempo de substituição (s)", fontsize=12)
    plt.title(
        "Gráfico de escalabilidade da etapa de solução: LU vs. Gauss", fontsize=16
    )
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)

    plt.legend()

    plt.show()
