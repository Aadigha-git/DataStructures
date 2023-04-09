package gfg.basic;

import java.util.Scanner;

class ThreeTernary {

	// Function to find the biggest of three numbers using ternary operator
	static int biggestOfThree(int x, int y, int z) {
		return z > (x > y ? x : y) ? z : ((x > y) ? x : y);
	}

	public static void main(String[] args) {

		int a, b, c;
		int max;

		Scanner scn = new Scanner(System.in);
		System.out.println("Enter the three numbers to be compared");

		a = scn.nextInt();
		b = scn.nextInt();
		c = scn.nextInt();

		// Calling the above function in main
		max = biggestOfThree(a, b, c);

		// Printing the largest number
		System.out.println(max + " is the largest number.");
		scn.close();
	}
}
