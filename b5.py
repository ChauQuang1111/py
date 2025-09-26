# 19. Remove Nth Node From End of List
from typing import Optional

# Định nghĩa node của Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Tạo dummy node trỏ vào head để xử lý trường hợp xóa node đầu
        dummy = ListNode(0, head)
        fast = dummy  # con trỏ nhanh
        slow = dummy  # con trỏ chậm

        # Bước 1: cho fast chạy trước n+1 bước
        # Lý do: khi fast đến cuối, slow sẽ đứng ngay TRƯỚC node cần xóa
        for _ in range(n + 1):
            fast = fast.next

        # Bước 2: di chuyển fast và slow song song cho đến khi fast null
        while fast:
            fast = fast.next
            slow = slow.next

        # Bước 3: xóa node sau slow (chính là node thứ n từ cuối)
        slow.next = slow.next.next

        # Trả về head mới (bỏ qua dummy)
        return dummy.next

# Rồi 👍 mình sẽ giải thích chi tiết **thuật toán** trong code Python của bạn (Remove Nth Node From End of List).

# ---

# ## 📝 Ý tưởng chính

# * Đề yêu cầu: xóa node **thứ n từ cuối** trong Linked List.
# * Vấn đề: ta không biết trước độ dài list, nên khó tính vị trí node cần xóa từ đầu.
# * Giải pháp: dùng **two pointers** (fast & slow).

# ---

# ## 🔎 Giải thích từng bước trong code

# ```python
# dummy = ListNode(0, head)
# fast = dummy
# slow = dummy
# ```

# 👉 Tạo một **dummy node** đứng trước head. Dummy giúp xử lý trường hợp đặc biệt như xóa node đầu tiên (`head`).

# * Ban đầu cả `fast` và `slow` đều trỏ vào `dummy`.

# ---

# ```python
# for _ in range(n + 1):
#     fast = fast.next
# ```

# 👉 Di chuyển `fast` **n+1 bước** về phía trước.

# * Tại sao phải `n+1`?

#   * Vì ta muốn khi `fast` đến cuối (null), thì `slow` đứng ngay **trước node cần xóa**.
#   * Nếu chỉ đi `n` bước thì `slow` sẽ đứng **ở node cần xóa**, khó để chỉnh `slow.next`.

# ---

# ```python
# while fast:
#     fast = fast.next
#     slow = slow.next
# ```

# 👉 Tiếp tục cho cả `fast` và `slow` di chuyển cùng lúc.

# * Khi `fast` chạm `null` → `slow` đứng ngay **trước node cần xóa**.

# ---

# ```python
# slow.next = slow.next.next
# ```

# 👉 Xóa node cần xóa bằng cách:

# * Bỏ qua `slow.next` (node cần xóa).
# * Nối `slow.next` sang `slow.next.next`.

# ---

# ```python
# return dummy.next
# ```

# 👉 Trả về `dummy.next` làm head mới (bỏ qua node giả `dummy`).

# ---

# ## 📌 Ví dụ minh họa

# Input: `head = [1,2,3,4,5], n = 2`

# 1. Dummy: `0 -> 1 -> 2 -> 3 -> 4 -> 5`

#    * `fast = dummy`, `slow = dummy`.

# 2. `fast` chạy trước `n+1 = 3` bước → `fast` ở node `3`.

# 3. Di chuyển song song:

#    * Lần 1: `fast=4`, `slow=1`
#    * Lần 2: `fast=5`, `slow=2`
#    * Lần 3: `fast=null`, `slow=3`

#    → `slow` đứng ngay trước node `4`.

# 4. `slow.next = slow.next.next`
#    → Xóa node `4`.

# Kết quả: `1 -> 2 -> 3 -> 5`. ✅

# ---

# 👉 Tóm lại:

# * **fast chạy trước n+1 bước** → đảm bảo khi fast hết list, slow đứng ngay trước node cần xóa.
# * **slow.next = slow.next.next** để xóa node.
# * **dummy** giúp xử lý dễ dàng trường hợp xóa head.

# ---

# Bạn có muốn mình viết thêm **hàm build linked list từ array** và **print linked list** trong Python để dễ test code không?
