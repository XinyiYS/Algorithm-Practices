# 839. Similar String Groups
# https://leetcode.com/problems/similar-string-groups/

# Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y.

# For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

# Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

# We are given a list A of strings.  Every string in A is an anagram of every other string in A.  How many groups are there?

# Example 1:

# Input: ["tars","rats","arts","star"]
# Output: 2
# Note:

# A.length <= 2000
# A[i].length <= 1000
# A.length * A[i].length <= 20000
# All words in A consist of lowercase letters only.
# All words in A have the same length and are anagrams of each other.
# The judging time limit has been increased for this question.

from collections import defaultdict
class UnionFind:
	def __init__(self, A):
		self.size = [1 for i in A]
		self.numComponent = len(A)
		self.root = list(range(len(A)))

	def isConnected(self, p, q):
		return self.find(p)==self.find(q)

	def find(self, p):
		root = p
		while root != self.root[root]:
			root = self.root[root]

		while (p!= root):
			next = self.root[p]
			self.root[p] = root
			p = next
		return root

	def union(self, p, q):
		P, Q = self.find(p), self.find(q)

		if P == Q : return
		if self.size[P] > self.size[Q]:
			self.root[Q] = P
			self.size[P] += self.size[Q]
		else:
			self.root[P] = Q
			self.size[Q] += self.size[P]
		self.numComponent -= 1
		return

class Solution:
	def numSimilarGroups(self, A) -> int:
		#use union-find to keep track of number of connected components, to perform union
		#iterate the array, and for each element, use dfs to search for an existing component
		if len(A) >= 2 * len(A[0]):
			return self.solve_long_A(A)
		else:
			return self.solve_long_words(A)

	def solve_long_A(self, A):
		self.uf = UnionFind(A)
		self.word_dict = defaultdict(list)
		for i, word in enumerate(A): self.word_dict[word].append(i)
		
		for i, word in enumerate(A):
			visited = set()
			self.dfs(i, word, visited)
		return self.uf.numComponent

	def dfs(self, index, word, visited):
		if index in visited: return
		visited.add(index)
		for i in range(len(word) - 1):
			for j in range(i+1, len(word)):
				if word[i] == word[j]: continue
				chars = [c for c in word]
				chars[i], chars[j] = chars[j], chars[i]
				newWord = "".join(chars)
				if newWord in self.word_dict:
					for neighbor_index in self.word_dict[newWord]:
						self.uf.union(neighbor_index, index)
						self.dfs(neighbor_index, newWord, visited)
		
		visited.remove(index)
		return

	def solve_long_words(self, A):
		uf = UnionFind(A)
		for i in range(len(A)-1):
			for j in range(i+1, len(A)):
				if self.isSimilar(A[i], A[j]):
					uf.union(i, j)
		return uf.numComponent

	def isSimilar(self, word1, word2):
		count = 0
		for c1, c2 in zip(word1, word2):
			if c1 != c2:
				count += 1
				if count > 2: return False
		return count == 2 or count == 0

s = Solution()
a = s.numSimilarGroups(["tars","rats","arts","arts","arts","arts","arts","arts","arts","arts"])
print(a)