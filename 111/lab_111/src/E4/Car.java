package E4;

public class Car extends Vehicle {

    public Car (double gpk, String make, String color, double tankSize){
        super(gpk, make, color, tankSize);
        this.tiresNum = 4;
    }
}
