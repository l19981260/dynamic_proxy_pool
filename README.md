# dynamic_proxy_pool
python实现动态代理池

#### 运行环境
- python 3.6
- redis

####安装依赖

```
pip install aiohttp
pip install Flask
pip install redis
pip install requests
pip install pyquery
```
#### 配置
```
cd proxypool
```
进入proxypool目录，修改settings.py文件中 REDIS_HOST REDIS_PORT REDIS_PASSWORD 为您使用的redis数据库地址，端口号，密码
#### 使用
```
python3 run.py
```
#### 获取
```python
import requests
PROXY_POOL_URL = 'http://localhost:5000/random'
def get_proxy():
    try:
        return requests.get(PROXY_POOL_URL).text
    except ConnectionError:
        return None
```
#### 思路
https://www.zhihu.com/question/25566731
