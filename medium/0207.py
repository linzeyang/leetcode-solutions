"""207. Course Schedule"""

from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping: dict[int, list[int]] = {}
        in_degree = [0] * numCourses

        for course_a, course_b in prerequisites:
            if course_a not in mapping:
                mapping[course_a] = [course_b]
            else:
                mapping[course_a].append(course_b)
            in_degree[course_b] += 1

        queue = deque()

        for idx, degree in enumerate(in_degree):
            if not degree:
                queue.append(idx)

        while queue:
            course = queue.popleft()

            if course not in mapping:
                continue

            for parent_course in mapping[course]:
                in_degree[parent_course] -= 1

                if not in_degree[parent_course]:
                    queue.append(parent_course)

        return not sum(in_degree)
