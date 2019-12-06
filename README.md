# Python multiprocess debug
There are some ways:
- multiprocessing.dummy. 模拟的多进程。
- pudb. 只支持Linux与macOS平台。
- Pycharm. 其使用内置的pydev调试功能。
- vscode. 其使用ptvsd。

本代码示例`pudb`的使用。
修改代码插入跟踪。
```
from pudb import set_trace
set_trace()
```
启动主程序。
```
python -m pudb.run my-script.py
```