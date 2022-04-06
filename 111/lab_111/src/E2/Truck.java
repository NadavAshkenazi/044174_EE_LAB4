package E2;

public class Truck extends Vehicle {
    public Truck(double gpk, String make, String color, double tankSize){
        super(gpk, make, color, tankSize);
        this.tiresNum = 4;
    }
}
