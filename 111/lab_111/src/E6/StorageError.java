package E6;

public class StorageError extends RuntimeException {
    public StorageError(){
        super("out of space");
    }
}
