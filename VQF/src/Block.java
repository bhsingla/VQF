public class Block {
    int[] metadata;
    int[] fingerprints;

    int numBuckets /*b*/;
    int numFingerprints /*s*/;

    public Block(int buckets, int fingerprints){
        this.numBuckets = buckets;
        this.numFingerprints = fingerprints;
        this.metadata = new int[numBuckets+numFingerprints];
        this.fingerprints = new int[numFingerprints];
    }


}
