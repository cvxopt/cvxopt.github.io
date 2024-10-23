def read(digits, N = None, dataset = "training", 
    path = "/home/vandenbe/papers/svm/data/mnist", bias = False):

    """
    Read N images from classes in digits.  
    If bias is False, return as an N x 28**2 matrix.
    If bias is True, return as an N x (1 + 28**2) matrix with first
        column 127.
    """
    

    import os, struct
    from array import array
    from cvxopt import matrix

    if dataset is "training":
        fname_img = os.path.join(path, 'train-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 'train-labels-idx1-ubyte')
    elif dataset is "testing":
        fname_img = os.path.join(path, 't10k-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 't10k-labels-idx1-ubyte')
    else:
        raise ValueError, "dataset must be 'testing' or 'training'"
    
    flbl = open(fname_lbl, 'rb')
    magic_nr, size = struct.unpack(">II", flbl.read(8))
    lbl = array("b", flbl.read())
    flbl.close()

    fimg = open(fname_img, 'rb')
    magic_nr, size, rows, cols = struct.unpack(">IIII", fimg.read(16))
    img = array("B", fimg.read())
    fimg.close()
  
    ind = [ k for k in xrange(size) if lbl[k] in digits ]
    if N is not None: ind = ind[:N]
    c = int(bias)
    images =  matrix(0, (len(ind), c + rows*cols))
    if bias: images[:, 0 ] = 127
    labels = matrix(0, (len(ind), 1))
    for i in xrange(len(ind)):
        images[i, c:] = img[ ind[i]*rows*cols : (ind[i]+1)*rows*cols ]
        labels[i] = lbl[ind[i]]

    return images, labels


def show(X, I = None, title = None):
    """
    Show first 100 images in rows I of X.
    """
    import pylab
    from cvxopt import matrix

    if I is None: I = range(X.size[0])
    N = min(len(I), 100)
    pylab.gray()
    for k in xrange(N):
        pylab.subplot(N/10+1, min(N, 10), k+1)
        if X.size[1] == 784:
            pylab.imshow(-matrix( X[I[k],:], size=(28,28)).T)
        else: 
            pylab.imshow(-matrix( X[I[k],1:], size=(28,28)).T)
        if title is not None: pylab.title(str(title[k]))
        pylab.axis('off')


import random, math
from cvxopt import matrix

def rand_data(N1 = None, N2 = None, digits1 = None, digits2 = None,
    dataset = "training", bias = False):
    """
    Reads from MNIST data set. 

    Returns N1 examples from class 1 and N2 examples from class 2.
    
    """
    random.seed()

    # Classify digits1 versus digits2.
    if digits1 is None:
        digits1 = [ 0 ]
    if digits2 is None:
        digits2 = [ k for k in xrange(10) if k not in digits1 ]

    # Read examples for digits in digits1 + digits2.
    if dataset == "training":
        print "reading training data ..."
        images, labels = read(digits1 + digits2, bias = bias)
    elif dataset == "testing":
        print "reading testing data ..."
        images, labels = read(digits1 + digits2, "testing", bias = bias)

    images = images / (256. * math.sqrt(images.size[1]))
    C1 = [ k for k in xrange(len(labels)) if labels[k] in digits1 ] 
    C2 = [ k for k in xrange(len(labels)) if labels[k] in digits2 ] 
    random.shuffle(C1)
    random.shuffle(C2)
    
    if N1 is None: N1 = len(C1)
    if N2 is None: N2 = len(C2)
    print "N1 = %i, N2 = %i"%(N1,N2)

    train = C1[:N1] + C2[:N2]
    random.shuffle(train)
    X = images[train,:]
    d = matrix([ 2*(k in digits1) - 1 for k in labels[train] ])
    del(images)

    return X, d
