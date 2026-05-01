
# 示例 PR Agent

def generate_pr(issues):
    print('生成重构 PR...')
    for issue in issues:
        print(f'改进: {issue}')

if __name__ == '__main__':
    sample_issues = ['函数命名不规范', '缺少单元测试']
    generate_pr(sample_issues)
