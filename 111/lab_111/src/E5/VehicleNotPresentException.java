package E5;

public class VehicleNotPresentException extends RuntimeException {
    public VehicleNotPresentException(){
        super("vehicle not found");
    }
}
