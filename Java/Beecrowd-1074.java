import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int P = sc.nextInt();
            if (P == 0) {
                System.out.println("NULL");
            } else if (P > 0 && P%2==0) {
                System.out.println("EVEN POSITIVE");
            } else if (P > 0 && P%2==1) {
                System.out.println("ODD POSITIVE");
            } else if (P < 0 && P%2==0) {
                System.out.println("EVEN NEGATIVE");
            } else if (P < 0 && P%2==-1) {
                System.out.println("ODD NEGATIVE");
            }
        }
    }
}