import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int k = 0; k < t; k++) {
            String num = sc.next();
            int cont = 0;
            for (int i = 0; i < num.length(); i++) {
                switch (num.charAt(i)) {
                    case '1':
                        cont += 2;
                        break;
                    case '2':
                    case '5':
                    case '3':
                        cont += 5;
                        break;
                    case '6':
                    case '9':
                    case '0':
                        cont += 6;
                        break;
                    case '4':
                        cont += 4;
                        break;
                    case '7':
                        cont += 3;
                        break;
                    case '8':
                        cont += 7;
                        break;
                }
            }
            System.out.println(cont + " leds");
        }

    }

}