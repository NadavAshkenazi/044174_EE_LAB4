package E4;

public class StorageError extends RuntimeException {
    public StorageError(){
        super("out of space");
    }
}
