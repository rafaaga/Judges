import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        try {
            int caso = sc.nextInt(), a, b;
            String n, num, f;
            for (int i = 0; i < caso; i++) {
                a = sc.nextInt();
                b = sc.nextInt();
                n = a+"";
                num = b+"";
                if ( n.length() < num.length()) {
                    System.out.println("nao encaixa");
                }else{
                f = n.substring(n.length()-num.length(), n.length());
                    if (f.equals(num)) {
                        System.out.println("encaixa");
                    }else{
                        System.out.println("nao encaixa");
                    }
                }
                
            }
        } catch (Exception e) {
        }
    }
    
}