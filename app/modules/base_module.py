# 使用 #@DESC 描述此模組的用途
# 模組對於基礎設施定義檔處理流程與參數解析說明描述於 desc 函數
#@DESC 基礎模組結構

# Import libraries
from libs.docker import Service
# Declare variable
# Declare function
def main():
    """
    ISA 系統不會呼叫該函數，此函數應用於單獨執行時，用來測試模組內容
    """
    print("Do something to test base module")

def desc():
    """
    用於描述當前模組對配置內容的處理規則。
    """
    print("Show module configuration processing description.")

def exec(config):
    """
    模組執行時最後呼叫的函數，可在此執行配置檔中無特定對應函數的內容
    """
    print("Execute module with config.")
    s = Service(config, exec.__module__)
    s.run()

def container(service, config):
    """
    模組固定執行函數，將相應資訊填入 Container 物件
    """
    print("Create and assign container other information to service.")
    print(service.container)
    print(config)
    print('---')

def authorize(service, config):
    """
    模組固定執行函數，用來處理對服務容器的授權相關操作
    """
    print("Setting authorize information with target container.")
    print(f"Do {config}")
    print('---')

def secure(service, config):
    """
    模組固定執行函數，用來處理對服務容器的安全性相關操作
    """
    print("Setting secure information with target container.")
    print(f"Do {config}")
    print('---')

def command(service, config):
    """
    模組固定執行函數，用來處理對服務容器的非標準操作項目
    """
    print("Execute command to target container.")
    print(f"Execute with {config}")
    print('---')


def other(service, config):
    """
    自定義函數，若配置檔存在相應的關鍵字，則對應執行此動作
    """
    print("Custom configuration function.")
    print(f"Do {config}")
    print("Show all config:")
    print(service.config)
    print('---')

# Python entrypoint program
if __name__ == '__main__':
    main()
