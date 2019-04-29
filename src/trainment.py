#!/bin/python
import argparse
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, metrics, model_selection
import sys
sys.setrecursionlimit(10000)

'''
Visualization

FROM: https://scikit-learn.org/stable/auto_examples/svm/plot_iris.html#sphx-glr-auto-examples-svm-plot-iris-py
'''

def make_meshgrid(x, y, h=.02):
    print('Mesh grid...')
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    return xx, yy

def plot_contours(ax, clf, xx, yy, **params):
    print('Ploting contours...')
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out

'''
Trainment
'''
def train(dataset):
    X = np.delete(dataset, -1, axis=1) 
    y = dataset[:,-1]
    clf = svm.SVC(gamma='scale')
    return clf.fit(X, y)

'''
Arguments
'''
parser = argparse.ArgumentParser(description='Model trainer')
parser.add_argument('dataset', metavar='dataset', type=str, help='File containing the data')
parser.add_argument('--cache', metavar='size', type=float, help='Size of the kernel cache', default=200) 

'''
Main Function
'''
def main():
    args = parser.parse_args()
    dataset = np.load(args.dataset)

    labels = ['Will stay', 'Uncertain', 'Will resign']
    print("Starting...")
    X = np.delete(dataset, -1, axis=1)
    y = dataset[:,-1]

    X_train, X_test, y_train, y_test = model_selection.train_test_split(
                                         X, y, test_size=.1, random_state=0)
    
    C = 1.0
    
    models = (svm.SVC(kernel='linear', cache_size=args.cache, C=C),
              svm.LinearSVC(C=C),
              svm.SVC(kernel='rbf', gamma='scale', cache_size=args.cache, C=C),
              svm.SVC(kernel='poly', gamma='scale', degree=3, cache_size=args.cache, C=C),
              svm.SVC(kernel='sigmoid', gamma='scale', cache_size=args.cache, C=C)
              )
    
    titles = ('SVC with linear kernel',
              'LinearSVC (linear kernel)',
              'SVC with RBF kernel',
              'SVC with polynomial (degree 3) kernel',
              'SVC with sigmoidal kernel')

    print("Training...")
    models = (clf.fit(X_train, y_train) for clf in models)
    
    print("Validating...")
    for clf, title in zip(models, titles):
        y_pred  = [ clf.predict([x])[0] for x in X_test ]
        #y_scores = [ clf.score([x], [y]) for x,y in zip(X_test, y_test) ]
        
        print("")
        print(title)
        print(metrics.classification_report(y_test, y_pred))
        print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
        print("Balanced Accuracy:", metrics.balanced_accuracy_score(y_test, y_pred))
        print("Precision (micro):", metrics.precision_score(y_test, y_pred, average='micro'))
        print("Precision (macro):", metrics.precision_score(y_test, y_pred, average='macro'))
        print("Precision (weighted):", metrics.precision_score(y_test, y_pred, average='weighted'))

        cm = metrics.confusion_matrix(y_test, y_pred)
        print(cm)
        
        # Plot
        fig, ax = plt.subplots()
        im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
        ax.figure.colorbar(im, ax=ax)
        ax.set(xticks=np.arange(cm.shape[1]),
               yticks=np.arange(cm.shape[0]),
               xticklabels=labels,
               yticklabels=labels,
               title=title+" Confusion Matrix",
               ylabel="True",
               xlabel="Predicted")
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
        
        # Annotations
        thresh = cm.max() / 2.0
        for i in range(cm.shape[0]):
            for j in range(cm.shape[1]):
                ax.text(j, i, format(cm[i, j], 'd'),
                        ha="center", va="center",
                        color="white" if cm[i, j] > thresh else "black")
        fig.tight_layout()
        # Save
        plt.savefig(title+" Confusion Matrix.png")

if __name__ == '__main__':
    main()

