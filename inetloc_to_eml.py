#!/usr/bin/env python3
"""Export an Apple Mail message referenced by a .inetloc file as .eml."""

import argparse
import plistlib
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote, unquote, urlparse


MAIL_SOURCE_SCRIPT = r"""
on run argv
    set targetID to item 1 of argv
    set targetURL to item 2 of argv
    set candidateIDs to {targetID}
    if targetID starts with "<" and targetID ends with ">" then
        set end of candidateIDs to text 2 thru -2 of targetID
    end if

    open location targetURL
    repeat 20 times
        delay 0.25
        tell application "Mail"
            set selectedMessages to selection
            if (count of selectedMessages) > 0 then
                set selectedMessage to item 1 of selectedMessages
                set selectedID to message id of selectedMessage
                if candidateIDs contains selectedID then
                    return source of selectedMessage
                end if
            end if
        end tell
    end repeat

    tell application "Mail"
        repeat with acctRef in every account
            repeat with boxRef in every mailbox of acctRef
                repeat with candidateID in candidateIDs
                    try
                        set foundMessages to (every message of boxRef whose message id is (contents of candidateID))
                        if (count of foundMessages) > 0 then
                            return source of item 1 of foundMessages
                        end if
                    end try
                end repeat
            end repeat
        end repeat
    end tell

    error "Mail 中未找到 Message-ID: " & targetID number 44
end run
"""


def message_id_from_inetloc(path: Path) -> str:
    with path.open("rb") as file:
        data = plistlib.load(file)

    url = data.get("URL")
    if not isinstance(url, str):
        raise ValueError("inetloc 文件中没有有效的 URL")

    parsed = urlparse(url)
    if parsed.scheme.lower() != "message":
        raise ValueError(f"不是 Apple Mail 的 message: 链接：{url}")

    message_id = unquote(parsed.path)
    if not message_id:
        raise ValueError("message: 链接中没有 Message-ID")
    return message_id


def mail_source(message_id: str) -> bytes:
    message_url = "message:" + quote(message_id, safe="@.")
    result = subprocess.run(
        ["osascript", "-", message_id, message_url],
        input=MAIL_SOURCE_SCRIPT.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        error = result.stderr.decode("utf-8", "replace").strip()
        raise RuntimeError(error or f"osascript 退出状态：{result.returncode}")
    return result.stdout


def main() -> int:
    parser = argparse.ArgumentParser(
        description="把 Apple Mail 的 .inetloc 邮件快捷方式导出为 .eml"
    )
    parser.add_argument("inetloc", type=Path, help=".inetloc 文件路径")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="输出路径（默认与输入文件同目录、同名但扩展名为 .eml）",
    )
    args = parser.parse_args()

    source_path = args.inetloc.expanduser()
    output_path = args.output.expanduser() if args.output else source_path.with_suffix(".eml")

    if source_path.suffix.lower() != ".inetloc":
        parser.error("输入文件扩展名必须是 .inetloc")
    if not source_path.is_file():
        parser.error(f"文件不存在：{source_path}")
    if output_path.exists():
        parser.error(f"为避免覆盖，输出文件已存在：{output_path}")

    try:
        message_id = message_id_from_inetloc(source_path)
        print(f"Message-ID: {message_id}")
        print("正在从 Mail 查找邮件……")
        source = mail_source(message_id)
        output_path.write_bytes(source)
    except (OSError, ValueError, RuntimeError, plistlib.InvalidFileException) as error:
        print(f"转换失败：{error}", file=sys.stderr)
        return 1

    print(f"已保存：{output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
