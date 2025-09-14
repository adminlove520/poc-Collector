#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
异步功能兼容性适配模块
解决Python 3.11+环境下aiohttp相关库的兼容性问题
"""

import sys
import importlib
import warnings


class AsyncCompat:
    """异步功能兼容性适配类"""
    
    def __init__(self):
        """初始化并尝试导入所需的异步库"""
        self.aio_requests = None
        self.aiohttp = None
        self.has_async_support = False
        self.python_version = sys.version_info
        
        # 尝试导入aiohttp_requests和aiohttp
        try:
            # 首先尝试导入aiohttp_requests
            self.aio_requests = importlib.import_module("aiohttp_requests")
            # 尝试导入aiohttp（如果aiohttp_requests已导入成功，这应该也能成功）
            self.aiohttp = importlib.import_module("aiohttp")
            self.has_async_support = True
            print(f"✅ 成功导入异步库，Python版本: {self.python_version.major}.{self.python_version.minor}")
        except ImportError as e:
            # 导入失败，提供警告
            warnings.warn(f"⚠️ 无法导入异步库: {str(e)}")
            warnings.warn("⚠️ 异步功能可能不可用，建议使用同步脚本exp.py")
            self.has_async_support = False
        except Exception as e:
            # 其他错误
            warnings.warn(f"⚠️ 导入异步库时发生错误: {str(e)}")
            self.has_async_support = False
    
    def is_compatible(self):
        """检查当前环境是否支持异步功能"""
        # Python 3.11+ 版本下aiohttp可能存在兼容性问题
        # 特别是缺少longintrepr.h头文件导致的编译错误
        if self.python_version.major > 3 or (self.python_version.major == 3 and self.python_version.minor >= 11):
            if self.has_async_support:
                warnings.warn("⚠️ 在Python 3.11+环境下使用aiohttp可能存在兼容性问题")
                warnings.warn("⚠️ 建议使用同步脚本exp.py或降级到Python 3.10及以下版本")
        
        return self.has_async_support
    
    def get_requests(self):
        """获取异步请求对象"""
        if self.has_async_support:
            # 返回aiohttp_requests中的requests对象
            return self.aio_requests.requests
        else:
            # 如果没有异步支持，返回None
            warnings.warn("❌ 没有可用的异步请求对象")
            return None
    
    def get_aiohttp(self):
        """获取aiohttp库"""
        if self.has_async_support:
            return self.aiohttp
        else:
            warnings.warn("❌ 没有可用的aiohttp库")
            return None


# 创建全局实例，方便其他模块导入使用
async_compat = AsyncCompat()


def check_async_compatibility():
    """检查异步兼容性并返回结果"""
    result = {
        "has_async_support": async_compat.has_async_support,
        "python_version": f"{async_compat.python_version.major}.{async_compat.python_version.minor}",
        "compatible": async_compat.is_compatible(),
        "recommendation": "" 
    }
    
    if not result["compatible"]:
        result["recommendation"] = "建议使用同步脚本exp.py或降级到Python 3.10及以下版本"
    elif async_compat.python_version.major > 3 or (async_compat.python_version.major == 3 and async_compat.python_version.minor >= 11):
        result["recommendation"] = "在Python 3.11+环境下使用异步功能可能不稳定，建议优先使用同步脚本exp.py"
    else:
        result["recommendation"] = "当前环境适合使用异步功能"
    
    return result


# 简单测试（如果直接运行此模块）
if __name__ == "__main__":
    result = check_async_compatibility()
    print(f"异步兼容性检查结果:")
    print(f"- 有异步支持: {result['has_async_support']}")
    print(f"- Python版本: {result['python_version']}")
    print(f"- 兼容性: {'兼容' if result['compatible'] else '不兼容'}")
    print(f"- 建议: {result['recommendation']}")
    
    if result['has_async_support']:
        print("\n✅ 异步功能可用，可以使用exp_async.py或exp_async_v2.py脚本")
    else:
        print("\n❌ 异步功能不可用，建议使用exp.py同步脚本")