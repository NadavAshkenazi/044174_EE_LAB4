package E7;

public abstract class WheeledVehicle extends Vehicle {
    private int tiresNum;

    public WheeledVehicle(double gpk, String make, String color, double tankSize, int tiresNum) {
        super(gpk, make, color, tankSize);
        this.tiresNum = tiresNum;
    }

        public int changeTires(){
            return this.tiresNum;
    }
}
