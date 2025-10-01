# #  Range Sum Query Mutable
# Ok, mình sẽ giải thích thuật toán chi tiết và chèn chú thích trực tiếp vào code Python của bạn nhé.

# ---

# ### 📝 Giải thích thuật toán

# Bài toán **Range Sum Query - Mutable (307)** yêu cầu:

# * Cập nhật giá trị tại một index (`update`).
# * Tính tổng đoạn từ `left` đến `right` (`sumRange`).

# Nếu dùng cách đơn giản (brute force):

# * `update`: O(1) ✅
# * `sumRange`: O(n) ❌ (quá chậm khi có nhiều truy vấn)

# 👉 Giải pháp tối ưu: dùng **Fenwick Tree (Binary Indexed Tree - BIT)** để:

# * Cập nhật (`update`): O(log n)
# * Tính tổng (`sumRange`): O(log n)

# Fenwick Tree hoạt động dựa trên việc lưu trữ **một phần tổng** ở mỗi node, nhờ đó có thể:

# * Nhanh chóng cập nhật khi một phần tử thay đổi.
# * Nhanh chóng lấy tổng từ 0 → index bất kỳ.

# ---

# ### ✅ Code Python có chú thích

# ```python
from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        # Số lượng phần tử
        self.n = len(nums)
        # Sao chép mảng gốc để lưu giá trị hiện tại
        self.nums = nums[:]
        # Khởi tạo Fenwick Tree (bit), dùng index 1-based
        self.bit = [0] * (self.n + 1)

        # Xây dựng Fenwick Tree ban đầu bằng cách cộng từng phần tử vào
        for i, num in enumerate(nums):
            self._add(i, num)

    def update(self, index: int, val: int) -> None:
        """
        Cập nhật nums[index] = val
        Ta cần tính delta = val - nums[index] 
        rồi cập nhật vào Fenwick Tree
        """
        delta = val - self.nums[index]   # thay đổi giá trị
        self.nums[index] = val           # cập nhật mảng gốc
        self._add(index, delta)          # cập nhật Fenwick Tree

    def sumRange(self, left: int, right: int) -> int:
        """
        Tính tổng đoạn [left, right]
        Dùng công thức: prefix(right) - prefix(left-1)
        """
        return self._prefix_sum(right) - self._prefix_sum(left - 1)

    # --------- helper functions (Fenwick Tree) ---------
    def _add(self, index: int, delta: int):
        """
        Thêm delta vào nums[index]
        Đồng thời cập nhật các node liên quan trong Fenwick Tree
        """
        index += 1  # chuyển sang 1-based
        while index <= self.n:
            self.bit[index] += delta
            # đi tới node cha (cộng thêm lowest set bit)
            index += index & -index

    def _prefix_sum(self, index: int) -> int:
        """
        Tính tổng từ 0 -> index
        Di chuyển ngược trên Fenwick Tree bằng cách
        trừ đi lowest set bit
        """
        if index < 0:
            return 0
        index += 1  # chuyển sang 1-based
        res = 0
        while index > 0:
            res += self.bit[index]
            # đi tới node cha (trừ lowest set bit)
            index -= index & -index
        return res


# ---

# ### 🔍 Ví dụ chạy thử

# ```python
# arr = NumArray([1, 3, 5])   # nums = [1,3,5]
# print(arr.sumRange(0, 2))   # 1+3+5 = 9
# arr.update(1, 2)            # nums = [1,2,5]
# print(arr.sumRange(0, 2))   # 1+2+5 = 8
# ```

# ---

# ### 🚀 Tóm tắt

# * **Fenwick Tree** chia nhỏ đoạn tổng để có thể:

#   * Cập nhật nhanh bằng cách thêm `delta` vào các node cha.
#   * Lấy tổng nhanh bằng cách đi ngược lên các node cha.
# * Tất cả thao tác đều O(log n), tối ưu hơn nhiều so với O(n).

# ---

# 👉 Bạn có muốn mình vẽ thêm **sơ đồ Fenwick Tree hoạt động** để dễ hình dung cách update và query không?

# ---

# ## 📌 Đề bài

# Bạn được cho một **mảng số nguyên `nums`**, và cần hỗ trợ 2 loại thao tác:

# 1. **update(index, val)**

#    * Cập nhật giá trị của phần tử tại vị trí `index` thành `val`.

# 2. **sumRange(left, right)**

#    * Trả về tổng các phần tử trong khoảng `[left, right]`.

# 👉 Khác với bài **303. Range Sum Query – Immutable** (không cho update), ở bài này mảng có thể thay đổi nên phải có cấu trúc dữ liệu hiệu quả để hỗ trợ cả update lẫn sum.

# ---

# ## 📌 Ví dụ

# Input:

# ```
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1,3,5]], [0,2], [1,2], [0,2]]
# ```

# Giải thích:

# * `NumArray([1,3,5])` → khởi tạo mảng `[1,3,5]`.
# * `sumRange(0,2)` → 1+3+5 = 9.
# * `update(1,2)` → mảng thành `[1,2,5]`.
# * `sumRange(0,2)` → 1+2+5 = 8.

# Output:

# ```
# [null, 9, null, 8]
# ```

# ---

# ## 📌 Ràng buộc

# * `1 <= nums.length <= 3 * 10^4`
# * `-100 <= nums[i] <= 100`
# * `0 <= index < nums.length`
# * Có thể có **10^4 thao tác** update hoặc sumRange.

# 👉 Nếu dùng cách cộng dồn đơn giản (mỗi lần sumRange duyệt từ `left → right`) → O(n) cho mỗi query → quá chậm.

# ---

# ## 📌 Hướng tiếp cận

# Ta cần cấu trúc dữ liệu hỗ trợ:

# * **Update 1 phần tử** nhanh.
# * **Tính tổng trên đoạn [L, R]** nhanh.

# Các cách:

# 1. **Fenwick Tree (Binary Indexed Tree – BIT)**

#    * Update: O(log n).
#    * Query prefix sum: O(log n).
#    * sumRange(L, R) = prefix(R) - prefix(L-1).

# 2. **Segment Tree**

#    * Update: O(log n).
#    * Query sumRange: O(log n).

# 👉 Cả 2 đều phù hợp. BIT cài ngắn gọn hơn, Segment Tree dễ mở rộng cho các loại query khác.

# ---

# 📌 Tóm lại:

# * Đây là bài toán điển hình về **cấu trúc dữ liệu cho Range Query + Update**.
# * Giải bằng **Fenwick Tree hoặc Segment Tree** để đạt hiệu quả.

# ---

# Bạn muốn mình viết code **Fenwick Tree (ngắn gọn)** hay **Segment Tree (dễ hiểu hơn)** cho bài này?
