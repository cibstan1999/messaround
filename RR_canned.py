#!/usr/bin/env python3
import sys
import subprocess
from datetime import datetime, timezone

TEMPLATE = """Hi {name},

[{item}] has been delivered to your desk [{seat}] as noted in MOMA.

Delivery Time is [{time}], Asset Tag is [{asset}].

Please note that once the order is delivered, we are unable to see and respond to updates in this order. 
If you need further help, please submit a request through go/stuff by selecting "Have questions about your order?", or by opening a ticket at go/emt-request.

Regards,
Stanley
"""

def now_str():
    try:
        return datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")
    except Exception:
        return datetime.now().strftime("%Y-%m-%d %H:%M")

def main():
    if len(sys.argv) == 5:
        name = sys.argv[1]
        item = sys.argv[2]
        seat = sys.argv[3]
        asset = sys.argv[4]
    else:
        print("=== RR_canned Generator ===")
        name = input("Enter user's first name: ").strip()
        item = input("Enter item: ").strip()
        seat = input("Enter seat number: ").strip()
        asset = input("Enter asset tag: ").strip()

    current_time = now_str()
    output = TEMPLATE.format(name=name, item=item, seat=seat, time=current_time, asset=asset)

    print("\n✅ Generated message:\n")
    print(output)

    try:
        subprocess.run("pbcopy", universal_newlines=True, input=output)
        print("\n(已复制到剪贴板，可直接 ⌘V 粘贴)\n")
    except Exception as e:
        print("\n(复制到剪贴板失败：", e, ")\n")

if __name__ == "__main__":
    main()
