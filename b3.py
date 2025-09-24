# Word Search
# Dưới đây là phiên bản Python của thuật toán Word Search mà bạn gửi, **thêm chú thích chi tiết** và giải thích thuật toán:

# ```python
from typing import List
from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        # B1: Đếm số lần xuất hiện của từng ký tự trên board
        count = Counter(sum(board, []))  # sum(board, []) flatten 2D -> 1D
        for c, countWord in Counter(word).items():
            # Nếu số lần ký tự c trên board < số lần cần trong word → chắc chắn không tìm được
            if count[c] < countWord:
                return False

        # B2: "Heuristic" – nếu ký tự đầu ít xuất hiện hơn ký tự cuối, ta đảo word để giảm DFS
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        # B3: DFS + backtracking
        def dfs(r, c, i):
            # i là chỉ số ký tự đang tìm trong word
            if i == len(word):
                return True  # đã tìm hết word

            # Nếu ra ngoài board, hoặc ký tự không khớp, hoặc ô đã đi qua ('#')
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False

            # Đánh dấu ô là đã đi để tránh đi lại
            board[r][c] = '#'

            # Thử 4 hướng: xuống, lên, phải, trái
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            # Phục hồi ô sau khi thử xong (backtracking)
            board[r][c] = word[i]

            return res

        # B4: Thử DFS từ mọi ô trên board
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
# ```

# ---

# ### **Giải thích thuật toán**

# 1. **Kiểm tra khả năng tồn tại trước khi DFS:**

#    * Dùng `Counter` để đếm tần suất ký tự trên board.
#    * Nếu board không đủ ký tự cần cho `word`, return `False` ngay.

# 2. **Heuristic đảo word:**

#    * Nếu ký tự đầu ít xuất hiện hơn ký tự cuối, ta đảo word để DFS bắt đầu từ ký tự hiếm hơn → giảm số lượng nhánh cần duyệt.

# 3. **DFS + backtracking:**

#    * `dfs(r, c, i)` tìm chữ thứ `i` của word từ ô `(r,c)`.
#    * Base case: nếu `i == len(word)` → đã tìm xong → return `True`.
#    * Nếu ô ra ngoài board, ký tự không khớp, hoặc ô đã đi qua → return `False`.
#    * Đánh dấu ô đã đi bằng `'#'`.
#    * Thử 4 hướng: xuống, lên, phải, trái.
#    * Phục hồi ô sau khi thử xong (backtracking).

# 4. **DFS từ mọi ô:**

#    * Duyệt toàn bộ board để tìm điểm bắt đầu.
#    * Nếu DFS từ bất kỳ ô nào return `True` → word tồn tại trên board.
#    * Nếu hết board mà không tìm thấy → return `False`.

# ---

# Nếu muốn, mình có thể viết luôn **phiên bản Java tương đương**, dùng `Scanner` nhập board và word, để bạn chạy trực tiếp.

# Bạn có muốn mình làm không?

# Ok, mình giải thích rõ đề **Word Search** (LeetCode 79) cho bạn nhé:

# ---

# ### Đề bài

# Bạn được cho một **ma trận ký tự** `board` (2D grid) và một **chuỗi từ cần tìm** `word`.

# Hãy kiểm tra xem có thể tìm thấy `word` trong `board` hay không.

# **Quy tắc di chuyển:**

# * Bắt đầu từ bất kỳ ô nào trong `board`.
# * Tại mỗi bước, có thể đi **lên, xuống, trái, phải** (4 hướng).
# * **Không được dùng lại một ô** đã được chọn trong cùng một lần tìm.

# 👉 Nếu tìm được thì trả về `true`, ngược lại trả về `false`.

# ---

# ### Ví dụ 1

# ```
# board = [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED"
# ```

# Lời giải:

# * Bắt đầu ở `board[0][0] = 'A'`.
# * Đi → `B`, → `C`, → `C`, ↓ `E`, ↓ `D`.
# * Ghép lại được `"ABCCED"` → **True**.

# ---

# ### Ví dụ 2

# ```
# board = [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "SEE"
# ```

# Lời giải:

# * Bắt đầu ở `board[1][3] = 'S'`.
# * Xuống → `E`, xuống → `E`.
# * Ghép lại `"SEE"` → **True**.

# ---

# ### Ví dụ 3

# ```
# board = [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCB"
# ```

# Lời giải:

# * Không thể tìm ra `"ABCB"` mà không dùng lại một ô.
# * Kết quả → **False**.

# ---

# ### Ý tưởng giải thuật

# Đây là một bài **Backtracking (DFS trên grid)**:

# 1. Duyệt từng ô trong `board`.
# 2. Nếu ô đó = ký tự đầu tiên của `word` → bắt đầu tìm kiếm DFS.
# 3. Trong DFS:

#    * Kiểm tra nếu ký tự hiện tại khớp.
#    * Đánh dấu ô này là **đã dùng** (thường tạm đổi thành ký tự đặc biệt, ví dụ `'#'`).
#    * Gọi đệ quy tìm ký tự tiếp theo theo 4 hướng.
#    * Quay lui (backtrack): khôi phục ký tự cũ để các lần tìm khác không bị ảnh hưởng.
# 4. Nếu tại bất kỳ điểm nào tìm được đủ các ký tự trong `word` → trả về `true`.
# 5. Nếu duyệt hết mà không tìm được → trả về `false`.

# ---

# Bạn có muốn mình viết code minh họa luôn (Python hoặc Java) không?
