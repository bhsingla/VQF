import org.apache.commons.codec.digest.MurmurHash3;

import java.math.BigInteger;
import java.security.MessageDigest;

public class Helper {
    public static int hash1String(String input){
        try{
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] messageDigest = md.digest(input.getBytes());
            return new BigInteger(messageDigest).intValue();
        } catch (Exception e){
            System.out.println("Unable to hash the input string...");
        }
        return -1;
    }

    public static int mmhash(String input){
        try{
            int hashedValue = MurmurHash3.hash32x86(input.getBytes());
            return hashedValue;
        } catch (Exception e){
            System.out.println("Unable to hash the input string...");
        }
        return -1;
    }

}


