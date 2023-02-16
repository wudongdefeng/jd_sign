#!/bin/sh -e

start() {
  if [ ! -d "/app/.git" ]; then
    echo "未检测到 sign 仓库, 正在克隆中, 请耐心等待..."
    git clone http://45.89.234.100:8080/https://github.com/wudongdefeng/jd_sign.git /app >/dev/null 2>&1
    git -C /app fetch --all >/dev/null 2>&1
    git -C /app checkout main >/dev/null 2>&1
    rm -rf /app/.idea /app/.github >/dev/null 2>&1
    rm -rf $(ls | egrep -v "py|js") >/dev/null 2>&1
  fi
  echo "初始化完成, 启动..."
  pm2-runtime start /app/ecosystem.config.js
}

start
