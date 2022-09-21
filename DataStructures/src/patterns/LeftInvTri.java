package patterns;

public class LeftInvTri {

	public static void main(String[] args) {
		int a = 5;

		patternA(a);
	}

	static void patternA(int n) {
		for (int row = n; row > 0; row--) {
			for (int col = 0; col < row; col++) {
				System.out.print("* ");
				// for numbers
				// System.out.println(col+1);
			}
			System.out.println();
		}
	}

}
