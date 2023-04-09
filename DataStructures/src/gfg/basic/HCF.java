package gfg.basic;

import java.util.Scanner;

public class HCF {

	// Function to find the HCF of two numbers using the Euclidean algorithm
	public static int findHCF(int a, int b) {
		if (b == 0) {
			return a;
		} else {
			return findHCF(b, a % b);
		}
	}

	public static void main(String[] args) {
		Scanner scn = new Scanner(System.in);

		// Read in the number of elements
		System.out.print("Enter the number of elements: ");
		int n = scn.nextInt();

		// Read in the elements
		int[] arr = new int[n];
		System.out.print("Enter the elements: ");
		for (int i = 0; i < n; i++) {
			arr[i] = scn.nextInt();
		}

		// Find the HCF of the elements
		int hcf = arr[0];
		for (int i = 1; i < n; i++) {
			hcf = findHCF(hcf, arr[i]);
		}

		// Print the result
		System.out.println("The HCF is: " + hcf);
		scn.close();
	}

}
