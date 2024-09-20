import java.util.Arrays;
import java.util.Scanner;

public class CostCutter {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int vector[] = null;
        try {
            int caso = sc.nextInt();
            for (int i = 0; i < caso; i++) {
                vector = new int[3];
                for (int j = 0; j < 3; j++) {
                    vector[j] = sc.nextInt();
                }
                Arrays.sort(vector);
                System.out.println("Case " + (i + 1) + ": " + vector[1]);
            }
        } catch (Exception e) {
        }

    }

}
