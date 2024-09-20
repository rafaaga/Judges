import java.util.Scanner;

public class DetectionLanguage{

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int caso = 0;
        String palabra = "";
        try {
            while (!(palabra = sc.nextLine()).equals("#")) {

                caso++;
                switch (palabra) {
                    case "HELLO":
                        System.out.println("Case " + caso + ": ENGLISH");
                        break;
                    case "HOLA":
                        System.out.println("Case " + caso + ": SPANISH");
                        break;
                    case "CIAO":
                        System.out.println("Case " + caso + ": ITALIAN");
                        break;
                    case "BONJOUR":
                        System.out.println("Case " + caso + ": FRENCH");
                        break;
                    case "HALLO":
                        System.out.println("Case " + caso + ": GERMAN");
                        break;
                    case "ZDRAVSTVUJTE":
                        System.out.println("Case " + caso + ": RUSSIAN");
                        break;
                    default:
                        System.out.println("Case " + caso + ": UNKNOWN");
                        break;
                }
            }
        } catch (Exception e) {
        }
    }
}
