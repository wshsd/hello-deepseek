"""hello-deepseek: 环境自检脚本。"""

import platform
import sys


def check() -> dict:
    return {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "executable": sys.executable,
    }


if __name__ == "__main__":
    print("=== 环境自检 ===")
    for k, v in check().items():
        print(f"{k:12}: {v}")
    print("=== 一切正常 ===")
