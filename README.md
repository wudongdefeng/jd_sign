<h1 align="center">
  某东
  <br>
  Author: chiupam
</h1>

# 简介
把自己的sign算法部署到腾讯云serverless上。
> 各位，别浪费时间了，直接看这个项目吧 👉 [official](https://github.com/chiupam/Docker/blob/main/official/README.md) 👈
# 目录
- [简介](#简介)
- [目录](#目录)
- [使用方式](#使用方式)
  - [Docker部署（推荐）](#docker部署推荐)
    - [1.1使用docker部署](#11-使用docker部署)
    - [1.2.使用docker-compose部署](#12-使用docker-compose部署)
    - [2.上传正确的文件](#2-上传正确的文件)
  - [腾讯云函数（推荐）](#腾讯云函数serverless不推荐)
    - [1.Fork本项目](#1fork本项目)
    - [2.准备腾讯云函数serverless的必备参数](#2准备腾讯云函数serverless的必备参数)
    - [3.将参数填到Secrets](#3将参数填到Secrets)
    - [4.同意Actions条款](#4同意Actions条款)
    - [5.部署到腾讯云函数serverless](#5部署到腾讯云函数serverless)
- [申明](#申明)
# 使用方式
## Docker部署（推荐）
### 1.1 使用docker部署
```shell
docker run -dit \
  --name sign \
  --restart always \
  --hostname sign \
  -v $PWD/sign:/app \
  -p 80:80 \
  chiupam/sign:latest
```
### 1.2 使用docker-compose部署
```shell
cat > ./docker-compose.yml << EOF
version: "2.0"
services:
  surgio:
    image: chiupam/sign:latest
    container_name: sign
    restart: always
    hostname: sign
    volumes:
      - $PWD/sign:/app
    ports:
      - 80:80
EOF
docker-compose up -d
```
### 2. 上传正确的文件
```text
将正确的 sign.py 算法文件拉取到 /sign 目录中即可
```
## 腾讯云函数serverless（不推荐）
### 1.Fork本项目
- 点击 [chiupam/jd_sign](https://github.com/chiupam/jd_sign)
- 然后点击右上角的 `Fork` 按钮即可.
### 2.准备腾讯云函数serverless的必备参数
- 腾讯云账户需要 [实名认证](https://console.cloud.tencent.com/developer/auth)
- 为了确保权限足够, 获取以下这两个参数时**不要使用子账户**
- 开通云函数 `SCF` 的腾讯云账号，在 [访问秘钥页面](https://console.cloud.tencent.com/cam/capi) 获取账号的 `SecretID`，`SecretKey`
- 依次登录 [SCF 云函数控制台](https://console.cloud.tencent.com/scf) 和 [SLS 控制台](https://console.cloud.tencent.com/sls) 开通相关服务，确保您已开通服务并创建相应 [服务角色](https://console.cloud.tencent.com/cam/role) **SCF_QcsRole、SLS_QcsRole**
### 3.将参数填到Secrets
- 打开您自己的jd_sign仓库
- 点击上方的 `Settings` , 依次点击 `Secrets` 、 `New secret`
- 依次添加以下内容
- `Name`和`Value`的内容各如下：
  
|        Name        |      Value      | 必须  |
|:------------------:|:---------------:|:---:|
|        SIGN        | 正确的 sign.py 的代码 |  是  |
| TENCENT_SECRET_ID  | 腾讯云用户 SecretID  |  是  |
| TENCENT_SECRET_KEY | 腾讯云账户 SecretKey |  是  |

### 4.同意Actions条款
- `fork` 完后点击您仓库上方的 `Actions` 里面
- 点击同意使用 `Actions` 条款.
### 5.部署到腾讯云函数serverless
- 添加完上面 `3` 个 `Secrets` 
- 依次点击仓库上方的 `Actions` 、 `Serverless`
- 点击右边的 `Run workflow` 即可部署至腾讯云函数.
# 申明
神州行，我看这是真滴刑！