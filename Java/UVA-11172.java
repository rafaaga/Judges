import java.util.Scanner;

public class RelationalOperator {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            int t, a, b;
            t = sc.nextInt();
            for (int i = 0; i < t ; i++ ){
              a = sc.nextInt();
              b = sc.nextInt();
              if (a > b) {
                  System.out.println(">");
                } else if (a < b) {
                    System.out.println("<");
                } else {
                    System.out.println("=");
                }           
            } 
                
        } catch (Exception e) {

        }
    }
}