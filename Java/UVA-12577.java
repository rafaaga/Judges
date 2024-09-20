import java.util.Scanner;

public class HajjeAkbar {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int caso = 0;
        String palabra = "";
        try {
            while (!(palabra = sc.nextLine()).equals("*")) {

                caso++;
                if ("Hajj".equals(palabra)) {
                    System.out.println("Case " + caso + ": Hajj-e-Akbar");
                } else if ("Umrah".equals(palabra)) {
                    System.out.println("Case " + caso + ": Hajj-e-Asghar");
                } 
            }
        } catch (Exception e) {
        }

    }
}
