## 基礎設施服務應用程式 - 服務操作介面

本章節說明基礎設施服務應用程式 ( ISA ) 提供兩種操作介面，分別為命令介面 ( Command-Line interface ) 與網頁應用程式介面 ( Website Application Interface )。

+ 命令介面 ( Command-Line interface ) 使用 Python 的 argparse 設計
    - 專案啟動開發環境 ```isa.bat dev``` 後，進入容器 ```isa.bat dev --into```，即可使用命令介面 ( Command-Line interface )
+ 網頁應用程式介面 ( Website Application Interface ) 使用 Python 的 FastAPI 設計
    - 專案啟動開發環境 ```isa.bat dev``` 後，即可透過瀏覽器操作網頁應用程式介面 ( Website Application Interface )

開發模式預設進入為[測試目錄](./test)，若要執行測試腳本，請用以下指令執行相應腳本：

```
bash xxx.sh
```

以下基於服務主要功能說明提供的介面內容：

#### 列舉可供控制的模組

此項指令用來列出目前專案中擁有的基礎設施處理模組，例如對 nginx 或 kafka 基礎設施的操作。

可使用 CLI 指令如下，操作範本參考[測試腳本](./test/isa-list-cli.sh)：

+ ```isa list```：搜尋所有模組，並顯示模組進入點檔案的 ```#@DESC``` 標籤內容
	- 本專案繼承 [Algorithm service Application](https://github.com/eastmoon/algorithm-service-application) 專案設計概念，在專案 ```app``` 目錄層的 ```*.py``` 檔案或 ```*/main.py``` 目錄會被視為模組
+ ```isa list [module_name]```：用來顯示特定模組的解析說明，此動作會執行模組函示庫中的 ```desc()``` 函數  

可使用 API 路徑如下，操作範本參考[測試腳本](./test/isa-list-api.sh)：

+ ```http://localhost:8080/isa/list``` 與 ```isa list``` 功能相同
+ ```http://localhost:8080/isa/list/[module_name]``` 與 ```isa list [module_name]``` 功能相同

對於模組的詳細設計，請參考[基礎設施處理模組](#基礎設施處理模組)章節。

#### 配置檔讀取、修改、刪除

此項指令用來彙整供專案執行的配置檔內容，而其配置檔為 YAML 格式且結構如下：

```
[module_name]:
	{module_configuration}
```

配置檔主要描述內容，是當該配置檔被執行時，提供給相應模組需要的配置內容，而模組會依據其設定內容對目標基礎設施進行操作。

因此，配置檔操作會包括以下主要參數

+ 配置檔名稱 ( file )：要寫入的配置檔名，若未提供則寫入 default.yml 檔案
+ 模組名稱 ( module )：要配置的模組名，若未提供則寫入 default 模組
+ 配置字串：提供給模組的配置內容字串，此字串可為 JSON 或 YAML 格式

基於以上描述，可使用 CLI 指令如下：

+ 顯示所有的配置檔名稱
```
isa conf --methods list
```
+ 顯示 demo 配置檔的配置內容
```
isa conf --methods get demo
```
+ 顯示 demo 配置檔中 m1 模組的配置內容
```
isa conf --methods get demo m1
```
+ 移除 demo 配置檔中 m1 模組的配置內容
```
isa conf --methods del demo m1
```
+ 經由 STDIN 將 demo_text 字串寫入 demo 配置檔中 m1 模組的配置內容
```
echo demo_text | isa conf --methods post -i demo m1
```
+ 經由 STDIN 重定向 ( Redirections ) 的 Here Document 機制寫入 demo 配置檔中 m1 模組的配置內容
```
isa conf --methods post -i demo m1 << EOF
DEMO_TXT
EOF
```
+ 經由 JSON 解析，將 ```/data/m1.json``` 檔案內容寫入 demo 配置檔中 m1 模組的配置內容
	- 目前提供 JSON ( ```*.json``` )與 YAML ( ```*.yml```、```*.yaml``` ) 格式解析
	- 若未提供 ```--module``` 參數，預設會寫入於 default 模組
```
isa conf --methods post -f /data/m1.json demo m1
```

CLI 測試腳本包括如下：

+ [配置檔清單與內容擷取](./test/isa-conf-retrieve-cli.sh)
+ [利用 STDIN 寫入配置檔](./test/isa-conf-write-stdin-cli.sh)
+ [利用檔案寫入配置檔](./test/isa-conf-write-file-cli.sh)
+ [配置檔模組寫入與移除](./test/isa-conf-write-and-remove-cli.sh)

使用 API 路徑：

+ ```GET http://localhost:8080/isa/conf```：顯示所有的配置檔名稱
+ ```GET http://localhost:8080/isa/conf/[filename]```：顯示 filename 配置檔的配置內容
+ ```GET http://localhost:8080/isa/conf/[filename]/[module]```：顯示 filename 配置檔中 module 模組的配置內容
+ ```DELETE http://localhost:8080/isa/conf/[filename]/[module]```：移除 filename 配置檔中 module 模組的配置內容
+ ```POST http://localhost:8080/isa/conf/[filename]/[module] --data [json_string] ```：將 json_string 內容寫入 filename 配置檔中 module 模組的配置內容

CLI 測試腳本包括如下：

+ [配置檔清單與內容擷取](./test/isa-conf-retrieve-api.sh)
+ [配置檔模組寫入與移除](./test/isa-conf-write-and-remove-api.sh)

#### 執行配置檔

此項指令用來執行基礎設施操作，其操作內容則基於配置檔中對每個模組的描述。

其操作可使用 CLI 指令，操作範本參考[測試腳本](./test/isa-exec-cli.sh)：：

```
isa exec [file]
```

其中 file 是指要執行的配置檔名，若目標配置檔不存在則不會執行，若未提供則使用 default.yml 配置檔。

使用 API 路徑，操作範本參考[測試腳本](./test/isa-exec-api.sh)：

+ ```POST http://localhost:8080/isa/exec/[filename]```：執行目標 filename 配置檔

配置檔執行會有其預設行為，倘若要改變行為，則設定於 ```global``` 模組或各模組的關鍵字，當前以規劃功能如下：

+ 模組執行順序
	- 預設依據關鍵字的排序執行
	- 若要強制順序則可設定 ```global.flow = [moduele_name_1, ..., module_name_N]```
+ 執行模組
	- 預設關鍵字即為模組名稱
	- 若要更換實際執行模組可設定 ```[module_name_1].module = 'module_name_2'```
	- 實務上可以利用此方式將關鍵字做為標籤使用

對於模組的詳細設計，請參考[基礎設施處理模組](#基礎設施處理模組)章節。

#### 管理的基礎設施狀態

此項指令用來執行基礎設施操作與管理，原則上 ISA 專案會啟動時會與相應基礎設施同屬一個區域網路，因此可以利用 Docker-in-Docker 並透過 Compose 指令來監控與管理目標容器。

基於上述概念，此指令可執行必需包括以下設定與工具：

+ ISA 內有 Docker 指令，且設定使用 HOST 的 docker.sock 檔案
+ ISA 內有 docker-compose 設定檔

可使用 CLI 指令如下，操作範本參考[測試腳本](./test/isa-infra-cli.sh)：

+ 顯示管理環境檢核
```
isa infra
```
+ 顯示基礎設施容器資訊
```
isa infra ps
```
+ 顯示基礎設施的資源數據
```
isa infra stats
```
+ 啟動全體基礎設施服務
```
isa infra start
```
+ 關閉全體基礎設施服務 ( 不包括 ISA 自身 )
```
isa infra stop
```
+ 重啟目標基礎設施 ( 不可包括 ISA 自身 )
```
isa infra restart [container_name]
```

可使用 API 路徑如下，操作範本參考[測試腳本](./test/isa-infra-api.sh)：

+ ```GET http://localhost:8080/isa/infra/```：顯示管理環境檢核
+ ```GET http://localhost:8080/isa/infra/ps```：顯示基礎設施容器資訊
+ ```GET http://localhost:8080/isa/infra/stats```：顯示基礎設施的資源數據
