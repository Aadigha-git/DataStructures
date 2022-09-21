package patterns;

public class UpPyramid {

	public static void main(String[] args) {
		int n = 5;
		pyramid(n);
	}

	public static void pyramid(int n) {

		for (int row = 0; row < n; row++) {

			for (int col = n - row; col > 1; col--) {
				System.out.print(" ");
			}
			for (int col = 0; col <= row; col++) {
				System.out.print("* ");
			}
			System.out.println();
		}

	}
}
