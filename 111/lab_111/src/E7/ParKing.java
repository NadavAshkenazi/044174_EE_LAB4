package E7;



import java.util.ArrayList;
import java.util.function.Predicate;


public class ParKing {
    private ArrayList<ParkingLot> lots;
    private static ParKing instance = null;

    private ParKing(){
        this.lots = new ArrayList<ParkingLot>();
    }

    public static ParKing getInstance(){
        if (ParKing.instance == null){
            ParKing.instance = new ParKing();
        }
        return ParKing.instance;
    }

    public void addLot(ParkingLot p){
        this.lots.add(p);
    }

    public double getBalance(){
        return this.lots.stream().mapToDouble(p -> p.getBalance()).sum();
    }

    public double getRevenue(){
        return this.lots.stream().mapToDouble(p -> p.getExpectedRevenue()).sum();
    }

    public int countVehicles(){
        return this.lots.stream().mapToInt(p -> (int)p.countWheeledVehicle()).sum();
    }

    public int countSpaceShips(){
        return this.lots.stream().mapToInt(p -> (int)p.countSpaceShip()).sum();
    }

    public int customCount(Predicate pred){
        return this.lots.stream().mapToInt(p -> (int)p.customCount(pred)).sum();
    }

    public static void main(String args[]){
        ParKing park = ParKing.getInstance();
        SpacePort spacePort = new SpacePort(4,4);
        Car car = new Car(8, "WV", "Orange", 40);
        Motorcycle motor = new Motorcycle(5, "AR", "Black", 10);
        CargoShip cargoShip = new CargoShip(2, "ET", "Purple", 1000, 4,3);
        DeathStar deathStar = new DeathStar(2, "TE", "Grenn", 1000);
        ParKing x = ParKing.getInstance();

        spacePort.enter(car, 2);
        spacePort.enter(motor, 2);
        spacePort.enter(cargoShip, 2);
        spacePort.enter(deathStar, 2);
        x.addLot(spacePort);

        System.out.println(park.countVehicles());
        System.out.println(park.countSpaceShips());
        System.out.println(x.getBalance());
        System.out.println(x.getRevenue());

        ParkingLot parkingLot = new ParkingLot(3,5);
        Truck truck = new Truck(20, "BMW", "Gray", 60);
        parkingLot.enter(truck, 1);
        park.addLot(parkingLot);

        System.out.println(park.countSpaceShips());
        System.out.println(park.countVehicles());
        System.out.println(park.getBalance());
        System.out.println(park.getRevenue());

        Predicate<Vehicle> gasTankGreaterThan50 = (i) -> i.getGasTank() > 50;
        System.out.println(x.customCount(gasTankGreaterThan50));
        parkingLot.exit(truck);

        System.out.println(park.getBalance());
        System.out.println(x.customCount(gasTankGreaterThan50));




    }
}



