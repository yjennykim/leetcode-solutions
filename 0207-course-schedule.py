class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [course, prereq]
        # Build adjacency list. Prerequisite --> Set of courses 
        # Build preqreq counter. Course --> Count
        adjacency_list = {}
        prereq_counter = {}
        for i in range(numCourses):
            if i not in adjacency_list:
                adjacency_list[i] = set()
            if i not in prereq_counter:
                prereq_counter[i] = 0

        for course, prereq in prerequisites:
            adjacency_list[prereq].add(course)
            prereq_counter[course] += 1
        
        # Take class with no incoming edges (no prereqs)
        queue = collections.deque()
        for course in prereq_counter:
            if prereq_counter[course] == 0:
                queue.append(course)

        while len(queue) > 0:
            course = queue.popleft()
            

            for nxt in adjacency_list[course]:
                prereq_counter[nxt] -= 1. # Remove this class from prereq requirements
                if prereq_counter[nxt] == 0:
                    queue.append(nxt)
            del adjacency_list[course]  # This class has been taken
        
        return len(adjacency_list) == 0

