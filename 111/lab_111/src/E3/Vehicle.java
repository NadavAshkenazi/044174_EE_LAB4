package E3;

import java.util.ArrayList;
import java.util.List;

abstract class Vehicle {
    private double gpk;
    private String make;
    private String color;
    private double tankSize;
    private double gas;
    protected int tiresNum;

    public Vehicle(double gpk, String make, String color, double tankSize) {
        this.gpk = gpk;
        this.make = make;
        this.color = color;
        this.tankSize = tankSize;
        this.gas = this.tankSize; //getting new car with full tank
    }

    public String toString() {
        return this.color + " " + this.make + " " + this.gas + "/" + this.tankSize;
    }

    public boolean drive(float distance) {
        if (this.gpk * distance <= this.gas) {
            this.gas -= distance * this.gpk;
            return true;
        }
        return false;
    }

    public double fillGas(double pricePerLiter) {
        double amountToFill = this.tankSize - this.gas;
        this.gas = this.tankSize;
        return amountToFill * pricePerLiter;
    }

    public int changeTires(){
        return this.tiresNum;
    }

    public static void main(String args[]){
        List<Vehicle> vehicle_list = new ArrayList<>();
        Car c = new Car(8, "WV", "Orange", 40);
        Motorcycle m = new Motorcycle(5, "AR", "Black", 10);
        Truck t = new Truck(20, "BMW", "Gray", 60);
        vehicle_list.add(c);
        vehicle_list.add(m);
        vehicle_list.add(t);
        vehicle_list.forEach(
                (vehicle)->{
                    System.out.println(vehicle.toString() + " Number of tires = " + vehicle.changeTires());
                }
        );
    /*
        Expected:
            Orange WV 40.0/40.0 Number of tires = 4
            Black AR 10.0/10.0 Number of tires = 2
            Gray BMW 60.0/60.0 Number of tires = 4
     */
    }
}














