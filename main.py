"""hello-deepseek: 鐜鑷鑴氭湰銆?""
import sys
import platform


def check() -> dict:
    return {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "executable": sys.executable,
    }


if __name__ == "__main__":
    print("=== 鐜鑷 ===")
    for k, v in check().items():
        print(f"{k:12}: {v}")
    print("=== 涓€鍒囨甯?===")