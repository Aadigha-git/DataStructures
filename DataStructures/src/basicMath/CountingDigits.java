package basicMath;

import java.util.*;

public class CountingDigits {

	static int count_digits(int n) {

		String n2 = Integer.toString(n);
		return n2.length();
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Enter the integer to check length. ");
		Scanner scn = new Scanner(System.in);
		
		int n = scn.nextInt();
		System.out.println("Number of digits in " + n + " is: " + count_digits(n));
		
		scn.close();
	}

}
