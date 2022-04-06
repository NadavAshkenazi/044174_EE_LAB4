package E5;

import java.util.ArrayList;
import java.util.List;

abstract class Vehicle {
    private double gpk;
    private String make;
    private String color;
    private double tankSize;
    private double gas;

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

    public String getMake(){
        return this.make;
    }
    public String getColor(){
        return this.color;

    }
}














