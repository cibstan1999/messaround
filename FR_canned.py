#!/usr/bin/env python3
import subprocess

template = """Dear {name},

Thanks for your request for [{item}].

We are currently processing this request for you, item will be delivered to your seat [{seat}].

We will be contacting you should there be any queries. Please expect an update before 4 PM today.

Stanley
"""

def main():
    print("=== Canned Response Generator ===")
    name = input("Enter user's first name: ").strip()
    item = input("Enter requested item: ").strip()
    seat = input("Enter seat number: ").strip()

    response = template.format(name=name, item=item, seat=seat)

    print("\n✅ Generated response:\n")
    print(response)

    # 自动复制到 macOS 剪贴板
    subprocess.run("pbcopy", universal_newlines=True, input=response)
    print("\n(已复制到剪贴板，可直接 ⌘V 粘贴)\n")

if __name__ == "__main__":
    main()

