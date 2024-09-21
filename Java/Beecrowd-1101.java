import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            int a, b;
            a = sc.nextInt();
            b = sc.nextInt();
            while (a!=0 && a>0 && b!=0 && b>0) {
                int cont = 0;
                if (b < a) {
                    for (int i = b; i <= a; i++) {
                        cont += i;
                        System.out.print(i + " ");
                    }
                }else{
                    for (int i = a; i <= b; i++) {
                        cont +=i;
                        System.out.print(i+" ");
                    }
                }
                System.out.println("Sum="+ cont);
                cont = 0;
                a = sc.nextInt();
                b = sc.nextInt();
            }
        } catch (Exception e) {
        }
    }
}