## 基礎設施處理模組

基礎設施處理模組對 ISA 系統是一個動態載入的函數包，執行時會根據配置檔關鍵字，以反射概念呼叫函數包中的函數；對此，ISA 提供兩種模組範本：

+ [簡易模組](./app/modules/simple_module.py)，僅符合 ISA 系統介面執行最低限度所需的函數。
+ [基礎模組](./app/modules/base_module.py)，符合基礎設施處理模組標準所需的所有函數。


+ 描述函數：```def desc()``` 是用來描述本模組配置檔會如何處理，主要用於 ```isa list [module_name]```。
+ 執行函數：```def exec(config)``` 是用來執行本模組配置檔實際執行狀況，主要用於 ```isa exec [configuration_filename]```
	- config 為配置檔中對應此模組的配置全部內容
	- 在簡易模組範本中，開發者可以依據自身需求處理配置內容
	- 在基礎模組範本中，開發者可使用服務類別來處理對應關鍵字的配置內容

由於基礎設施皆屬於同 ISA 虛擬網域下的服務容器，因此服務類別主要處理規範如下：

### 容器資訊

配置對象容器的基本資訊。

+ 配置檔：```[module_name].container = { name, port, restart }```
	- ```name``` 為容器名稱，亦是其在虛擬網路的域名
 	- ```port``` 為容器開啟的連接埠
 	- ```restart``` 為容器是否需要重啟，若不提供預設為 False
+ 模組函數：```def container(service, config)```
	- service 為服務類別的實體
	- config 為 ```[module_name].container``` 的內容
	- 相關資訊會預先處理並存於 service 的 container 變數，若有額外資訊要填寫，可於此函數中處理

### 設定授權資訊

配置對象的授權資訊。

+ 配置檔： ```[module_name].authorize```
	- 若配置對象的基礎服務有提供相應操作，應基於該關鍵字處理。
+ 模組函數：```def authorize(service, config)```
	- service 為服務類別的實體
	- config 為 ```[module_name].container``` 的內容

### 設定安全性資訊

配置對象的安全性資訊

+ 配置檔：```[module_name].secure```
	- 若配置對象的基礎服務有提供相應操作，應基於該關鍵字處理。
+ 模組函數：```def secure(service, config)```
	- service 為服務類別的實體
	- config 為 ```[module_name].secure``` 的內容

### 標準命令操作

對配置對象的執行標準操作程序

+ 配置檔：```[module_name].command```
	- 對配置對象的操作命令，模組執行時會依此關鍵字內的矩陣內容依序處理。
		+ 內容為一個包括三個 key 的物件 ```{'msg': '此命令的描述，可不提供', 'cmd': '命令名稱, 'data': '命令內容'}```
	- 可執行命令包括：
		+ ```template```：樣板操作
			- 從樣板目錄中取得樣板檔案
			- 將樣板檔案覆蓋關鍵字成為內容檔案
			- 內容檔案指定放置到共享目錄，若無共享目錄則放到 ```/tmp``` 目錄
		+ ```api```：服務 API 操作
			- 發送非同步的 RestAPI 訊息
			- 若 ```url``` 為相對路徑則會使用容器名稱組成完整路徑
		+ ```exec```：服務命令操作
			- 對目標服務執行 Docker exec 來發送命令
		+ ```restart```：重啟目標服務
			- 對目標服務執行 Docker restart
		+ ```sleep```：操作休眠
			- 依據秒數暫停流程
+ 模組函數：```def command(service, config)```
	- service 為服務類別的實體
	- config 為 ```[module_name].command``` 的內容
	- 前述的標準命令會由 service 直接執行，但若有額外關鍵字要執行，會呼叫模組函數，需自行分辨並撰寫相應處理方式

### 通用設計規範

+ 若需配置資訊已經存在於該服務，則應避免重複操作。
+ 若需配置複數內容，該關鍵字內容應為物件或矩陣，並依序或依序列表執行。
+ 若需操作配置對象的目錄內容，應確保目錄有共享。
+ 若需操作配置對象的遠端服務，應確保安全通訊所需資訊有共享。

### 模組關鍵字執行規範

+ 模組固定項目：容器資訊 ( Container )、授權資訊 ( authorize )、安全性資訊 ( secure )、操作程序 ( command )
	- 若無關鍵字則忽略該動作
+ 執行固定關鍵字以外的關鍵字
