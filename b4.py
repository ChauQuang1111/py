# 100. Same Tree
from collections import deque
from typing import Optional

# Định nghĩa TreeNode theo chuẩn LeetCode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Hàng đợi lưu cặp node để so sánh song song
        queue = deque([p, q])  

        while queue:
            # Lấy ra 2 node để so sánh
            node1 = queue.popleft()
            node2 = queue.popleft()

            # Nếu cả hai đều null → tiếp tục vòng lặp
            if not node1 and not node2:
                continue

            # Nếu chỉ 1 node null → khác nhau
            if not node1 or not node2:
                return False

            # Nếu giá trị khác nhau → khác nhau
            if node1.val != node2.val:
                return False

            # Thêm cặp con trái và cặp con phải vào hàng đợi để so sánh tiếp
            queue.append(node1.left)
            queue.append(node2.left)
            queue.append(node1.right)
            queue.append(node2.right)

        # Nếu duyệt hết mà không có sai khác → hai cây giống nhau
        return True
