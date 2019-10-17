# 399. Evaluate Division
# https://leetcode.com/problems/evaluate-division/description/


# Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

# Example:
# Given a / b = 2.0, b / c = 3.0.
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].

# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.


"""
floyd-warshall

1. setup graph
	need to read all the nodes first
	create a nodes set: for easy edge case checking
	or use a dict of dict
	create a 2D matrix: need a node-name to index mapping

2. floyd-warshall all the possible edges
3. allow queries
"""


equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

from collections import defaultdict
class Solution:
	def calcEquation(self, equations, values , queries ):
		graph = self.setup(equations, values)
		graph = self.floyd_warshall(graph)
		ans = [self.query(graph, From, to) for (From,to) in queries]
		return ans

	def setup(self, equations, values):
		graph = defaultdict(defaultdict) 
		# key,value = <node, adjacent list as a dict:<toNode, dist>>
		for (From, to), value in zip(equations, values):
			graph[From][to] = value
			graph[to][From] = 1.0 / value 
			graph[From][From] = 1
			graph[to][to] = 1
		return graph

	def floyd_warshall(self, graph):
		for middle in graph.keys():
			for From in graph.keys():
				for to in graph.keys():
					if middle in graph[From] and to in graph[middle]:
						graph[From][to] = graph[From][middle] * graph[middle][to]
		return graph
	def query(self, graph, From, to):
		return graph[From][to] if (From in graph and to in graph[From]) else -1

s = Solution()
print(s.calcEquation(equations, values, queries))

