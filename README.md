# Infrastructure Service Application

## 簡介

系統的基礎設施 ( Infrastructure ) 是指諸多完善且可運行的開源或閉源軟體，藉由運用此些軟體來補充系統的軟體服務基礎，讓開發的軟體能基於此些服務繼續擴大應用方面；例如，伺服器端 API 服務會配合相應的資料庫基礎設施。

在微服物系統中，應用程式開通常會配置相應的基礎設施；然而，有些基礎設施提供的服務要完整，需與其他服務串聯運作，例如藉由雲端儲存服務儲存伺服器日誌與數據，並經由流處理統計與分析，將相應結果提供給數據視覺化軟體呈現。

在這種多基礎設施串聯構成的服務結構中，需提供基礎設施配置、執行、管理的流程與介面，從而讓其他應用程式能藉由遠端服務操控。

基於上述概念，基礎設施服務應用程式是將對基礎設施的配置、執行、管理方法以容器封裝的服務應用程式，其專案基礎源於 [Algorithm service Application](https://github.com/eastmoon/algorithm-service-application) 的 FastAPI 框架概念，藉由 YAML 配置資訊，進而控制與管理相應的基礎設施容器；因此，該服務應用程式應包括下述特性：

+ 可控制同一個聯集 ( Docker Compose ) 的容器服務
+ 依據配置檔管理控制流程與內容
+ 實際執行對基礎設施配置應由處理模組負責

若從設計細節來討論，ISA 專案是基於容器環境下的簡易 [Ansible](https://github.com/eastmoon/infra-ansible) 專案，其相同設計概念：

+ 配置檔 ( Configuration file ) 即為 [Ansible Playbook](https://docs.ansible.com/ansible/latest/reference_appendices/playbooks_keywords.html)
+ 處理模組 ( Module ) 即為 [Ansible Module](https://docs.ansible.com/ansible/2.9/modules/list_of_all_modules.html)

其差異在於：

+ 專案結構簡易
+ 服務對象為同容器虛擬網路下的服務單元
+ 精簡對外 API 接口
+ 模組處理可自行規劃與定義

但實務若有需要可以整合 Ansible 框架，並加以運用 ansible 的處理模組。

## 適用情境

+ 封裝基礎建設項目的服務配置、執行、控制相關函式庫與腳本
+ 封裝內容為映像檔，可提供給其他容器服務系統使用
+ 基礎建設的執行目錄為固定

## 設計與說明文件

+ [開發運維指令](./docs/isa-devops-cli.md)
+ [服務操作介面](./docs/isa-command-and-route.md)
+ [基礎設施處理模組](./docs/isa-modules-design-concept.md)
