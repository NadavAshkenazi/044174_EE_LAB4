package E5;

public class CargoShip extends SpaceShip{
    private ParkingLot parkingLot;

    public CargoShip(double gpk, String make, String color, double tankSize, int maxSize, double pricePerHour){
        super(gpk, make, color, tankSize);
        this.parkingLot = new ParkingLot(maxSize, pricePerHour);
    }

    public String toString() {
        return super.toString() + " " + parkingLot.getSize() + "/" + parkingLot.getMaxSize();
    }

    public boolean enter(Vehicle v, double expectedTime) {
        return this.parkingLot.enter(v, expectedTime);
    }

    public boolean exit(Vehicle v) {
        if (this.parkingLot.exit(v)){
            return true;
        }
        throw new VehicleNotPresentException();
    }




}
