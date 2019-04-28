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
              'SVC with polynomial (degree 3) kernel')

    print("Training...")
    models = (clf.fit(X_train, y_train) for clf in models)
    
    print("Validating...")
    for clf, title in zip(models, titles):
        y_pred  = [ clf.predict([x])[0] for x in X_test ]
        #y_scores = [ clf.score([x], [y]) for x,y in zip(X_test, y_test) ]
        
        print(title)
        print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
        print("Balanced Accuracy:", metrics.balanced_accuracy_score(y_test, y_pred))
        print("Precision (micro):", metrics.precision_score(y_test, y_pred, average='micro'))
        print("Precision (macro):", metrics.precision_score(y_test, y_pred, average='macro'))
        print("Precision (weighted):", metrics.precision_score(y_test, y_pred, average='weighted'))

    '''
    fig, sub = plt.subplots(2, 2)
    plt.subplots_adjust(wspace=.4, hspace=.4)

    X0, X1 = X[:,0], X[:, 1]
    xx, yy = make_meshgrid(X0, X1)
    
    print("Preparing plot...")
    for clf, title, ax in zip(models, titles, sub.flatten()):
        plot_contours(ax, clf, xx, yy,
                      cmap=plt.cm.coolwarm, alpha=.8)
        ax.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm,
                   s=20, edgecolors='k')
        ax.set_xlim(xx.min(), xx.max())
        ax.set_ylim(yy.min(), yy.max())
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_xticks(())
        ax.set_yticks(())
        ax.set_title(title)
        print(title, 'is ready...')
    
    print("Show!")
    plt.show()
    plt.savefig('plot.png')
    '''

if __name__ == '__main__':
    main()

