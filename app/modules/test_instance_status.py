# 使用 #@DESC 描述此模組的用途
# 模組對於基礎設施定義檔處理流程與參數解析說明描述於 desc 函數
#@DESC 單一檔案的基礎設施模組範例

# Import libraries

# Declare variable
global_count = 0

# Declare function
def main():
    print("It is demo module.")

def desc():
    print("Show module configuration processing description.")

def exec(config):
    global global_count
    print("Execute module with config")
    print(f"Global variable: {global_count}")
    global_count += 1

# Python entrypoint program
if __name__ == '__main__':
    main()
