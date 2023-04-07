package gfg.basic;
import java.util.Scanner;

public class BinaryAdd {

	// Function to add two binary strings
	static String add_Binary(String x, String y) {

		// converting binary string into integer(decimal number)
		int num1 = Integer.parseInt(x, 2);
		int num2 = Integer.parseInt(y, 2);

		int sum = num1 + num2;
		// Adding those two decimal numbers and storing in sum

		String result = Integer.toBinaryString(sum);
		// Converting resultant decimal into binary
		
		return result;
	}

	public static void main(String args[]) {

		Scanner scn = new Scanner(System.in);

		String x = null, y = null;

		boolean validInput = false;

		// prompt the user to enter both binary strings
		while (!validInput) {
			System.out.print("Enter first binary string: ");
			x = scn.nextLine();

			System.out.print("Enter second binary string: ");
			y = scn.nextLine();

			if (x.matches("[01]+") && y.matches("[01]+")) {
				validInput = true;
			} else {
				System.out.println("Invalid input. Please enter two binary strings.");
			}
		}

		System.out.print("The resultant binary sum is: "+add_Binary(x, y));
		
		scn.close();
	}
}
