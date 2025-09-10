# Infrastructure Service Application

## 簡介

系統的基礎設施 ( Infrastructure ) 是指諸多完善且可運行的開源或閉源軟體，藉由運用此些軟體來補充系統的軟體服務基礎，讓開發的軟體能基於此些服務繼續擴大應用方面；例如，伺服器端 API 服務會配合相應的資料庫基礎設施。

在微服物系統中，應用程式開通常會配置相應的基礎設施；然而，有些基礎設施提供的服務要完整，需與其他服務串聯運作，例如藉由雲端儲存服務儲存伺服器日誌與數據，並經由流處理統計與分析，將相應結果提供給數據視覺化軟體呈現。

在這種多基礎設施串聯構成的服務結構中，需提供基礎設施配置、執行、管理的流程與介面，從而讓其他應用程式能藉由遠端服務操控。

基於上述概念，基礎設施服務應用程式是將對基礎設施的配置、執行、管理方法以容器封裝的服務應用程式，其專案基礎源於 [Algorithm service Application](https://github.com/eastmoon/algorithm-service-application) 的 FastAPI 框架概念，藉由 YAML 配置資訊，進而控制與管理相應的基礎設施容器；因此，該服務應用程式應包括下述特性：

+ 對 Host 的容器操作
+ 具有相關服務的配置目錄
	- 依據服務名稱目錄在 ```/data/conf``` 目錄下
+ 服務包括以下行為
	- 列舉
		+ 服務項目的處理模組
		+ 工作流配置檔
	- 建置工作流配置檔
		+ 依據工作流需要添加配置資訊與行為
		+ 對於可配置的服務對象，應為可添加的項目
	- 執行工作流配置檔
		+ 解析 yaml 與 json 檔案
		+ 依據配置檔提供不同服務需要的配置檔 ( configuration file ) 與服務內容建置 ( Service API )
		+ 依據需要判斷是否重啟該服務
+ DevOps CLI
	- dev : 開發服務配置與服務操控
	- pub : 發佈包括控制腳本與相關的容器服務配置檔
	- pack：將服務配置檔與相關內容產出映像檔，並增加啟動腳

## 適用情境

+ 封裝基礎建設項目的服務配置、執行、控制相關函式庫與腳本
+ 封裝內容為映像檔，可提供給其他容器服務系統使用
+ 基礎建設的執行目錄為固定

## 開發環境

本專案預設於 Windows 環境設計，相關操作指令如下：

### 啟動環境

使用以下命令會啟動開發容器。

```
isa.bat dev
```

開發模式中會掛起不同目錄以便開發細節

+ ```/app``` 目錄會掛入專案目錄 ```app``` ，用於基礎設施模組開發，亦是容器指定的工作目錄
+ ```/usr/local/isa``` 目錄會掛入專案目錄 ```conf/docker/cli```，用於服務命令介面開發
+ ```/usr/local/fastapi``` 目錄會掛入專案目錄 ```conf/docker/api```，用於 WebAPI 服務開發/

開發模式會啟動 WebAPI 服務，可透過 HOST 主機連線則使用 ```http://localhost:8080``` 網址，並執行有開啟的路徑以執行相應的服務命令介面。

開發容器啟動後有提供以下選項進行額外操作：

+ ```isa.bat dev --into```：進入開發容器
+ ```isa.bat dev --stop```：關閉開發容器

### 服務命令介面

服務命令介面為容器內提供的 ```isa``` 命令介面，要執行相關指令必須先啟動開發環境並進入容器：

```
# 啟動開發容器
isa.bat dev
# 進入開發容器
isa.bat dev --into
```

服務命令介面包括以下功能：

#### 列舉可供控制的模塊

此項指令用來列出目前專案中擁有的基礎設施處理模組，例如對 nginx 或 kafka 基礎設施的操作。

使用 CLI 指令：

+ ```isa list```：搜尋所有模組，並顯示模組進入點檔案的 ```#@DESC``` 標籤內容
	- 本專案繼承 [Algorithm service Application](https://github.com/eastmoon/algorithm-service-application) 專案設計概念，在專案 ```app``` 目錄層的 ```*.py``` 檔案或 ```*/main.py``` 目錄會被視為模組
+ ```isa list [module_name]```：用來顯示特定模組的解析說明，此動作會執行模組函示庫中的 ```desc()``` 函數  

使用 API 路徑：

+ ```http://localhost:8080/isa/list``` 與 ```isa list``` 功能相同
+ ```http://localhost:8080/isa/list/[module_name]``` 與 ```isa list [module_name]``` 功能相同

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

使用 API 路徑：

+ ```GET http://localhost:8080/isa/conf```：顯示所有的配置檔名稱
+ ```GET http://localhost:8080/isa/conf/[filename]```：顯示 filename 配置檔的配置內容
+ ```GET http://localhost:8080/isa/conf/[filename]/[module]```：顯示 filename 配置檔中 module 模組的配置內容
+ ```DELETE http://localhost:8080/isa/conf/[filename]/[module]```：移除 filename 配置檔中 module 模組的配置內容
+ ```POST http://localhost:8080/isa/conf/[filename]/[module] --data [json_string] ```：將 json_string 內容寫入 filename 配置檔中 module 模組的配置內容

#### 執行配置檔

此項指令用來執行基礎設施操作，其操作內容則基於配置檔中對每個模組的描述。

其操作可使用 CLI 指令：

```
isa exec [file]
```

其中 file 是指要執行的配置檔名，若目標配置檔不存在則不會執行，若未提供則使用 default.yml 配置檔。

使用 API 路徑：

+ ```POST http://localhost:8080/isa/exec/[filename]```：執行目標 filename 配置檔

配置檔執行會有其預設行為，倘若要改變行為，則設定於 ```global``` 模組或各模組的關鍵字，當前以規劃功能如下：

+ 模組執行順序
		- 預設依據關鍵字的排序執行
		- 若要強制順序則可設定 ```global.flow = [moduele_name_1, ..., module_name_N]```
+ 執行模組
		- 預設關鍵字即為模組名稱
		- 若要更換實際執行模組可設定 ```[module_name_1].module = 'module_name_2'```
		- 實務上可以利用此方式將關鍵字做為標籤使用

此外，考量基礎設施操作，各模組應具有以下關鍵字：

+ 配置對象容器資訊 ```[module_name].container = { name, port, restart }```
		- ```name``` 為容器名稱，亦是其在虛擬網路的域名
		- ```port``` 為容器開啟的連接埠
		- ```restart``` 為容器是否需要重啟，若不提供預設為 False

#### 管理的基礎設施狀態

此項指令用來執行基礎設施操作與管理，原則上 ISA 專案會啟動時會與相應基礎設施同屬一個區域網路，因此可以利用 Docker-in-Docker 並透過 Compose 指令來監控與管理目標容器。

基於上述概念，此指令可執行必需包括以下設定與工具：

+ ISA 內有 Docker 指令，且設定使用 HOST 的 docker.sock 檔案
+ ISA 內有 docker-compose 設定檔

其操作可使用 CLI 指令：

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

使用 API 路徑：

+ ```GET http://localhost:8080/isa/infra/```：顯示管理環境檢核
+ ```GET http://localhost:8080/isa/infra/ps```：顯示基礎設施容器資訊
+ ```GET http://localhost:8080/isa/infra/stats```：顯示基礎設施的資源數據
