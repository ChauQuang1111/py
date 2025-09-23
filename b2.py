# 70. Climbing Stairs
# Ok, mình sẽ giải thích chi tiết thuật toán và thêm **chú thích từng dòng code** cho bạn nhé.

# ---

# ### 💡 Ý tưởng thuật toán

# * Bài toán này chính là biến thể của **dãy Fibonacci**.
# * Gọi `dp[i]` là **số cách leo lên bậc thứ i**.
# * Khi muốn leo đến **bậc i**, ta có 2 cách:

#   1. Leo 1 bước từ bậc `i-1` → `dp[i-1]` cách.
#   2. Leo 2 bước từ bậc `i-2` → `dp[i-2]` cách.
# * Vậy:

#   ```
#   dp[i] = dp[i-1] + dp[i-2]
#   ```
# * Trường hợp cơ sở:

#   * `dp[1] = 1` (chỉ có 1 cách: bước 1 lần).
#   * `dp[2] = 2` (có 2 cách: 1+1 hoặc 2).

# ---

# ### 📝 Code với chú thích

# ```python
class Solution:
    def climbStairs(self, n: int) -> int:
        # Nếu n <= 2 thì số cách leo chính là n (1 bậc có 1 cách, 2 bậc có 2 cách)
        if n <= 2:
            return n
        
        # Tạo mảng dp để lưu số cách leo đến mỗi bậc
        dp = [0] * (n + 1)
        
        # Khởi tạo cơ sở
        dp[1], dp[2] = 1, 2
        
        # Dùng công thức quy hoạch động
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]  # Muốn đến bậc i thì đi từ i-1 hoặc i-2
        
        # Trả về kết quả là số cách leo đến bậc n
        return dp[n]
# ```

# ---

# ### 🔎 Ví dụ chạy với `n = 5`

# * `dp[1] = 1`
# * `dp[2] = 2`
# * `dp[3] = dp[2] + dp[1] = 2 + 1 = 3`
# * `dp[4] = dp[3] + dp[2] = 3 + 2 = 5`
# * `dp[5] = dp[4] + dp[3] = 5 + 3 = 8`

# 👉 Kết quả: **8 cách** leo lên bậc thứ 5.

# ---

# Bạn có muốn mình viết thêm **phiên bản tối ưu O(1) memory** (chỉ dùng 2 biến, không cần mảng `dp`) không?
