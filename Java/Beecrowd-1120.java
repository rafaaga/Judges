import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String n1;
        String [] x;
        try {
            x = sc.nextLine().split(" ");
            while (!(x[0].equals("0") && x[1].equals("0"))) {
                
                n1 = x[1].replace(x[0], "");
                n1 = n1.replaceFirst("0*", "");
                if (n1.length() > 0) {
                    System.out.println(n1);
                } else {
                    System.out.println("0");
                }
                x = sc.nextLine().split(" ");
            }
        } catch (Exception e) {
        }
    }
}