import email
from bs4 import BeautifulSoup
from pathlib import Path
import argparse
from datetime import datetime


OUTPUT_PREFIX = "merged_eml_content"


def timestamped_output_path(now=None):
    """Return a timestamped output path for the current parsing run."""
    current_time = now or datetime.now()
    timestamp = current_time.strftime("%Y%m%d_%H%M%S")
    return Path(f"{OUTPUT_PREFIX}_{timestamp}.txt")

def eml_to_text(eml_file):
    with open(eml_file, 'rb') as f:
        msg = email.message_from_binary_file(f)
        
        text = " "
        
        for part in msg.walk():
            if part.get_content_type() == "text/html":
                html_content = part.get_payload(decode=True)
                if isinstance(html_content, bytes):
                    html_content = html_content.decode("utf-8", "ignore")
                # Ensure we have a string before passing to BeautifulSoup
                if not isinstance(html_content, str):
                    html_content = str(html_content)
                # 解析HTML内容并提取文本
                soup = BeautifulSoup(html_content, 'html.parser')
                
                if soup.body and soup.body.div:
                    for child in soup.body.div.contents:
                        text += child.get_text()
                        text += "\n"
                else:
                    # If no body or div, just get all text
                    text += soup.get_text()
        
        
        return text
    

def process_eml_files(directory, eml_contents):
    for item in directory.iterdir():
        if item.is_file():
            if item.suffix.lower() == '.eml':
                print("Parsing:", item.name)
                eml_text = eml_to_text(item)
                eml_contents.append(eml_text)
            elif item.suffix.lower() == '.txt':
                print("Appending:", item.name)
        elif item.is_dir():
            print(f"Entering: {item.name}")
            process_eml_files(item, eml_contents)


if __name__ == "__main__":
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description='合并指定文件夹中的 .eml 文件内容')
    # 添加位置参数，用于获取文件夹路径
    parser.add_argument('folder', type=str, nargs='?', help='包含 .eml 文件的文件夹路径')
    # 解析命令行参数
    args = parser.parse_args()

    if args.folder is None:  # 检查 args.folder 是否为 None
        script_dir = Path("./merged_20260719_20260728")  # 默认相对路径
    else:
        script_dir = Path(args.folder)
    # 确保路径存在并且是一个目录
    if not script_dir.exists() or not script_dir.is_dir():
        raise ValueError(f"错误: {script_dir} 不是一个有效的目录")

    # 列出当前目录下的.eml文件
    eml_contents = []
    process_eml_files(script_dir, eml_contents)

    # 将解析内容合并成一个字符串
    merged_content = "\n".join(eml_contents)

    # 使用本次解析时间命名输出文件，不再生成无时间戳文件
    output_file = timestamped_output_path()
    with open(output_file, 'x', encoding='utf-8') as f:
        f.write(merged_content)

    print("合并后的内容已保存到:", output_file)
