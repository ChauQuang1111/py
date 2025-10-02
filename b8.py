# # 23. Merge k Sorted Lists
# Ok 👍 mình sẽ **giải thích chi tiết thuật toán** và thêm **chú thích vào code** cho bạn:

# ---

# ### 💡 Ý tưởng thuật toán:

# * Ta có `k` danh sách liên kết đã được **sắp xếp tăng dần**.
# * Ta muốn gộp tất cả thành **1 danh sách duy nhất cũng sắp xếp tăng dần**.
# * Nếu ta chỉ nối rồi sắp xếp lại thì sẽ mất **O(N log N)** (N là tổng số node).
# * Thay vào đó, ta dùng **Min-Heap (priority queue)**:

#   * Luôn lưu phần tử nhỏ nhất hiện tại từ mỗi danh sách.
#   * Mỗi lần pop ra phần tử nhỏ nhất rồi nối vào kết quả.
#   * Nếu phần tử đó còn `next`, ta đưa `next` vào heap.
#   * Lặp cho đến khi heap rỗng.

# → Độ phức tạp: **O(N log k)** (mỗi node push + pop khỏi heap, heap có tối đa `k` phần tử).

# ---

# ### ✅ Code có chú thích:

# ```python
import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Min-heap: sẽ chứa tuple (giá trị node, index, node)
        # Dùng index để tránh lỗi khi 2 node có cùng giá trị (Python không so sánh được object trực tiếp)
        heap = []
        
        # 1. Đưa node đầu tiên của mỗi danh sách vào heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
                # push giá trị node, index danh sách, và node đó
        
        # Dummy node để dễ quản lý danh sách kết quả
        dummy = ListNode(-1)
        curr = dummy

        # 2. Xử lý heap cho đến khi rỗng
        while heap:
            # Lấy ra node có giá trị nhỏ nhất hiện tại
            val, i, node = heapq.heappop(heap)

            # Gắn node này vào danh sách kết quả
            curr.next = node
            curr = curr.next

            # Nếu node này còn phần tử tiếp theo -> đưa node.next vào heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        # Trả về danh sách đã gộp (bỏ dummy)
        return dummy.next
# ```

# ---

### 🔑 Ví dụ minh họa:

# Giả sử ta có 3 danh sách:

# ```
# list1: 1 -> 4 -> 5
# list2: 1 -> 3 -> 4
# list3: 2 -> 6
# ```

# * Heap ban đầu = `[1(list1), 1(list2), 2(list3)]`
# * Pop 1(list1), thêm `4(list1)` → kết quả `1`
# * Heap = `[1(list2), 2(list3), 4(list1)]`
# * Pop 1(list2), thêm `3(list2)` → kết quả `1 -> 1`
# * Cứ thế cho đến hết...

# Kết quả cuối cùng:

# ```
# 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
# ```

# ---

# 👉 Bạn có muốn mình viết thêm **hàm main Python** để nhập danh sách từ `stdin` (giống bản Java dùng `Scanner`) không?
