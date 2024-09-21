import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        try {
            int a, b, cont = 0, aux;
                a = sc.nextInt();
                b = sc.nextInt();
                aux = a;
                if (a>b) {
                a = b;
                b = aux;
                }
                for (int i = a+1; i <b; i++) {
                    if (i%2==1 || i%2==-1) {
                        cont +=i;
                    }
                }
                    System.out.println(cont);
                    cont = 0;
        } catch (Exception e) {
        }
    }
}