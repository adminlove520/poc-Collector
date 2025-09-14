#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
项目功能测试脚本
验证主要脚本功能是否正常工作
"""

import os
import sys
import subprocess
import time


def print_separator(title):
    """打印分隔线"""
    print(f"\n{'='*50}")
    print(f"{title.center(50)}")
    print(f"{'='*50}")


def test_token_rate():
    """测试token_rate.py功能"""
    print_separator("测试token_rate.py")
    try:
        result = subprocess.run(
            [sys.executable, "scripts\\token_rate.py", "config\\TOKENS"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            print("✅ token_rate.py测试成功！")
            print(f"输出: {result.stdout[:100]}...")  # 只显示部分输出
        else:
            print(f"❌ token_rate.py测试失败！")
            print(f"错误: {result.stderr}")
        return result.returncode == 0
    except Exception as e:
        print(f"❌ token_rate.py测试异常: {str(e)}")
        return False


def test_download_dir():
    """测试download目录是否存在"""
    print_separator("测试download目录")
    if os.path.exists("download") and os.path.isdir("download"):
        print("✅ download目录已存在！")
        # 查看目录内容
        files = os.listdir("download")
        if files:
            print(f"download目录包含 {len(files)} 个文件")
            print(f"最近的文件: {sorted(files)[-5:]}")  # 显示最近的5个文件
        else:
            print("download目录为空")
        return True
    else:
        print("❌ download目录不存在！")
        return False


def test_chardet_compat():
    """测试chardet_compat模块是否正常工作"""
    print_separator("测试chardet_compat模块")
    try:
        # 添加scripts目录到Python路径
        sys.path.append("scripts")
        
        # 导入兼容性模块
        from chardet_compat import chardet_compat, detect
        
        print(f"✅ 成功导入chardet_compat模块！")
        print(f"使用的字符编码检测库: {chardet_compat.lib_name}")
        
        # 测试编码检测功能
        test_text = "测试中文文本".encode('utf-8')
        result = detect(test_text)
        print(f"编码检测结果: {result}")
        
        if result["encoding"] is not None:
            print("✅ 编码检测功能正常！")
        else:
            print("⚠️ 编码检测可能不正常，返回了None")
        
        return True
    except Exception as e:
        print(f"❌ chardet_compat模块测试异常: {str(e)}")
        return False


def test_async_compat():
    """测试async_compat模块是否正常工作"""
    print_separator("测试async_compat模块")
    try:
        # 添加scripts目录到Python路径
        sys.path.append("scripts")
        
        # 导入兼容性模块
        from async_compat import async_compat, check_async_compatibility
        
        print(f"✅ 成功导入async_compat模块！")
        
        # 检查兼容性
        result = check_async_compatibility()
        print(f"Python版本: {result['python_version']}")
        print(f"有异步支持: {result['has_async_support']}")
        print(f"兼容性: {'兼容' if result['compatible'] else '不兼容'}")
        print(f"建议: {result['recommendation']}")
        
        # 尝试获取异步请求对象
        aio_requests = async_compat.get_requests()
        print(f"异步请求对象: {'可用' if aio_requests else '不可用'}")
        
        return True
    except Exception as e:
        print(f"❌ async_compat模块测试异常: {str(e)}")
        return False


def main():
    """主函数"""
    print("开始测试项目功能...")
    print(f"使用Python: {sys.version}")
    print(f"当前目录: {os.getcwd()}")
    
    # 检查配置文件
    config_files = ["config\\TOKENS", "config\\BLACKLIST.txt"]
    config_ok = True
    for config_file in config_files:
        if not os.path.exists(config_file):
            print(f"❌ 缺少配置文件: {config_file}")
            config_ok = False
        else:
            print(f"✅ 找到配置文件: {config_file}")
    
    # 运行测试
    tests = [
        ("token_rate.py", test_token_rate),
        ("download目录", test_download_dir),
        ("chardet_compat模块", test_chardet_compat),
        ("async_compat模块", test_async_compat)
    ]
    
    success_count = 0
    for name, test_func in tests:
        if test_func():
            success_count += 1
        time.sleep(1)  # 短暂暂停
    
    # 显示测试结果
    print_separator("测试总结")
    print(f"总测试数: {len(tests)}")
    print(f"成功测试数: {success_count}")
    print(f"成功率: {success_count/len(tests)*100:.1f}%")
    
    if success_count == len(tests):
        print("✅ 所有测试通过！项目基础功能正常工作。")
    else:
        print("⚠️ 部分测试失败，请查看上面的错误信息。")
    
    # 提供使用建议
    print_separator("使用建议")
    print("1. 安装依赖: .\\install_deps.ps1")
    print("2. 运行exp.py下载CVE数据: python scripts\\exp.py")
    print("3. 查看今日CVE: python scripts\\today.py")
    print("4. 如有依赖问题，请参考README.md中的解决方案")


if __name__ == "__main__":
    main()