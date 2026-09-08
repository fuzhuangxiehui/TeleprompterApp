#!/usr/bin/env python3
"""
软著申请源代码提取工具

从项目中提取源代码，生成符合软著申请要求的格式：
- 前30页 + 后30页（每页50行）
- 去除空行和注释过多的情况
- 页眉标注软件名称和版本号

使用方法：
    python3 release/extract_source_for_copyright.py

输出：
    release/copyright_source_front.txt   — 前30页
    release/copyright_source_back.txt     — 后30页
"""

import os
import re

# ===== 配置 =====
SOFTWARE_NAME = "提词器"
SOFTWARE_VERSION = "V1.0"
SOURCE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                          "app", "src", "main", "java", "com", "teleprompter", "app")
LINES_PER_PAGE = 50
FRONT_PAGES = 30
BACK_PAGES = 30
# ================

def collect_source_files(source_dir):
    """收集所有源代码文件，按路径排序"""
    files = []
    for root, dirs, filenames in os.walk(source_dir):
        for f in sorted(filenames):
            if f.endswith(('.kt', '.java')):
                filepath = os.path.join(root, f)
                files.append(filepath)
    return sorted(files)

def read_and_clean(filepath):
    """读取源代码文件，保留有意义的行"""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 保留所有非空行（软著要求包含正常代码，不需要过度精简）
    cleaned = []
    for line in lines:
        # 去掉行尾空白但保留缩进
        cleaned.append(line.rstrip())

    return cleaned

def format_output(lines, start_page=1):
    """格式化输出：每页50行，带页眉"""
    output = []
    total_pages = (len(lines) + LINES_PER_PAGE - 1) // LINES_PER_PAGE

    for page in range(total_pages):
        page_num = start_page + page
        start_idx = page * LINES_PER_PAGE
        end_idx = min(start_idx + LINES_PER_PAGE, len(lines))
        page_lines = lines[start_idx:end_idx]

        # 页眉
        output.append(f"{'='*60}")
        output.append(f"软件名称：{SOFTWARE_NAME}  版本号：{SOFTWARE_VERSION}  第{page_num}页")
        output.append(f"{'='*60}")

        # 代码行
        for i, line in enumerate(page_lines):
            line_num = start_idx + i + 1
            output.append(f"{line_num:4d} | {line}")

        # 补足50行
        remaining = LINES_PER_PAGE - len(page_lines)
        for _ in range(remaining):
            output.append("")

    return output

def main():
    print(f"扫描源代码目录: {SOURCE_DIR}")
    source_files = collect_source_files(SOURCE_DIR)

    if not source_files:
        print("❌ 未找到源代码文件！")
        return

    print(f"找到 {len(source_files)} 个源代码文件:")
    for f in source_files:
        print(f"  - {os.path.basename(f)}")

    # 合并所有源代码
    all_lines = []
    for filepath in source_files:
        lines = read_and_clean(filepath)
        # 文件间分隔
        rel_path = os.path.relpath(filepath, os.path.dirname(SOURCE_DIR))
        all_lines.append(f"// ===== 文件: {os.path.basename(filepath)} =====")
        all_lines.extend(lines)
        all_lines.append("")  # 文件间空行

    total_lines = len(all_lines)
    print(f"\n总行数: {total_lines}")
    print(f"需要: 前{FRONT_PAGES}页({FRONT_PAGES * LINES_PER_PAGE}行) + 后{BACK_PAGES}页({BACK_PAGES * LINES_PER_PAGE}行)")

    # 前30页
    front_lines = all_lines[:FRONT_PAGES * LINES_PER_PAGE]
    front_output = format_output(front_lines, start_page=1)

    # 后30页
    back_start = max(0, total_lines - BACK_PAGES * LINES_PER_PAGE)
    back_lines = all_lines[back_start:]
    back_output = format_output(back_lines, start_page=FRONT_PAGES + 1)

    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    front_path = os.path.join(output_dir, "copyright_source_front.txt")
    back_path = os.path.join(output_dir, "copyright_source_back.txt")

    with open(front_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(front_output))
    print(f"\n✅ 前30页已保存: {front_path}")

    with open(back_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(back_output))
    print(f"✅ 后30页已保存: {back_path}")

    print(f"\n📝 软著申请时提交这两个文件即可。")

if __name__ == "__main__":
    main()