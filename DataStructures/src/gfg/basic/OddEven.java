package gfg.basic;

import java.util.*;

public class OddEven {
	// Java Program to Check if Given Integer is Odd or Even by checking the LSB of
	// the Number
	public static String testOddEvenByCheckingLSB(int a) {

		if (a != 0) {
			if (Integer.toBinaryString(a).endsWith("0")) {
				return "Even";
			} else {
				return "Odd";
			}
		}

		else {
			return "Zero";
		}
	}

	public static void main(String[] args) {

		Scanner scn = new Scanner(System.in);
		int i = 0;
		
		System.out.println("Enter the number you want to check");
		i = scn.nextInt();
		
		System.out.println(i + " : " + testOddEvenByCheckingLSB(i));
	}
}
