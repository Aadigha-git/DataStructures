package sortingTechniques;

import java.util.Arrays;
import java.util.Scanner;

public class RadixSort {

	void countingSort(int array[], int size, int place) {
		int[] output = new int[size + 1];
		int max = array[0];
		for (int i = 1; i < size; i++) {
			if (array[i] > max)
				max = array[i];
		}
		int[] count = new int[max + 1];

		for (int i = 0; i < max; ++i)
			count[i] = 0;

		// Calculate count of elements
		for (int i = 0; i < size; i++)
			count[(array[i] / place) % 10]++;

		// Calculate cumulative count
		for (int i = 1; i < 10; i++)
			count[i] += count[i - 1];

		// Place the elements in sorted order
		for (int i = size - 1; i >= 0; i--) {
			output[count[(array[i] / place) % 10] - 1] = array[i];
			count[(array[i] / place) % 10]--;
		}

		for (int i = 0; i < size; i++)
			array[i] = output[i];
	}

	int getMax(int array[], int n) {
		int max = array[0];
		for (int i = 1; i < n; i++)
			if (array[i] > max)
				max = array[i];
		return max;
	}

	void radixSort(int array[], int size) {
		int max = getMax(array, size);

		for (int place = 1; max / place > 0; place *= 10)
			countingSort(array, size, place);
	}

	public static void main(String args[]) {
		Scanner scn = new Scanner(System.in);
		System.out.println("Enter the elemnts to be sorted. ");

		int n = scn.nextInt();
		int[] data = new int[n];

		System.out.println("Enter the elemnts to be sorted.");
		for (int i = 0; i < n; i++) {
			data[i] = scn.nextInt();
		}

		int size = data.length;
		RadixSort rs = new RadixSort();
		rs.radixSort(data, size);
		System.out.println("Sorted Array in Ascending Order: ");
		System.out.println(Arrays.toString(data));

		scn.close();
	}
}