package patterns;

public class SolidRectangle {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		printRectangle(5, 5);
	}

	public static void printRectangle(int width, int height) {
		int i;
		int j;
		for (i = 0; i < height; i++) {
			for (j = 0; j < width; j++) {
				printStars(width);
			}
			System.out.println("");
		}
	}

	public static void printStars(int amount) {
		System.out.print("* ");
	}
}