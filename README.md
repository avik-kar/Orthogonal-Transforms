# Orthogonal-Transforms
Implementation of Various 1-D Orthogonal Transforms.

1. Discrete Fourier Transform
2. Decimation in Time - Fast Fourier Transform
3. Decimation in Frequency - Fast Fourier Transform
4. Discrete Cosine Transform
5. Discrete Sine Transform
6. Walsh-Hadamard Transform
7. Slant Transform
8. Haar Transform
9. Karhunen-Loeve Transform

## Requirments
* Python3

## Running the experiments

* To get the DFT of seq:
```
python src/ot_main.py --transform=dft --sequence=seq
```
* To get the DIT-FFT of seq:
```
python src/ot_main.py --transform=ditfft --sequence=takeinput
```

You can change the default values of other parameters to simulate different conditions. Refer to the options section.

## Options
The default values for paramters parsed to the experiment are given in ```options.py```. Details of those parameters are given:

* ```--transform:```  Default: 'dft'. Options: 'dft', 'ditfft', 'diffft', 'dct', 'dst', 'wht', 'slant', 'haar', 'klt'
* ```--sequence:```    Default: 'random' (length = 8). Options: 'random', 'takeinput'


## Further Readings
### Books:
* [Introduction to Orthogonal Transforms with Applications in Data Processing and Analysis](http://fourier.eng.hmc.edu/book/lectures/mybook.pdf)
