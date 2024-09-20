import java.util.Scanner;

public class ArmstrongNumber {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            int t = sc.nextInt(), n, exp, result;
            String num;
            for (int i = 0; i < t; i++) {
                n = sc.nextInt();
                num = ""+ n;
                exp = num.length();
                result = 0;
                for (int j = 0; j < exp; j++) {
                    result += Math.pow(Integer.parseInt(""+num.charAt(j)), exp);
                }
                if (result==n) {
                    System.out.println("Armstrong");
                } else {
                    System.out.println("Not Armstrong");
                }
            }
        } catch (NumberFormatException e) {
        }

    }

}
