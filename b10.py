# 101. Symmetric Tree
# Dưới đây là lời giải **đầy đủ và tối ưu** cho bài **LeetCode 101 – Symmetric Tree** viết bằng **Python** 👇

# ---

# ### ✅ Code đầy đủ:

# ```python
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Nếu cây rỗng → đối xứng
        if not root:
            return True

        # Gọi hàm kiểm tra 2 nhánh con có đối xứng không
        return self.isMirror(root.left, root.right)

    # Hàm kiểm tra hai cây con có là ảnh gương của nhau không
    def isMirror(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        # Cả hai cùng null → đối xứng
        if not t1 and not t2:
            return True
        # Một bên null, bên kia không → không đối xứng
        if not t1 or not t2:
            return False
        # Giá trị của 2 nút phải bằng nhau,
        # và nhánh trái của t1 phải đối xứng với nhánh phải của t2
        # nhánh phải của t1 đối xứng với nhánh trái của t2
        return (t1.val == t2.val and
                self.isMirror(t1.left, t2.right) and
                self.isMirror(t1.right, t2.left))
# ```

# ---

# ### 🧩 Giải thích thuật toán:

# * **Ý tưởng:**
#   Một cây là **đối xứng** nếu:

#   * Hai nhánh trái và phải là **ảnh gương của nhau**, tức là:

#     * Nút trái và phải có cùng giá trị
#     * Cây con trái của bên trái đối xứng với cây con phải của bên phải
#     * Cây con phải của bên trái đối xứng với cây con trái của bên phải

# ---

### 📘 Ví dụ:

# **Input:**

# ```
#        1
#      /   \
#     2     2
#    / \   / \
#   3  4  4  3
# ```

# **Output:**

# ```
# True
# ```

# **Giải thích:**
# Mỗi cặp đối xứng đều có cùng giá trị và cấu trúc giống hệt ảnh gương của nhau.

# ---

# ### ⏱️ Độ phức tạp:

# * **Thời gian:** `O(n)` – duyệt qua toàn bộ cây một lần.
# * **Không gian:** `O(h)` – do ngăn xếp đệ quy (h là chiều cao của cây).

# ---

# Bạn có muốn mình viết thêm **phiên bản không đệ quy (duyệt BFS/queue)** để so sánh tốc độ không?

# Rất hay 👍
# Cùng mình **giải thích chi tiết đề bài LeetCode 101 – Symmetric Tree** nhé 👇

# ---

# ## 🧩 **Đề bài: Symmetric Tree**

# Bạn được cho **gốc của một cây nhị phân (`root`)**.
# Hãy **kiểm tra xem cây đó có đối xứng (symmetric)** quanh **tâm dọc** của nó hay không.

# Nói cách khác:

# > Cây là đối xứng nếu **ảnh phản chiếu của nó qua trục giữa giống chính nó**.

# ---

# ### 🌳 Ví dụ 1

# **Input:**

# ```
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# ```

# **Output:**

# ```
# true
# ```

# **Giải thích:**
# Cây bên trái và cây bên phải là hình phản chiếu của nhau qua trục dọc đi qua nút gốc.

# ---

# ### 🌳 Ví dụ 2

# **Input:**

# ```
#     1
#    / \
#   2   2
#    \   \
#     3   3
# ```

# **Output:**

# ```
# false
# ```

# **Giải thích:**
# Hai cây con không đối xứng vì bên trái có `null` ở vị trí mà bên phải có `3`.

# ---

# ## 🔍 **Yêu cầu**

# Viết hàm:

# ```java
# public boolean isSymmetric(TreeNode root)
# ```

# Trả về `true` nếu cây đối xứng, ngược lại `false`.

# ---

# ## 💡 **Ý tưởng chính**

# ### Cách 1️⃣ – **Đệ quy (Recursive)**

# Hai cây con của `root` là đối xứng nếu:

# 1. `root.left.val == root.right.val`
# 2. `root.left.left` đối xứng với `root.right.right`
# 3. `root.left.right` đối xứng với `root.right.left`

# Tức là ta so sánh **cây trái của cây trái** với **cây phải của cây phải**,
# và **cây phải của cây trái** với **cây trái của cây phải**.

# ---

# ### ✅ Code minh họa (Java)

# ```java
# class Solution {
#     public boolean isSymmetric(TreeNode root) {
#         if (root == null) return true;
#         return isMirror(root.left, root.right);
#     }

#     private boolean isMirror(TreeNode t1, TreeNode t2) {
#         if (t1 == null && t2 == null) return true;   // cả hai rỗng → đối xứng
#         if (t1 == null || t2 == null) return false;  // một rỗng, một không → không đối xứng
#         return (t1.val == t2.val)
#             && isMirror(t1.left, t2.right)
#             && isMirror(t1.right, t2.left);
#     }
# }
# ```

# ---

# ### Cách 2️⃣ – **Duyệt theo hàng (Iterative)**

# Dùng **hàng đợi (queue)**:

# * Đưa `root.left` và `root.right` vào queue.
# * Mỗi lần lấy ra 2 nút để so sánh:

#   * Nếu cả hai đều null → bỏ qua.
#   * Nếu chỉ một null → false.
#   * Nếu giá trị khác nhau → false.
#   * Nếu giống nhau → thêm các cặp con theo thứ tự đối xứng:

#     * `(t1.left, t2.right)`
#     * `(t1.right, t2.left)`

# ---

# ### ✅ Code minh họa (Python)

# ```python
# from collections import deque

# class Solution:
#     def isSymmetric(self, root):
#         if not root:
#             return True
        
#         q = deque([(root.left, root.right)])
        
#         while q:
#             t1, t2 = q.popleft()
#             if not t1 and not t2:
#                 continue
#             if not t1 or not t2 or t1.val != t2.val:
#                 return False
#             q.append((t1.left, t2.right))
#             q.append((t1.right, t2.left))
        
#         return True
# ```

# ---

# ## 🧠 **Tóm tắt**

# | Phương pháp    | Cách tiếp cận                | Độ phức tạp | Ưu điểm                         |
# | -------------- | ---------------------------- | ----------- | ------------------------------- |
# | **Đệ quy**     | So sánh gương qua trái-phải  | O(n)        | Ngắn gọn, dễ hiểu               |
# | **Duyệt hàng** | So sánh từng cặp trong queue | O(n)        | Tránh tràn ngăn xếp với cây sâu |

# ---

# Nếu bạn muốn, mình có thể **vẽ hình minh họa** cách cây được so sánh theo cặp (left-left với right-right, left-right với right-left).
# Bạn có muốn xem hình minh họa đó không?

# // 101. Symmetric Tree

# import java.util.*;

# public class b10 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int n = sc.nextInt();

#         System.out.println("Nhập các giá trị node theo thứ tự level order:");
#         Integer[] arr = new Integer[n];
#         for (int i = 0; i < n; i++) {
#             int val = sc.nextInt();
#             arr[i] = val; // không có null ở đây để đơn giản
#         }

#         // Xây cây từ mảng level order
#         TreeNode root = buildTree(arr);

#         // Kiểm tra đối xứng

#         boolean result = isSymmetric(root);

#         System.out.println(result ? "Cây đối xứng" : "Cây không đối xứng");
#     }

#     // Xây cây nhị phân từ mảng level order
#     public static TreeNode buildTree(Integer[] arr) {
#         if (arr.length == 0 || arr[0] == null)
#             return null;

#         TreeNode root = new TreeNode(arr[0]);
#         Queue<TreeNode> q = new LinkedList<>();
#         q.add(root);
#         int i = 1;

#         while (!q.isEmpty() && i < arr.length) {
#             TreeNode node = q.poll();

#             // thêm nhánh trái
#             if (i < arr.length && arr[i] != null) {
#                 node.left = new TreeNode(arr[i]);
#                 q.add(node.left);
#             }
#             i++;

#             // thêm nhánh phải
#             if (i < arr.length && arr[i] != null) {
#                 node.right = new TreeNode(arr[i]);
#                 q.add(node.right);
#             }
#             i++;
#         }
#         return root;
#     }

#     static class TreeNode {
#         int val;
#         TreeNode left, right;

#         TreeNode(int val) {
#             this.val = val;
#         }
#     }

#     public static boolean isSymmetric(TreeNode root) {
#         if (root == null)
#             return true;
#         return isMirror(root.left, root.right);
#     }

#     // Hàm kiểm tra 2 nhánh có là ảnh gương của nhau không
#     public static boolean isMirror(TreeNode t1, TreeNode t2) {
#         if (t1 == null && t2 == null)
#             return true; // cả 2 đều rỗng → đối xứng
#         if (t1 == null || t2 == null)
#             return false; // 1 bên null → không đối xứng

#         // kiểm tra giá trị và 2 cặp nhánh con
#         return (t1.val == t2.val)
#                 && isMirror(t1.left, t2.right)
#                 && isMirror(t1.right, t2.left);
#     }
# }

# // Tất nhiên 👇 — mình sẽ **giải thích chi tiết thuật toán “Symmetric Tree”**
# // (Bài LeetCode 101) kèm ví dụ minh họa rõ ràng.

# // ---

# // ## 🧩 Đề bài

# // Cho gốc của một **cây nhị phân**, hãy kiểm tra xem **cây có đối xứng
# // (symmetrical)** quanh trục dọc đi qua gốc hay không.

# // Nói cách khác, cây đó có phải là **ảnh gương của chính nó** không?

# // ---

# // ## 💡 Ý tưởng chính

# // Cây đối xứng khi:

# // * Hai nhánh trái và phải của gốc là **ảnh gương** của nhau.
# // * Nghĩa là:

# // * Giá trị nút trái và phải **bằng nhau**
# // * Nhánh **trái của cây bên trái** phải đối xứng với **nhánh phải của cây bên
# // phải**,
# // * và ngược lại.

# // ---

# // ## 🔁 Thuật toán đệ quy

# // Ta viết một hàm phụ `isMirror(TreeNode t1, TreeNode t2)` để kiểm tra xem hai
# // cây có là ảnh gương của nhau hay không.

# // ### Bước kiểm tra:

# // 1. **Cả hai cùng null** → ✅ Đối xứng
# // (vì cả hai đều không có gì)

# // 2. **Một trong hai null** → ❌ Không đối xứng
# // (một bên có nhánh, bên kia không có)

# // 3. **Giá trị không bằng nhau** → ❌ Không đối xứng

# // 4. Nếu các điều kiện trên đều qua, ta tiếp tục kiểm tra **2 cặp con tương
# // ứng**:

# // * `t1.left` ↔ `t2.right`
# // * `t1.right` ↔ `t2.left`

# // Nếu tất cả các cặp đều đúng → cây đối xứng.

# // ---

# // ## 🧠 Độ phức tạp

# // * **Thời gian:** `O(n)` — ta duyệt tất cả các nút trong cây đúng một lần.
# // * **Không gian:** `O(h)` — do đệ quy (h là chiều cao cây).

# // ---

# // ## 🧮 Ví dụ minh họa

# // ### Input:

# // ```
# // 1
# // / \
# // 2 2
# // / \ / \
# // 3 4 4 3
# // ```

# // ### So sánh từng cặp:

# // 1. `1 ↔ 1` ✅
# // 2. `2(left) ↔ 2(right)` ✅
# // 3. So sánh:

# // * `3 ↔ 3` ✅
# // * `4 ↔ 4` ✅

# // Mọi cặp tương ứng đều bằng nhau → **cây đối xứng** ✅

# // ---

# // ### Trường hợp **không đối xứng:**

# // ```
# // 1
# // / \
# // 2 2
# // \ \
# // 3 3
# // ```

# // So sánh:

# // * `1 ↔ 1` ✅
# // * `2(left) ↔ 2(right)` ✅
# // * Nhưng:

# // * `left.left = null`
# // * `right.right = 3`
# // → ❌ Không đối xứng

# // ---

# // ## ✅ Tóm tắt

# // | Điều kiện kiểm tra | Kết luận | | |
# // | -------------------------- |
# // ---------------------------------------------------- | ----------- |
# // -------------- |
# // | `t1 == null && t2 == null` | Đối xứng | | |
# // | `t1 == null | | t2 == null` | Không đối xứng |
# // | `t1.val != t2.val` | Không đối xứng | | |
# // | Còn lại | So sánh `t1.left ↔ t2.right` và `t1.right ↔ t2.left` | | |

# // ---

# // Bạn có muốn mình vẽ **sơ đồ minh họa dạng ảnh gương** để trực quan hóa quá
# // trình đệ quy không?
