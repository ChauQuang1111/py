# 95. Unique Binary Search Trees II
# Rồi 👍. Đây là cách giải bài **95. Unique Binary Search Trees II** với **memoization** (lưu kết quả để tránh tính lại).
# Mình sẽ giải thích thuật toán, sau đó thêm chú thích từng dòng vào code của bạn.

# ---

# ## 🔎 Giải thích thuật toán

# * Mục tiêu: Tạo **tất cả các cấu trúc cây nhị phân tìm kiếm (BST)** khác nhau có thể được tạo từ các số `1 → n`.

# * Ý tưởng:

#   1. Mỗi số `i` trong khoảng `[start, end]` có thể làm **root**.
#   2. Các số nhỏ hơn `i` sẽ tạo thành **cây con bên trái** (left subtree).
#   3. Các số lớn hơn `i` sẽ tạo thành **cây con bên phải** (right subtree).
#   4. Kết hợp mọi khả năng của cây con trái và cây con phải để tạo thành một cây mới.
#   5. Sử dụng **memoization** (bộ nhớ đệm) để lưu kết quả của `generate_trees(start, end)` nhằm tránh tính lại.

# * Trường hợp dừng:

#   * Nếu `start > end`, nghĩa là không có số nào để tạo cây ⇒ trả về `[None]` (tức là một cây rỗng).

# * Độ phức tạp:

#   * Thời gian: **O(Cn * n)**, trong đó `Cn` là số Catalan (số lượng BST có thể sinh ra).
#   * Không gian: phụ thuộc số lượng cây được sinh ra + memo.

# ---

# ## 📌 Code với chú thích chi tiết

# ```python
from typing import List, Optional

# Định nghĩa cấu trúc node của cây nhị phân
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val          # giá trị của node
        self.left = left        # con trái
        self.right = right      # con phải

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []  # nếu n = 0 thì không có cây nào

        memo = {}  # dictionary để ghi nhớ các lời giải con

        def generate_trees(start, end):
            # Nếu đã tính trước đó rồi thì trả về luôn
            if (start, end) in memo:
                return memo[(start, end)]

            trees = []  # lưu tất cả cây có thể tạo ra
            if start > end:
                # Nếu không còn số nào để tạo cây ⇒ trả về cây rỗng
                trees.append(None)
                return trees

            # Duyệt qua tất cả các giá trị có thể chọn làm root
            for root_val in range(start, end + 1):
                # Sinh tất cả cây con trái từ các số nhỏ hơn root_val
                left_trees = generate_trees(start, root_val - 1)
                # Sinh tất cả cây con phải từ các số lớn hơn root_val
                right_trees = generate_trees(root_val + 1, end)

                # Kết hợp tất cả cây con trái và phải để tạo cây hoàn chỉnh
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(root_val, left_tree, right_tree)
                        trees.append(root)

            # Lưu kết quả vào memo để lần sau không phải tính lại
            memo[(start, end)] = trees
            return trees

        # Sinh tất cả BST từ 1 đến n
        return generate_trees(1, n)
# ```

# ---

# 👉 Với `n = 3`, chương trình sẽ sinh ra **5 cây khác nhau** (đúng bằng số Catalan C3 = 5).

# Bạn có muốn mình viết thêm hàm **in ra danh sách cây theo kiểu level-order** (như LeetCode hiển thị) để dễ hình dung output không?
