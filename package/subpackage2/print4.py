
print(4)
 # 如果在当前文件想使用subpackage1中的print1文件，用from导入
 
from  package.subpackage1 import print1
print1()
from  package.subpackage1.print1 import a # 只使用其中的变量a10
print(a)
from  package.subpackage1 import * # 导入subpackage1下面的所有pathon文件，其实触发的是subpackage1下面的__init__.py文件



# 从当前导入同一个package里面的统一级别的文件
from . import print3

# 如果调用整个package，则需要创建一个跟package统计的目录，见run_package.py,这样就可以调用整个包