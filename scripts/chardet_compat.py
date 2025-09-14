#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
字符编码检测库兼容性适配模块
当cchardet不可用时，自动使用chardet作为替代
"""

import sys
import importlib


class ChardetCompat:
    """字符编码检测兼容性适配类"""
    
    def __init__(self):
        """初始化并尝试导入cchardet或chardet"""
        self.chardet_lib = None
        self.lib_name = ""
        
        # 首先尝试导入cchardet
        try:
            self.chardet_lib = importlib.import_module("cchardet")
            self.lib_name = "cchardet"
            return
        except ImportError:
            pass
        
        # cchardet不可用，尝试导入chardet
        try:
            self.chardet_lib = importlib.import_module("chardet")
            self.lib_name = "chardet"
            return
        except ImportError:
            pass
        
        # 两个库都不可用，给出警告
        print("警告: 未找到cchardet或chardet库，字符编码检测功能可能不可用")
    
    def detect(self, bytes_data):
        """检测字节数据的编码"""
        if self.chardet_lib is None:
            # 默认返回utf-8
            return {"encoding": "utf-8", "confidence": 0.5}
        
        if self.lib_name == "cchardet":
            # cchardet的API
            return self.chardet_lib.detect(bytes_data)
        else:
            # chardet的API
            return self.chardet_lib.detect(bytes_data)


# 创建全局实例，方便其他模块导入使用
chardet_compat = ChardetCompat()


# 提供与cchardet兼容的API
if chardet_compat.chardet_lib is not None:
    if chardet_compat.lib_name == "cchardet":
        # 直接使用cchardet的API
        detect = chardet_compat.chardet_lib.detect
    else:
        # 使用chardet的API，但保持与cchardet相同的接口
        detect = chardet_compat.chardet_lib.detect
else:
    # 提供一个简单的默认实现
    def detect(bytes_data):
        """默认的编码检测实现"""
        return {"encoding": "utf-8", "confidence": 0.5}


# 注册到系统模块，让其他模块可以通过import chardet_compat来使用
# 这样可以在需要时替换cchardet的导入
if __name__ == "__main__":
    # 简单测试
    test_text = "测试中文文本".encode('utf-8')
    result = detect(test_text)
    print(f"使用 {chardet_compat.lib_name} 检测编码: {result}")