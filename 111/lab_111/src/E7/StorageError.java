package E7;

public class StorageError extends RuntimeException {
    public StorageError(){
        super("out of space");
    }
}
