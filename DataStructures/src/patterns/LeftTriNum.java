package patterns;

public class LeftTriNum {

	public static void main(String[] args) {
		int a = 5;
		

patternA(a);
	}

	static void patternA(int n) {
		for  (int row = 0; row < n; row++) {
			
			for  (int col = 0; col <= row; col++) {
				
	System.out.print(col+1);			
				
			}
			System.out.println();
		}
	}
	
}
