# PocOrExp_in_Github

# PocOrExp_in_Github

一个用于CVE漏洞信息获取和分析的工具集合。

## 项目结构

该项目已按代码与配置分离的最佳实践进行重构，主要包含以下目录结构：

```
├── config/            # 配置文件目录（敏感信息存放处）
│   ├── BLACKLIST.txt  # 黑名单配置
│   └── TOKENS         # API令牌配置
├── scripts/           # 主要脚本文件
│   ├── exp.py         # 基础CVE信息获取脚本
│   ├── exp_async.py   # 异步版CVE信息获取脚本
│   ├── exp_async_v2.py # 优化后的异步版CVE信息获取脚本
│   ├── today.py       # 今日CVE信息获取脚本
│   └── token_rate.py  # 令牌使用速率监控脚本
├── download/          # 下载的CVE XML文件存放目录
├── install_deps.ps1   # 依赖安装脚本（Windows专用）
└── requirements.txt   # 项目依赖说明文件
```

## 快速开始

### 1. 安装依赖

由于项目在Python 3.12环境中存在一些依赖兼容性问题，推荐使用提供的PowerShell安装脚本来安装基本依赖：

```powershell
# 在PowerShell中运行
.\install_deps.ps1
```

或者手动安装：

```powershell
pip install tqdm
pip install loguru
pip install requests
pip install chardet
```

> **注意**：某些异步功能可能需要额外安装aiohttp，但可能会遇到cchardet编译问题。基础功能不依赖这些组件。

### 2. 配置文件设置

在运行脚本前，请确保`config`目录下包含必要的配置文件：
- `TOKENS`：包含API访问令牌
- `BLACKLIST.txt`：包含需要排除的条目

### 3. 运行脚本

#### token_rate.py
监控API令牌使用情况：

```powershell
python scripts\token_rate.py config\TOKENS
```

#### exp.py
下载CVE XML文件：

```powershell
python scripts\exp.py
```

下载的文件将保存在`download`目录中。

#### today.py
获取今日发布的CVE信息：

```powershell
python scripts\today.py
```

## 已知问题与解决方案

1. **Python 3.12兼容性问题**：
   - cchardet库无法在Python 3.12中编译，错误提示缺少'longintrepr.h'文件
   - 解决方案：使用chardet替代cchardet（纯Python实现）
   - 尝试方法（可能不适用Python 3.12）：
     ```powershell
     pip install cython  # 先安装Cython
     pip install cchardet  # 再尝试安装cchardet
     ```

2. **依赖安装问题**：
   - 尝试使用`--no-build-isolation`参数安装：
     ```powershell
     pip install --no-build-isolation 包名
     ```
   - 或使用`--no-cache-dir`参数避免缓存问题
   - 对于编译问题，可以使用`--only-binary :all:`参数安装预编译的二进制包
     ```powershell
     pip install --only-binary :all: 包名
     ```

3. **异步功能依赖问题**：
   - 项目中的异步脚本（exp_async.py, exp_async_v2.py）使用了aiohttp_requests，可能间接依赖cchardet
   - 解决方案：使用提供的async_compat.py兼容性模块，可以检测当前环境是否支持异步功能
      ```python
      # 在代码中导入兼容性模块
      from async_compat import async_compat, check_async_compatibility
      
      # 检查异步功能是否支持
      result = check_async_compatibility()
      if result['compatible']:
          # 获取异步请求对象
          aio_requests = async_compat.get_requests()
          if aio_requests:
              # 使用异步功能
              response = await aio_requests.get(url, headers=headers)
      else:
          # 使用同步替代方案（如requests库）
          import requests
          response = requests.get(url, headers=headers)
      ```
   - 说明：在Python 3.11+环境下，建议优先使用同步脚本`exp.py`，如需使用异步功能，请参考`async_compat.py`中的兼容性解决方案

4. **文件路径问题**：
   - 所有脚本已更新为使用绝对路径，解决了相对路径导致的文件找不到问题
   - 确保在项目根目录下运行脚本

## 项目功能验证

以下功能已测试并确认可正常工作：
- ✅ `token_rate.py` - 可正常读取`config/TOKENS`文件并显示令牌信息
- ✅ `exp.py` - 可正常下载CVE XML文件到`download`目录
- ✅ 配置文件结构重构 - 代码与配置分离，提高安全性和可维护性

## 注意事项

- 本项目仅供学习和研究使用
- 请遵守相关法律法规，合理使用工具
- 定期更新依赖以确保最佳性能和安全性