import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        try {
            int a, cont=0;
            a = sc.nextInt();
            for (int i = a; i <= a+20; i++) {
                if (i%2==1) {
                    cont +=1;
                    System.out.println(i);
                }if (cont==6) {
                    break;
                }
            }
        } catch (Exception e) {
        }
    }
}