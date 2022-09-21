package basicMath;

import java.io.*;
import java.util.Scanner;

class ReverseInt {

	static int rev = 0;

	static void reverse(int n) {

		if (n <= 0)
			return;

		int rem = n % 10;

		rev = (rev * 10) + rem;

		reverse(n / 10);
	}

	public static void main(String[] args) {

		System.out.println("Enter the number you wish to reverse");
		Scanner scn = new Scanner(System.in);
		int n = scn.nextInt();

		reverse(n);

		System.out.print("Reversed Number is " + rev);
		scn.close();
	}
}
