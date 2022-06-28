#将需要的代码复制并cd到severless文件夹
echo "开始拷贝必要文件"
sudo cp app.py ./serverless
sudo cp scf_bootstrap ./serverless
sudo cp requirements.txt ./serverless

echo "开始安装所需模块"
cd ./serverless
sudo -H pip install --upgrade setuptools >/dev/null
sudo -H pip install -r ./requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/ -t ./

#部署至腾讯云函数
if [ -z "$TENCENT_SECRET_ID" ] || [ -z "$TENCENT_SECRET_KEY" ]; then
  echo "部署至腾讯云需要填写TENCENT_SECRET_ID和TENCENT_SECRET_KEY两个secrets，跳过部署"
else
  echo "开始安装腾讯ServerlessFramework"
  sudo npm install -g serverless
  echo "开始部署至腾讯云函数"
  sls deploy --debug
  exit 0
fi
