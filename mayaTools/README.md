# -copyright@2021
***
# 拖拽install.mel到maya界面中。或者使用下面脚本进行部署
```python
import sys
in_path = r'../ToolName'
in_path in sys.path and sys.path.remove(in_path)
sys.path.insert(0, in_path)
from in_path import open_ui
reload(open_ui)
open_ui.encryption()
```
