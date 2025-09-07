#@DESC 組件化的基礎設施模組範例

# Import libraries
import numpy as np

# Declare variable

# Declare function
def main():
    a = np.arange(6)
    a2 = a[np.newaxis, :]
    print(a2.shape)


# Python entrypoint program
if __name__ == '__main__':
    main()
