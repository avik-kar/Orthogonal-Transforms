#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6

import numpy as np
import math

def getSequence():
    inSequence = np.array([])
    inSeqString = input("\nPlease enter the array (elements separated by space): ")
    seqSplited = inSeqString.split()
    for i in range(len(seqSplited)):
        inSequence = np.append(inSequence, float(seqSplited[i]))
    return inSequence

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

def viewable(seq):
    for i in range(len(seq)):
        if abs(seq[i].real) < 10**(-10):
            seq[i] = 0 + 1j*seq[i].imag
        if abs(seq[i].imag) < 10**(-10):
            seq[i] = seq[i].real
    return seq
    
def dct(seq):
    l = len(seq)
    out = np.zeros(l)
    for i in range(l):
        for j in range(l):
            out[i] = out[i] + 2*seq[j]*np.cos((math.pi*i*((2*j)+1))/(2*l))
    return out
   
def viewable_r(seq):
    for i in range(len(seq)):
        if abs(seq[i]) < 10**(-10):
            seq[i] = 0
    return seq

def dst(seq):
    l = len(seq)
    out = np.zeros(l)
    for i in range(l):
        for j in range(l):
            out[i] = out[i] + seq[j]*np.sin((math.pi*(i+1)*((2*j)+1))/(2*l))
    return out
    
def wht(seq):
    raise NotImplementedError()
    
def slant(seq):
    raise NotImplementedError()
    
def haar(seq):
    raise NotImplementedError()
    
def klt(seq):
    raise NotImplementedError()
