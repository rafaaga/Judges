import java.util.Scanner;
import java.util.Arrays;

class HorseRacing {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tian[] = null;
        int king[] = null;
        int n, lk, lt, hk, ht, ans;
         try {
            n = sc.nextInt();
            while(n!=0){
                boolean empate = true;
                lk = 0;
                lt = 0;
                hk = n-1;
                ht = n-1;
                ans = 0;
                tian = new int[n];
                king = new int[n];
                for (int j = 0; j < n; j++) {
                    tian[j] = sc.nextInt();
                }
                for (int j = 0; j < n; j++) {
                    king[j] = sc.nextInt();
                }
                Arrays.sort(tian);
                Arrays.sort(king);
                int i = 0;
                while(empate && i < n){
                    if(tian[ht] > king[hk]){
                        ans = ans + 200;
                        ht--;
                        hk--;
                    }else if(tian[lt] > king[lk]){
                        ans = ans + 200;
                        lt++;
                        lk++;
                    }else if(tian[lt] < king[hk]){
                        ans = ans - 200;
                        lt++;
                        hk--;
                    }else{
                        empate = false;
                    }
                    i++;
                }
                System.out.println(ans);
                n = sc.nextInt();
            }
        } catch (Exception e) {
        }
    }
}