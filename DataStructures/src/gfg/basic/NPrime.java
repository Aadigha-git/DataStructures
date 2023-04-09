package gfg.basic;

import java.util.Scanner;

//Java program to print all primes smaller than or equal to n
//using Sieve of Eratosthenes

/* Let us take an example when n = 50.
 *  So we need to print all prime numbers smaller than or equal to 50. 
 *  We create a list of all numbers from 2 to 50. 
 *  According to the algorithm we will mark all the numbers which are divisible by 2 and are greater than or equal to the square of it. 
Now we move to our next unmarked number 3 and mark all the numbers which are multiples of 3 and are greater than or equal to the square of it. */

class NPrime {
	void sieveOfEratosthenes(int n) {
		// Create a boolean array
		// "prime[0..n]" and
		// initialize all entries
		// it as true. A value in
		// prime[i] will finally be
		// false if i is Not a
		// prime, else true.
		boolean prime[] = new boolean[n + 1];
		for (int i = 0; i <= n; i++)
			prime[i] = true;

		for (int p = 2; p * p <= n; p++) {
			// If prime[p] is not changed, then it is a
			// prime
			if (prime[p] == true) {
				// Update all multiples of p
				for (int i = p * p; i <= n; i += p)
					prime[i] = false;
			}
		}

		// Print all prime numbers
		for (int i = 2; i <= n; i++) {
			if (prime[i] == true)
				System.out.print(i + " ");
		}
	}

	// Driver Code
	public static void main(String args[]) {
		Scanner scn = new Scanner(System.in);
		int N;
		System.out.println("Define n, upto which you want to find the prime numbers: ");
		N = scn.nextInt()
		System.out.println("All the Prime numbers within 1 and " + N + " are:");
		NPrime g = new NPrime();
		g.sieveOfEratosthenes(N);
		scn.close();
	}
}
