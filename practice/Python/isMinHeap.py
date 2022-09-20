# Iterative function to check if given list represents a Min-Heap or not
def checkMinHeap(A):

	# check for all internal nodes that their left child and
	# right child (if present) holds min-heap property or not

	# start with index 0 (root of the heap)
	for i in range((len(A) - 2) // 2 + 1):
		if A[i] > A[2 * i + 1] or (2 * i + 2 != len(A) and A[i] > A[2 * i + 2]):
			return False

	return True


if __name__ == '__main__':

	A = []
	A = [int(item) for item in input("enter list (comma seperated): ").split(',')]

	if checkMinHeap(A):
		print("Given list is a min heap")
	else:
		print("Given list is not a min heap")
