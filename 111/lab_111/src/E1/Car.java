package E1;

public class Car {
    private String color;
    private String make;
    private double gpk;
    private double gas;
    private double tankSize;
    private static final int tiresNum = 4;


    public Car(double gpk, String make, String color, double tankSize){
        this.gpk = gpk;
        this.make = make;
        this.color = color;
        this.tankSize = tankSize;
        this.gas = this.tankSize; //getting new car with full tank
    }

    public String toString(){
        return this.color + " " + this.make + " " + this.gas + "/" + this.tankSize;
    }

    public boolean drive(float distance){
        if (this.gpk * distance <= this.gas){
            this.gas  -= distance * this.gpk;
            return true;
        }
        return false;
    }

    public double fillGas(double pricePerLiter){
        double amountToFill = this.tankSize - this.gas;
        this.gas = this.tankSize;
        return amountToFill * pricePerLiter;
    }

    public void changeTires(){
        System.out.println("Changed " + this.tiresNum + " tires");

    }

    public static void main(String args[]){
        Car car1 = new Car(8, "WV", "Orange", 40);
        System.out.println(car1.toString());
        double payed = car1.fillGas(5);
        System.out.println("payed: " + payed);
        boolean drives = car1.drive(2);
        System.out.println("can we drive 2km? " + drives);
        System.out.println(car1.toString());
        drives = car1.drive(100);
        System.out.println("can we drive 100km? " + drives);
        System.out.println(car1.toString());
        car1.changeTires();

    }


}
