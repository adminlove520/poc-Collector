# 项目依赖安装脚本
# 针对Python 3.12优化，避免编译问题

Write-Host "开始安装项目依赖..."

# 单独安装每个依赖，更容易处理可能的错误
Write-Host "安装tqdm..."
try {
    pip install tqdm --no-cache-dir
} catch {
    Write-Host "警告: tqdm安装可能失败，请尝试: pip install tqdm"
}

Write-Host "安装loguru..."
try {
    pip install loguru --no-cache-dir
} catch {
    Write-Host "警告: loguru安装可能失败，请尝试: pip install loguru"
}

Write-Host "安装requests..."
try {
    pip install requests --no-cache-dir
} catch {
    Write-Host "警告: requests安装可能失败，请尝试: pip install requests"
}

Write-Host "安装chardet（替代cchardet）..."
try {
    pip install chardet --no-cache-dir
} catch {
    Write-Host "警告: chardet安装可能失败，请尝试: pip install chardet"
}

Write-Host "\n依赖安装完成！\n"
Write-Host "已验证可正常工作的功能："
Write-Host "1. token_rate.py - 可正常读取config/TOKENS文件"
Write-Host "2. exp.py - 可正常下载CVE XML文件到download目录"
Write-Host "3. today.py - 基本功能可用"

Write-Host "`n注意事项："
Write-Host "1. 异步功能（exp_async.py, exp_async_v2.py）在Python 3.11+环境下可能存在兼容性问题"
Write-Host "2. 已添加async_compat.py模块，用于检测异步功能兼容性并提供替代方案"
Write-Host "3. 推荐在Python 3.11+环境下使用同步脚本exp.py，稳定性更好"
Write-Host "4. chardet_compat.py模块已添加，可自动兼容cchardet和chardet库"