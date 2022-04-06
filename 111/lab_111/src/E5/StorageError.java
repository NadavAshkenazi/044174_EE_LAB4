package E5;

public class StorageError extends RuntimeException {
    public StorageError(){
        super("out of space");
    }
}
