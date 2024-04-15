class Solution1:
    def makeGood(self, s):
        if len(s) == 1:
            return s
        i = 0
        while i < len(s) - 1:
            if ord(s[i]) + 32 == ord(s[i + 1]) or ord(s[i + 1]) + 32 == ord(s[i]):
                s = s[:i] + s[i + 2:]
                i = 0
            else:
                i += 1 
        return s

class Solution2:
    def makeGood(self, s):
        stack = []
        for i in range(len(s)):
            if (
                stack and
                stack[-1] != s[i] and
                stack[-1].lower() == s[i].lower()
            ):
                stack.pop()
            else:
                stack.append(s[i])

        return "".join(stack)
  
class Solution3:
    def containsNearbyDuplicate(self, nums, k):
        window = set()
        left = 0
        for right in range(len(nums)):
            if right - left > k:
                window.remove(nums[left])
                left += 1
            if nums[right] in window:
                return True
            else:
                window.add(nums[right])
        return False
    
class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(100)
root.left = TreeNode(60)
root.right = TreeNode(110)
root.left.left = TreeNode(50)
root.left.right = TreeNode(61)
root.left.right.left = TreeNode(40)
root.left.right.right = TreeNode(62)

class Solution5:
    def isValidBST(self, root):
        def valid(node, left, right):
            if not node:
                return True
            if not(node.val < right and node.val > left):
                return False
            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))
        return valid(root, float("-inf"), float("inf"))
      
class Solution6:
    def merge(self, nums1, m, nums2, n):
        if n == 0:
            return  nums1
        pointer = m + n - 1
        while n != 0:
            if m != 0 and nums1[m - 1] > nums2[n - 1]:
                nums1[pointer], nums1[m - 1] = nums1[m - 1], nums1[pointer]
                m -= 1 
            else:
                nums1[pointer], nums2[n - 1] = nums2[n - 1], nums1[pointer]
                n -= 1
            pointer -= 1
        return nums1
    
class LinkedListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(6)
head.next.next.next = LinkedListNode(3)
head.next.next.next.next = LinkedListNode(4)
head.next.next.next.next.next = LinkedListNode(5)
head.next.next.next.next.next.next = LinkedListNode(6)

head = LinkedListNode(7)
head.next = LinkedListNode(7)
head.next.next = LinkedListNode(7)
head.next.next.next = LinkedListNode(7)

class Solution7:
    def removeElements(self, head, val):
        prev = None
        cur = head
        while cur:
            if cur.val == val:
                if not prev:
                    head = cur.next
                else:
                    prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

        cur = head
        while cur:
            print(cur.val)
            cur = cur.next
        return head
    
class Solution:
    def maxProfit(self, prices):
        if len(prices) == 1:
            return 0
        left = 0
        profit = 0
        for right in range(1, len(prices)):
            profit = max(profit, prices[right] - prices[left])
            if prices[right] < prices[left]:
                left = right
        return profit
    
class DLinkedListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head, self.tail = DLinkedListNode(0, 0), DLinkedListNode(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def insert(self, node):
        prev = self.tail.prev
        prev.next = self.tail.prev = node
        node.next, node.prev = self.tail, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = DLinkedListNode(key, value)
        self.insert(self.cache[key])
        if self.capacity < len(self.cache):
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]

cache = LRUCache(2)