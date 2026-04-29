import matplotlib.pyplot as plt
import seaborn as sns

def plot_graph(x_nodes: list[float], y_nodes: list[float], x_dense: list[float],
               y_original: list[float], y_interpolated: list[float], method_name: str):

    sns.set_theme(style="whitegrid", palette="muted")
    palette = sns.color_palette()
    color_orig = palette[0]
    color_interp = palette[2]
    color_nodes = "black"

    plt.figure(figsize=(10, 6))

    sns.lineplot(x=x_dense, y=y_original, color=color_orig, label='Funkcja Oryginalna')

    sns.lineplot(x=x_dense, y=y_interpolated, color=color_interp, label='Interpolacja', linestyle='--')

    sns.scatterplot(x=x_nodes, y=y_nodes, color=color_nodes, label='Węzły', s=80, zorder=3)

    plt.title(method_name, fontsize=15)

    plt.legend(frameon=True, shadow=True)
    plt.tight_layout()

    plt.show()