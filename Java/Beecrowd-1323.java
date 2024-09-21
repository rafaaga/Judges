import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n;
        long res[] = new long[100];
        res[0] = 1;
        for (int i = 1; i < res.length; i++) {
            res[i] = (long) Math.pow(i+1, 2) + res[i - 1];
        }
        while (true) {
            n = sc.nextInt();
            if (n == 0) {
                break;
            }
            System.out.println(res[n - 1]);
        }
    }
}
