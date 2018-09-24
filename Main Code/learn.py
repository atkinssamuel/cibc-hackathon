import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

def Learn(X, n, state):
    gmm = GaussianMixture(n_components=n, covariance_type='full', random_state=0).fit(X) 	# Create Gaussian Classifier
    labels = gmm.predict(X)																	# Predict Labels/Cluster
    plt.scatter(X[:, 1], X[:, 5], c=labels, s=1, cmap='viridis');							# Plot
    plt.xlabel("Provider Type")																	
    plt.ylabel("Dollar Amount of Claim")
    plt.title(state)
    plt.show()
    return gmm.score_samples(X)																# Probability score of all datapoints, returned as np.array()