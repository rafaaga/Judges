import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            int a, b, c;
            String n;
            a = sc.nextInt();
            b = sc.nextInt();
            while (a!=0 && b!=0) {
                c = a + b;
                n = c + "";
                System.out.println(n.replace("0", ""));
                a = sc.nextInt();
                b = sc.nextInt();
            }
        } catch (Exception e) {
        }
    }
}