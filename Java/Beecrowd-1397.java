import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n, L, R, con, coun;
        n = sc.nextInt();
        while (n != 0) {
            n = sc.nextInt();
            con = 0;
            coun = 0;
            for (int i = 0; i < n; i++) {
                L = sc.nextInt();
                R = sc.nextInt();
                if (L > R) {
                    con += 1;
                } else if (L < R) {
                    coun += 1;
                } else {
                    con += 0;
                    coun += 0;
                }
            }
            System.out.println(con + " " + coun);
            n = sc.nextInt();
        }
    }
}