package PreReport;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import java.lang.Math;

public class Q4 {
    public static void main(String[] args) {

        List<String> strings = Arrays.asList("abc", "", "bc", "efg", "abcd", "", "jkl");
        List<String> nonEmptyStrings = new ArrayList<String>();

        // get count of empty strings
        int count = (int) strings.stream().filter(string -> !string.isEmpty()).count();
        System.out.println("Q4.a: Non-Empty words count: " + count);
        for (String s: strings){
            if (!s.isEmpty()){
                nonEmptyStrings.add(s);
//                System.out.println(s);
            }
        }
        System.out.println("Q4.b: Non-Empty words: " + nonEmptyStrings);
        Random rnd = new Random();
        int size = Math.abs(rnd.nextInt()) % 5 + 2;
        List<Integer> numsArray = Stream.generate(() -> (rnd.nextInt() % 10)).limit(size).collect(Collectors.toList());
        List<Integer> numsSquareArray = numsArray.stream().mapToInt(i -> i*i).boxed().collect(Collectors.toList());
        System.out.println("Q4.c: Squares: " + numsSquareArray);
        System.out.println("      Squares sum: " + numsSquareArray.stream().mapToInt(i-> i).sum());
    }
}
