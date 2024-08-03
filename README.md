# Selection Sort Algorithm
**Introduction**

Selection Sort is a simple comparison-based sorting algorithm. It works by repeatedly finding the minimum element from the unsorted part of the list and swapping it with the first unsorted element. This process is repeated until the entire list is sorted.

**Time Complexity**
* Best Case: O(n^2) - The list is already sorted.
* Average Case: O(n^2) - The list is in random order.
* Worst Case: O(n^2) - The list is in reverse order.
Here, n is the number of elements in the list.

**Explanation**

1) Function Definition:

* The selectionSort function takes one parameter: arr (a list of integers to be sorted).

2) Outer Loop:

* The outer loop runs from i = 0 to n-1 (where n is the length of the list). This loop iterates through the entire list.

3) Finding the Minimum:

* The min_index variable holds the index of the minimum element found in the unsorted part of the list.
* The inner loop runs from j = i + 1 to n-1 to find the minimum element in the unsorted part of the list.

4) Swapping Elements:

* If a smaller element is found, min_index is updated.
* After finding the minimum element, it is swapped with the first unsorted element.

5) Return Sorted Array:

* After the loops complete, the sorted list arr is returned.

6) User Input:

* The user is prompted to enter the elements of the array as a space-separated string. This input is converted to a list of integers using map and list.

7) Print Before Sorting:

* The original array is printed before sorting.

8) Function Call and Result:

* The selectionSort function is called with the user-provided array.
* The sorted array is printed to the console.

**Usage**

* Run the code.
* Enter the elements of the array when prompted. Separate each element with a space.
* The program will output the original array before sorting and the sorted array after applying selection sort.
