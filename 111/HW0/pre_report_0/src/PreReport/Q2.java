package PreReport;

public class Q2 {
    public static void main(String args[]){
        int a1 = Integer.parseInt(args[0]);
        int d = Integer.parseInt(args[1]);
        int len = Integer.parseInt(args[2]);
        int an = a1;
        for (int i = 0; i < len; i++){
            System.out.print(an+ " ");
            an += d;
        }
        System.out.print("\n");
    }
}
