# 使用 #@DESC 描述此模組的用途
# 模組對於基礎設施定義檔處理流程與參數解析說明描述於 desc 函數
#@DESC 單一檔案的基礎設施模組範例

# Import libraries
import numpy as np

# Declare variable

# Declare function
def main():
    a = np.arange(6)
    a2 = a[np.newaxis, :]
    print(a2.shape)

def desc():
    print("Show module configuration processing description.")

# Python entrypoint program
if __name__ == '__main__':
    main()
