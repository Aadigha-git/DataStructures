package gfg.basic;

import java.util.Scanner;

public class LCM {
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

		// Find the LCM of the elements
		int max = arr[0];
		for (int i = 1; i < n; i++) {
			if (arr[i] > max) {
				max = arr[i];
			}
		}
		int lcm = max;
		while (true) {
			boolean isLCM = true;
			for (int i = 0; i < n; i++) {
				if (lcm % arr[i] != 0) {
					isLCM = false;
					break;
				}
			}
			if (isLCM) {
				break;
			} else {
				lcm += max;
			}
		}

		// Print the result
		System.out.println("The LCM is: " + lcm);
		scn.close();
	}
}
