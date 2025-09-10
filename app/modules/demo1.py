# 使用 #@DESC 描述此模組的用途
# 模組對於基礎設施定義檔處理流程與參數解析說明描述於 desc 函數
#@DESC 單一檔案的基礎設施模組範例

# Import libraries

# Declare variable

# Declare function
def main():
    print("It is demo module.")

def desc():
    print("Show module configuration processing description.")

def exec(config):
    print("Execute module with config")
    print(config)

# Python entrypoint program
if __name__ == '__main__':
    main()
