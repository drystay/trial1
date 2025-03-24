# trial1\
<<<<<<< HEAD
//this is a code
import java.util.Scanner;
public class ques2 {
    //SEQUENTIAL SEARCH
    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of the array");
        int n = sc.nextInt();
        int arr[]=new int [n];
        System.out.println("Enter the elements");
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        System.out.println("Enter the element you want to search");
        int search=sc.nextInt();
        for(int i=0;i<n;i++){
           if(arr[i]==search){
               System.out.println(i);
           }
           else{
               System.out.println("Not in the array");
           }
        }
        sc.close();
    }
}
=======

>>>>>>> 28d4cd6b36c89dcd86c97f949c63bc9aa12eb401
