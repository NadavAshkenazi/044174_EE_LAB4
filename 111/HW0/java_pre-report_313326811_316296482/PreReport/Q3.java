package PreReport;
import java.util.Random;
import java.lang.Math;

public class Q3 {
    public static void main(String args[]){
        Random rnd = new Random();
        int dim = Math.abs(rnd.nextInt()) % 10 + 2;
        int[][] matrix = new int[dim][dim];
        for (int i = 0; i < dim; i++){
            for (int j = 0; j < dim; j++){
                matrix[i][j] = (Math.abs(rnd.nextInt()) % 2);
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println("");
        }
        return;
    }
}
