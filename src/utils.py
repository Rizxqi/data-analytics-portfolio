import joblib
import matplotlib.pyplot as plt

def save_model(model, filename):
    joblib.dump(model, filename)

def load_model(filename):
    return joblib.load(filename)

def plot_bar(x, y, title='Bar Plot', xlabel='', ylabel=''):
    plt.figure(figsize=(8,5))
    plt.bar(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
