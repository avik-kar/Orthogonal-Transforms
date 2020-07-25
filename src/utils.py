#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6

import numpy as np
import math

#def get_sequence(args):
    
def dft(seq):
    l = len(seq)
    out = np.zeros(l, dtype=complex)
    for i in range(l):
        for j in range(l):
            out[i] = out[i] + seq[j]*np.exp((-2j*math.pi*j*i)/l)
    return out
    
def ditfft(seq):
    l = len(seq)
    half_l = l // 2
    out = np.zeros(l, dtype=complex)
    
    if l == 1:
        out[0] = seq[0]
    else:
        seq_even = seq[0::2] #get all even indexed elements
        seq_odd = seq[1::2]  #get all odd indexed elements
        out_even = ditfft(seq_even)
        out_odd = ditfft(seq_odd)
        for m in range(l):
            out[m] = out_even[m % half_l] + out_odd[m % half_l] * np.exp(-1j*2*math.pi*m/l)
    return out
    
def diffft(seq):
    l = len(seq)
    half_l = l // 2
    out = np.zeros(l, dtype=complex)
    out1 = np.zeros(half_l, dtype=complex)
    out2 = np.zeros(half_l, dtype=complex)
    seq1 = np.zeros(half_l, dtype=complex)
    seq2 = np.zeros(half_l, dtype=complex)
    if l == 1:
        out[0] = seq[0]
    else:
        seq_hi = seq[0:half_l:1] #get 1st half of input array
        seq_lo = seq[half_l:l:1]  #get 2nd half of input array
        for m in range(half_l):
            seq1[m] = seq_hi[m] + seq_lo[m]
            seq2[m] = (seq_hi[m] - seq_lo[m]) * np.exp(-1j*2*math.pi*m/l)
            
        out1 = diffft(seq1)
        out2 = diffft(seq2)
        out = np.concatenate([out1,out2])
    return out

def reArrange(seq):
    l = len(seq)
    n = np.int(np.log2(l))
    out = np.zeros(l, dtype=complex)
    for i in range(l):
        bin_i = bin(i)
        b_i = str(bin_i)[2::]
        b = ''.join(['0'*(n-len(b_i)),b_i])
        k = 0
        for element in range(len(b)): 
            if b[element] == '1':
                k = k + (2**element)
        out[k] = seq[i]
    return out
    
def dct(seq):
    raise NotImplementedError()
    
def dst(seq):
    raise NotImplementedError()
    
def wht(seq):
    raise NotImplementedError()
    
def slant(seq):
    raise NotImplementedError()
    
def haar(seq):
    raise NotImplementedError()
    
def klt(seq):
    raise NotImplementedError()
    

def exp_details(args):
    print('\nExperimental details:')
    print(f'    Model     : {args.model}')
    print(f'    Algorithm : {args.algo}')
    print(f'    Optimizer : {args.optimizer}')
    print(f'    Learning  : {args.lr}')
    print(f'    Global Rounds   : {args.epochs}\n')

    return
