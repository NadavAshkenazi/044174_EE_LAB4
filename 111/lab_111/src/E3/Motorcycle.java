package E3;

public class Motorcycle extends Vehicle {
    public Motorcycle(double gpk, String make, String color, double tankSize){
        super(gpk, make, color, tankSize);
        this.tiresNum = 2;
    }
}
