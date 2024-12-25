import re
from typing import List, Dict, Set
import argparse

def import_text_by_paragraphs(file_path: str) -> List[str]:
    """
    读取文本文件并根据双换行符将其拆分为段落。

    :param file_path: 文本文件的路径。
    :return: 段落列表。
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    paragraphs = text.split('\n\n')  # 根据双换行符拆分
    return paragraphs

def create_regex_pattern(journals: Set[str]) -> re.Pattern:
    """
    创建用于匹配目标期刊的正则表达式模式。

    :param journals: 期刊名称集合。
    :return: 编译后的正则表达式模式。
    """
    pattern = r'\b(' + '|'.join(re.escape(journal) for journal in journals) + r')\b'
    return re.compile(pattern, re.IGNORECASE)

def filter_paragraphs_containing_keywords(paragraphs: List[str]) -> Dict[str, Set[str]]:
    """
    过滤包含目标期刊关键词的段落。

    :param paragraphs: 段落列表。
    :return: 将关键词映射到段落集合的字典。
    """
    target_journals = {
        'Nature', 'Science', 'Science Advances', 'Advanced Materials',
        'Advanced Functional Materials', 'arxiv', 'Physical Review X',
        'Physical Review Letters', 'Nano Letters', 'ACS Nano'
    }
    target_pattern = create_regex_pattern(target_journals)

    partial_pattern = r'\b(Advanced Functional(?: Materials)?)\b'
    partial_regex = re.compile(partial_pattern, re.IGNORECASE)

    exclude_pattern = r'\b(Small Science|Journal of.*Science|.*Science & Technology|Science China|Materials Science|IOP Science|Advanced Science|Applied Surface Science|Light: Science(?:\s*&\s*[^,]*)?|Chemical Science|Structural Science|Advanced Materials Technologies|Progress in Natural Science|Science and Technology of|Surface Science|Cell Reports Physical Science)\b'
    exclude_regex = re.compile(exclude_pattern, re.IGNORECASE)

    keyword_paragraphs: Dict[str, Set[str]] = {}
    keyword_mapping = {
        'science advances': 'Science',
        'nature': 'Nature',
        'advanced materials': 'Advanced Materials',
        'advanced functional materials': 'Advanced Materials',
        'acs nano': 'ACS Nano'
    }

    for paragraph in paragraphs:
        lines = paragraph.strip().split('\n')
        if len(lines) < 2:
            continue  # 跳过不完整的条目

        journal_line = lines[1].strip()
        match = re.search(target_pattern, journal_line)
        partial_match = re.search(partial_regex, journal_line)

        if match or partial_match:
            keyword = match.group(0).strip() if match else 'Advanced Functional Materials'
            if re.search(exclude_regex, journal_line):
                continue  # 排除特定期刊

            keyword = keyword_mapping.get(keyword.lower(), keyword)

            if keyword.lower() == 'nature':
                nature_pattern = r'\b(Nature|Nature [A-Z][a-z]+)\b'
                nature_match = re.search(nature_pattern, journal_line)
                if nature_match:
                    keyword = nature_match.group(0)

            if keyword not in keyword_paragraphs:
                keyword_paragraphs[keyword] = set()
            keyword_paragraphs[keyword].add(paragraph)

    return keyword_paragraphs

def format_paragraph(paragraph: str) -> str:
    """
    格式化段落以用于Markdown输出。

    :param paragraph: 输入段落。
    :return: 格式化后的段落。
    """
    paragraph = paragraph.strip()
    lines = paragraph.split('\n')
    if len(lines) > 1:
        return f"**{lines[0]}**\n*{lines[1]}*\n{''.join(lines[2:])}\n\n"
    else:
        return f"**{lines[0]}**\n\n"

def save_to_markdown(paragraphs: Dict[str, Set[str]], file_name: str = "FileScholar.md") -> None:
    """
    将过滤后的段落保存到Markdown文件中。

    :param paragraphs: 将关键词映射到段落集合的字典。
    :param file_name: 输出Markdown文件的名称。
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        for keyword, keyword_paragraphs in paragraphs.items():
            file.write(f"# {keyword}\n\n")
            for paragraph in keyword_paragraphs:
                formatted_paragraph = format_paragraph(paragraph)
                file.write(formatted_paragraph)

if __name__ == "__main__":
    # 文件路径设置
    new_file = "merged_eml_content.txt"  # 新文件路径
    old_file = "merged_eml_content_20241225_221551.txt"  # 旧文件路径，根据实际时间戳修改
    output_file = "FileScholar.md"  # 输出文件名

    # 处理新文件
    new_paragraphs = import_text_by_paragraphs(new_file)
    new_keyword_paragraphs = filter_paragraphs_containing_keywords(new_paragraphs)

    # 处理旧文件
    old_paragraphs = import_text_by_paragraphs(old_file)
    old_keyword_paragraphs = filter_paragraphs_containing_keywords(old_paragraphs)

    # 创建差异字典
    diff_paragraphs = {}
    
    # 对于新文件中的每个关键词
    for keyword, new_para_set in new_keyword_paragraphs.items():
        # 如果关键词在旧文件中不存在，直接添加所有段落
        if keyword not in old_keyword_paragraphs:
            diff_paragraphs[keyword] = new_para_set
        else:
            # 如果关键词存在，只添加旧文件中没有的段落
            diff_set = new_para_set - old_keyword_paragraphs[keyword]
            if diff_set:
                diff_paragraphs[keyword] = diff_set

    # 保存差异到markdown文件
    save_to_markdown(diff_paragraphs, output_file)
    print(f"差异内容已保存到: {output_file}")
