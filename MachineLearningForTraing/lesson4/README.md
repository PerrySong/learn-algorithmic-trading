# Numpy

## Fast, wrapper of c

## Pandas is a wrapper of numpy
```python
  # nd array
  nd = df.values
```

## Notes on notation

``` python
  nd1[row, col]
  nd1[0, 0]
  nd1[3, 2]
  nd1[0:3, 1:3] # row (0,1,2) col(1, 2)
  nd1[:, 3]
  nd1[-1. 1:3]
```

## Creating NumPy arrays

```python
  np.array([1, 2, 3])

  # 2d array
  np.array([(1, 2, 3), (5, 6, 7)])

  # Empty array
  np.empty(5) # random value in the array
  np.empty((5, 4))

  # Array of 1s
  np.ones((5, 4))

  np.ones((5, 4), dtype=np.int_) # Makes the elements integers

```

## Generating random numbers  
``` python
  np.random.rand(5, 4) # Function arguments (not a tuple)

  # sample numbers from a Gaussian (normal) distribution
  np.random.normal(size=(2, 3)) # Standard normal, (mean = 0, s.d. = 1)
  np.random.normal(50, 10, size=(2, 3)) # change mean to 50 and s.d. to 10
```

## Array attributes

```python

  np.shape[0] # number of rows
  np.shape[1] # number of columns
  len(np.shape) # dimension
```
