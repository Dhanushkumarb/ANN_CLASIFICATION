import h5py
f = h5py.File('model.h5', 'r')
print(list(f.keys()))
