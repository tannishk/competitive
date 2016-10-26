import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

/**
 * Created by vipin on 26/10/16.
 */
public class TripleSum {
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = sc.nextInt();
        ArrayList<Integer> A = new ArrayList<>();
        for(int i=0;i<n;i++){
            A.add(sc.nextInt());
        }
        Collections.sort(A);
        boolean flag = false;
        for(int i=0;i<n-2;i++){
            if (!flag){
                int j = i+1;
                int k = n -1;
                while(k>=j){
                    if (A.get(i)+A.get(j)+A.get(k) > x){
                        k--;
                    }
                    else if (A.get(i)+A.get(j)+A.get(k) < x){
                        j++;
                    }
                    else {
                        System.out.println("1");
                        flag = true;
                        break;
                    }
                }
            }

        }
        if (!flag){
            System.out.println("0");
        }
    }
}
