#!/usr/bin/env python3
import subprocess
from datetime import datetime

def copy_to_clipboard(text):
    try:
        subprocess.run("pbcopy", text=True, input=text)
        print("\n✅ 已复制到剪贴板，可直接 ⌘V 粘贴\n")
    except Exception:
        print("\n⚠️ 无法复制到剪贴板，请手动复制。\n")

def now_str():
    try:
        return datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")
    except Exception:
        return datetime.now().strftime("%Y-%m-%d %H:%M")

def generate_fr(name, item, seat):
    template = f"""Dear {name},

Thanks for your request for {item}.

We are currently processing this request for you, item will be delivered to your seat {seat}.

We will be contacting you should there be any queries. Please expect an update before 4 PM today.

Stanley
"""
    print("\n=== FR_canned 内容如下 ===\n")
    print(template)
    copy_to_clipboard(template)

def generate_rr(name, item, seat, asset):
    current_time = now_str()
    template = f"""Hi {name},

{item} has been delivered to your desk {seat} as noted in MOMA.

Delivery Time is {current_time}, Asset Tag is {asset}.

Please note that once the order is delivered, we are unable to see and respond to updates in this order. 
If you need further help, please submit a request through go/stuff by selecting “Have questions about your order?”, or by opening a ticket at go/emt-request.

Regards,
Stanley
"""
    print("\n=== RR_canned 内容如下 ===\n")
    print(template)
    copy_to_clipboard(template)

def main():
    print("🪄 Full Canned Response Generator\n")

    # 一次输入全部参数
    name = input("Enter user's first name: ").strip()
    item = input("Enter item: ").strip()
    seat = input("Enter seat number: ").strip()
    asset = input("Enter asset tag: ").strip()

    # 生成 FR
    generate_fr(name, item, seat)
    cont = input("是否继续生成 RR_canned？(y/n): ").strip().lower()
    if cont in ["y", "yes"]:
        generate_rr(name, item, seat, asset)
    else:
        print("\n✅ 已结束，仅生成 FR_canned。\n")

if __name__ == "__main__":
    main()
