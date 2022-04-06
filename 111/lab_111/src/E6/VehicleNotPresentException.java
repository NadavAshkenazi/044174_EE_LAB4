package E6;

public class VehicleNotPresentException extends RuntimeException {
    public VehicleNotPresentException(){
        super("vehicle not found");
    }
}
