"""797. All Paths From Source to Target"""

from typing import List


class Solution:
    """My own solution"""

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        return self.find_paths(graph, index=0, dest=len(graph) - 1)

    def find_paths(
        self, graph: list[list[int]], index: int, dest: int
    ) -> list[list[int]]:
        out: list[list[int]] = []

        for node in graph[index]:
            if node == dest:
                out.append([index, node])
                continue

            for res in self.find_paths(graph, node, dest):
                out.append([index] + res)

        return out


class Solution2:
    """Labuladong's solution"""

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res: list[list[int]] = []
        path: list[int] = []
        self.traverse(graph, 0, path)

        return self.res

    def traverse(self, graph: List[List[int]], s: int, path: List[int]) -> None:
        """图的遍历框架"""

        path.append(s)  # 添加节点 s 到路径

        n = len(graph)

        if s == n - 1:  # 到达终点
            self.res.append(path[:])
            path.pop()

            return

        for v in graph[s]:  # 递归每个相邻节点
            self.traverse(graph, v, path)

        path.pop()  # 从路径移出节点 s


def test_solution_1():
    assert Solution().allPathsSourceTarget(
        graph=[[4, 3, 1], [3, 2, 4], [3], [4], []]
    ) == [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]


def test_solution_2():
    assert Solution2().allPathsSourceTarget(
        graph=[[4, 3, 1], [3, 2, 4], [3], [4], []]
    ) == [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
