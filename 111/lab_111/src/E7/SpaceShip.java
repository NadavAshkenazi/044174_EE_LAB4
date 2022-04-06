package E7;

import java.util.ArrayList;
import java.util.List;

public abstract class SpaceShip extends Vehicle {

    public SpaceShip(double gpk, String make, String color, double tankSize){
        super(gpk, make, color, tankSize);
    }

    @Override
    public String toString() {
        return this.getColor() + " " + this.getMake();
    }

    public boolean liftoff(float distance){
        return this.drive(distance);
    }

    public void shoot(){
        System.out.println("Bcuck!");
    }


    public static void main(String args[]){
        List<SpaceShip> vehicle_list = new ArrayList<>();
        Motorcycle m = new Motorcycle(5, "AR", "Black", 10);
        Motorcycle m2 = new Motorcycle(5, "AR", "Black", 10);
        Truck t = new Truck(20, "BMW", "Gray", 60);
        CargoShip cargo = new CargoShip(2, "BMW2", "Gray2", 60, 2, 5);
        cargo.enter(m, 3);
        cargo.enter(t, 3);
        try{
            cargo.exit(m2);
        }
        catch (Exception e) {
            System.out.println(e);
        }

        cargo.enter(m2, 3);
    }
}
