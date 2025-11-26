from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def train_kmeans(X, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(X)
    return kmeans

def evaluate_clusters(X, kmeans):
    labels = kmeans.labels_
    score = silhouette_score(X, labels)
    return score
