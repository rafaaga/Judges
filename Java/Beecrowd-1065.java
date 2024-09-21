import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b, c, d, e, cont;
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();
        d = sc.nextInt();
        e = sc.nextInt();
        cont = 0;
        if (a % 2 == 0) {
            cont += 1;
        }
        if (b % 2 == 0) {
            cont += 1;
        }
        if (c % 2 == 0) {
            cont += 1;
        }
        if (d % 2 == 0) {
            cont += 1;
        }
        if (e % 2 == 0) {
            cont += 1;
        }
        System.out.println(cont+" valores pares");
    }
}