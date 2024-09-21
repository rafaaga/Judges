import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int L,R;
        L = sc.nextInt();
        R = sc.nextInt();
        while (L!=0 || R!=0) {            
            L = sc.nextInt();
            R = sc.nextInt();
            System.out.println(L+R);
            L = sc.nextInt();
            R = sc.nextInt();
        }
    }
}