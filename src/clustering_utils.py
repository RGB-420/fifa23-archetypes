from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def cluster_position_group(df, position_group, features, n_clusters=5):
    """
    Filters the DataFrame by position group, scales the features,
    and applies KMeans clustering.

    Parameters:
        df (pd.DataFrame): The full player dataset
        position_group (str): Position group to filter ('DEF', 'MID', 'FWD')
        features (list): List of features for clustering
        n_clusters (int): Number of clusters

    Returns:
        pd.DataFrame: Filtered dataframe with added 'Cluster' column
        KMeans: Fitted KMeans object
    """
    group_df = df[df['Position Group'] == position_group].copy()
    group_df = group_df.dropna(subset=features)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(group_df[features])

    kmeans = KMeans(n_clusters=n_clusters, random_state=0, n_init=10)
    kmeans.fit(X_scaled)

    group_df['Cluster'] = kmeans.labels_

    return group_df, kmeans