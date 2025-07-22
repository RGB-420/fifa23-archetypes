import plotly.graph_objects as go
import plotly.subplots as sp

def plot_archetypes_radar(cluster_means, radar_features, archetype_names, position_group):
    """
    Plots radar charts for all archetypes in a single subplot figure.

    Parameters:
        cluster_means (pd.DataFrame): Cluster means (features as columns)
        radar_features (list): Features to plot (axes of radar)
        archetype_names (dict): Mapping {cluster_id: archetype_name}
        position_group (str): Position group name for the title ('DEF', 'MID', 'FWD')
    """
    # Create subplots grid
    fig = sp.make_subplots(
        rows=2, cols=3,
        specs=[[{'type': 'polar'}, {'type': 'polar'}, {'type': 'polar'}],
               [{'type': 'polar'}, {'type': 'polar'}, None]],
        subplot_titles=list(archetype_names.values())
    )

    # Map clusters to subplot positions
    row_col_map = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2)]

    # Add radar chart for each archetype
    for i, (cluster_id, archetype) in enumerate(archetype_names.items()):
        row, col = row_col_map[i]
        fig.add_trace(
            go.Scatterpolar(
                r=cluster_means.loc[cluster_id, radar_features].values,
                theta=radar_features,
                fill='toself',
                name=archetype
            ),
            row=row, col=col
        )

    # Update layout
    fig.update_layout(
        height=800, width=1200,
        title_text=f"FIFA23 {position_group} Archetypes (Radar Charts)",
        showlegend=False
    )

    fig.show()
