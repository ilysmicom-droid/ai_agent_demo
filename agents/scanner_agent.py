
# 示例扫描 Agent
import os

def scan_code(path):
    print(f'正在扫描 {path} 中的代码...')
    # 这里可以模拟扫描逻辑
    issues = ['函数命名不规范', '缺少单元测试']
    return issues

if __name__ == '__main__':
    issues = scan_code('../example_code')
    print('扫描结果:', issues)
