package E4;

import java.util.HashMap;
import java.util.Map;

public class SizeableVehicleStorage<K, V> extends HashMap<K, V> {
    private final int maxSize;

    public SizeableVehicleStorage(int maxSize){
        super();
        this.maxSize = maxSize;
    }

    @Override
    public V put(K key, V value) {
        if (this.size() + 1 <= this.maxSize)
            return super.put(key, value);
        throw new StorageError();
    }


    @Override //check if needed SizeableVehicleStorage
    public void putAll(Map<? extends K, ? extends V> m) {
        if (this.size() + m.size() <= this.maxSize)
            super.putAll(m);
        throw new StorageError();
        }

    @Override
    public V putIfAbsent(K key, V value){
        if (this.size() + 1 <= this.maxSize)
            return super.putIfAbsent(key, value);
        throw new StorageError();
    }

    public static void main(String args[]){
        SizeableVehicleStorage<Integer, Vehicle> svs = new SizeableVehicleStorage(2);
        Car c = new Car(8, "WV", "Orange", 40);
        Motorcycle m = new Motorcycle(5, "AR", "Black", 10);
        Truck t = new Truck(20, "BMW", "Gray", 60);
        svs.put(1, c);
        svs.put(4, m);
        try{
            svs.put(42, t);
        }
        catch(RuntimeException e){
            System.out.println(e);
        }
        svs.remove(1);
        svs.put(42, t);
    }


}
