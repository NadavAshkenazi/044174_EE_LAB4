package E6;


public class SpacePort extends ParkingLot{
    public SpacePort(int size, double pricePerHour){
        super(size,pricePerHour);
    }

    public void load(Vehicle v, CargoShip cs){
        if (this.isInLot(v) && this.isInLot(cs)){
            cs.enter(v, this.getExpectedTime(v)/ 2);
            this.exitByHours(v, this.getExpectedTime(v)/ 2);
        }
    }

    public void unload(Vehicle v, CargoShip cs){
        if (this.isInLot(cs) && cs.isInLot(v)){
            double time = cs.getExpectedTime(v);
            cs.exit(v);
            this.enter(v, time);
        }
    }

    public static void main(String args[]){
        SpacePort spacePort = new SpacePort(3,4);
        Car c = new Car(8, "WV", "Orange", 40);
        CargoShip cs = new CargoShip(2, "ET", "Purple", 1000, 4,3);
        spacePort.enter(c, 2.0);
        spacePort.load(c, cs);
        System.out.println(spacePort.enter(cs, 10));
        spacePort.load(c, cs);
        System.out.println(spacePort.getExpectedRevenue());
        System.out.println(spacePort.getBalance());
        spacePort.unload(c, cs);
        System.out.println(spacePort.getExpectedRevenue());
        System.out.println(spacePort.getBalance());
    }
}
