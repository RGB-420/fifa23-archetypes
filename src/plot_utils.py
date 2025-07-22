import plotly.graph_objects as go
import plotly.subplots as sp

def plot_archetypes_radar(cluster_means, radar_features, archetype_names, position_group):
    """
    Plots radar charts for all archetypes in a single subplot figure.
    """
    # Crear subplots grid
    fig = sp.make_subplots(
        rows=2, cols=3,
        specs=[[{'type': 'polar'}, {'type': 'polar'}, {'type': 'polar'}],
               [{'type': 'polar'}, {'type': 'polar'}, None]],
        subplot_titles=list(archetype_names.values()),
        horizontal_spacing=0.15,  # ligeramente menos espacio horizontal
        vertical_spacing=0.05     # menos espacio vertical entre filas
    )

    # Map clusters to subplot positions
    row_col_map = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2)]
    colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A']

    # Add radar chart for each archetype
    for i, (cluster_id, archetype) in enumerate(archetype_names.items()):
        row, col = row_col_map[i]
        fig.add_trace(
            go.Scatterpolar(
                r=cluster_means.loc[cluster_id, radar_features].values,
                theta=radar_features,
                fill='toself',
                name=archetype,
                opacity=0.8,
                line=dict(color=colors[i], width=2)
            ),
            row=row, col=col
        )

    # Ajustar layout
    fig.update_layout(
        height=1000, width=1500,
        title=dict(
            text=f"FIFA23 {position_group} Archetypes (Radar Charts)",
            font=dict(size=24, family="Arial Black")
        ),
        showlegend=False,
        margin=dict(t=120, b=50, l=100, r=50),  # ⬅️ más margen izquierdo (l=100)
        polar=dict(
            radialaxis=dict(visible=True, showticklabels=True, ticks='')
        )
    )

    fig.update_annotations(font=dict(size=18))
    fig.show()

