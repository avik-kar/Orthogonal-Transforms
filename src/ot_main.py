#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6



import pickle
import numpy as np


from options import args_parser
from utils import dft, ditfft, diffft, reArrange, dct, dst, wht, haar, slant, klt


if __name__ == '__main__':
    
    args = args_parser()
    
    if args.sequence == 'random':
        inSequence = np.random.rand(8)
    print("\nThe input sequence is: {}".format(inSequence))
    
    if args.transform == 'dft':
        task = 'Discrete Fourier Transform'
        outSequence = dft(inSequence)
    elif args.transform == 'ditfft':
        task = 'Fast Fourier Transform (Decimation in Time)'
        outSequence = ditfft(inSequence)
    elif args.transform == 'diffft':
        task = 'Fast Fourier Transform (Decimation in Frequency)'
        outSequence = reArrange(diffft(inSequence))
    elif args.transform == 'dct':
        task = 'Discrete Cosine Transform'
        outSequence = dct(inSequence)
    elif args.transform == 'dst':
        task = 'Discrete Sine Transform'
        outSequence = dst(inSequence)
    elif args.transform == 'wht':
        task = 'Walsh-Hadamard Transform'
        outSequence = wht(inSequence)
    elif args.transform == 'slant':
        task = 'Slant Transform'
        outSequence = slant(inSequence)
    elif args.transform == 'haar':
        task = 'Haar Transform'
        outSequence = haar(inSequence)
    else:
        task = 'Karhunen-Loeve Transform'
        outSequence = klt(inSequence)
    
    
    print("The {} of input sequence is: {}".format(task,outSequence))

    # Saving the objects train_loss and local_test_accuracy:
    path = 'C:\\Users\\Avik\\Orthogonal Transforms\\save\\'  # Define save folder path here
    file_name = '{}.pkl'.\
        format(task)
    with open(path+file_name, 'wb') as f:
        pickle.dump([inSequence, outSequence], f)
