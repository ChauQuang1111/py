# # 94. Binary Tree Inorder Traversal
from typing import List, Optional
# # Định nghĩa node của cây nhị phân
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.dfs(root, result)
        return result

    def dfs(self, node: Optional[TreeNode], result: List[int]):
        if not node:
            return
        # 1. duyệt trái
        self.dfs(node.left, result)
        # 2. thăm gốc
        result.append(node.val)
        # 3. duyệt phải
        self.dfs(node.right, result)



# Ok 👍 mình giải thích chi tiết nhé:

# Đây là **thuật toán duyệt cây nhị phân theo thứ tự trung tố (Inorder Traversal)**.

# ---

# ### 1️⃣ Ý tưởng của Inorder Traversal

# * Cây nhị phân có 3 kiểu duyệt cơ bản:

#   * **Preorder (NLR)**: Node → Left → Right
#   * **Inorder (LNR)**: Left → Node → Right
#   * **Postorder (LRN)**: Left → Right → Node

# Ở đây, ta dùng **Inorder (LNR)**:

# 1. Duyệt **cây con bên trái**.
# 2. Ghé thăm **nút hiện tại (node)**.
# 3. Duyệt **cây con bên phải**.

# ---

# ### 2️⃣ Thuật toán trong code

# ```python
# def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#     result = []
#     self.dfs(root, result)
#     return result
# ```

# * `result`: danh sách chứa kết quả cuối cùng.
# * Gọi hàm `dfs` để thực hiện duyệt đệ quy.

# ```python
# def dfs(self, node: Optional[TreeNode], result: List[int]):
#     if not node:
#         return
#     # 1. duyệt trái
#     self.dfs(node.left, result)
#     # 2. thăm gốc
#     result.append(node.val)
#     # 3. duyệt phải
#     self.dfs(node.right, result)
# ```

# 👉 Từng bước:

# * Nếu `node == None` (cây rỗng hoặc tới lá) thì **quay lui**.
# * Gọi đệ quy duyệt **con trái** trước.
# * Thêm giá trị `node.val` vào `result`.
# * Gọi đệ quy duyệt **con phải**.

# ---

# ### 3️⃣ Ví dụ minh họa

# Cho cây:

# ```
#     1
#      \
#       2
#      /
#     3
# ```

# * Bắt đầu từ `1` → đi sang trái (không có gì).
# * Thêm `1` vào kết quả → `[1]`.
# * Sang phải (`2`) → duyệt trái (`3`).
# * `3` không có trái, thêm `3` vào kết quả → `[1, 3]`.
# * Quay lại `2`, thêm `2` vào kết quả → `[1, 3, 2]`.

# ✅ Kết quả cuối cùng: `[1, 3, 2]`.

# ---

# 📌 Thuật toán này có:

# * **Độ phức tạp thời gian**: `O(n)` (mỗi node được thăm đúng 1 lần).
# * **Độ phức tạp bộ nhớ**: `O(h)` (h là chiều cao cây, do dùng ngăn xếp đệ quy).

# ---

# Bạn có muốn mình viết lại thuật toán này theo **cách không đệ quy (iterative, dùng stack)** để so sánh không?
# Đúng rồi 👍 cái bạn đang viết chính là **đệ quy DFS (Depth-First Search)**.
# Cụ thể:

# * DFS có 3 cách duyệt chính trên cây nhị phân:

#   * **Inorder (LNR)**: Trái → Gốc → Phải
#   * **Preorder (NLR)**: Gốc → Trái → Phải
#   * **Postorder (LRN)**: Trái → Phải → Gốc

# Hàm bạn viết đang dùng **Inorder DFS**, và việc gọi lại `self.dfs(node.left, result)` hay `self.dfs(node.right, result)` chính là bản chất của đệ quy trong DFS.

# ---

# 📌 Nếu bạn thấy "giống đệ quy quá", thì đúng luôn 😆 vì **Inorder traversal thực chất là một dạng DFS được triển khai bằng đệ quy**.

# ---

# 👉 Nếu bạn muốn thấy rõ sự khác biệt, có thể viết lại **phiên bản DFS không dùng đệ quy (iterative)** với `stack` như sau:

# ```python
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result, stack = [], []
#         current = root

#         while current or stack:
#             # đi hết nhánh trái
#             while current:
#                 stack.append(current)
#                 current = current.left
#             # lấy nút ra và xử lý
#             current = stack.pop()
#             result.append(current.val)
#             # sang phải
#             current = current.right

#         return result
# ```

# ---

# 🔑 So sánh:

# * **Đệ quy**: ngắn gọn, dễ viết → nhưng phụ thuộc vào stack của hệ thống (dễ tràn stack nếu cây quá sâu).
# * **Không đệ quy (iterative)**: dùng stack thủ công → kiểm soát tốt hơn, tránh tràn stack.

# ---

# Bạn muốn mình so sánh **DFS (Inorder) và BFS (Level-order)** để thấy sự khác biệt rõ hơn không?
