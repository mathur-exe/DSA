def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    for i, row in enumerate(matrix):
        left, right = 0, len(row)-1
        while left <= right:
            mid = left + (right - left) // 2        
            if row[mid] == target: return True
            elif row[mid] < target: left = mid + 1
            else: right = mid - 1
    return False