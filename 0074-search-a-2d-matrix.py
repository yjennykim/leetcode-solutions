class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarySearch(arr):
            l, r = 0, len(arr)-1
            while l <= r:
                mid = (l+r) // 2
                if arr[mid] > target:
                    # too high
                    r = mid - 1
                elif arr[mid] < target:
                    # too low
                    l = mid + 1
                else:
                    return mid
            
            # return R because we want the last row less than target 
            return r
        
        cols = [row[0] for row in matrix]
        print(f"searching cols={cols}")
        rowIndex = binarySearch(cols)
        print(f"rowIndex={rowIndex}")
        colIndex = binarySearch(matrix[rowIndex])
        print(f"colIndex={colIndex}")
        
        return matrix[rowIndex][colIndex] == target
        
