import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
        int t = sc.nextInt();
            for (int i = 0; i < t; i++) {
        String ent = sc.next();
        int sum = 0, re;
        boolean ver = false;
        String res = "0";
        String num = "1234567890";
        for (int k = 0; k < ent.length(); k++) {
            for (int j = 0; j < num.length(); j++) {
                if (ent.charAt(k) == num.charAt(j)) {
                    ver = true;
                }
            }
            if (ver) {
                res += ent.charAt(k);
                if (k==ent.length()-1) {
                    re = Integer.parseInt(res);
                    sum = sum + re;
                }
            }else{
                re = Integer.parseInt(res);
                sum = sum + re;
                res = "0";
            }
            ver = false;
        }
        System.out.println(sum);
            }
        } catch (Exception e) {
        }
        }
}
