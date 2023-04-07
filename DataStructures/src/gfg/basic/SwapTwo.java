package gfg.basic;

import java.util.Scanner;

public class SwapTwo {

	public static void main(String[] args) {
		
		/*Simplest way to swap two numbers without using a third variable in a single line.
		  					a = (a + b) - (b = a) 
		 This gives us "a + b - a", which simplifies to just "b", which we are equating to a */
		
		int a, b;

		System.out.println("Enter integer 'a': ");
		Scanner scn = new Scanner(System.in);

		a = scn.nextInt();

		System.out.println("Enter integer 'b': ");
		b = scn.nextInt();

		System.out.println("Before swapping, the Value of a is " + a + " and the Value of b is " + b);

		a = (a + b) - (b = a);

		System.out.println("After Swapping, the Value of a is " + a + " and the Value of b is " + b);
		scn.close();

	}
}
