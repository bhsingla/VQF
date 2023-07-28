public class Vector_QF {
    Block[] filter;
    int numBlocks /*B = n/s*/;
    int numBuckets /*b*/;
    int numElements /*n*/;
    int numFingerprints /*s=log(logn)*/;
    int r = 5;

    public Vector_QF(int numElements, int numBuckets){
        numBuckets = numBuckets;
        numFingerprints = Double.valueOf(Math.log(Math.log(numElements))).intValue();
        numBlocks = (numElements/numFingerprints)+1;
        filter = new Block[numBlocks];
        for(int i=0; i<numBlocks;i++){
            filter[i] = new Block(numBuckets, numFingerprints);
        }
    }


    public void insert(String item){
        int u = Helper.hash1String(item);
        int b1 = Helper.mmhash(item)%this.numBlocks;
        int b2 = b1^u;
        int i = b1;
        if(select(filter[b2].metadata,numBuckets-1)<select(filter[b1].metadata,numBuckets-1)){
            i = b2;
        }
        if(select(filter[i].metadata, numBuckets-1) == numFingerprints+numBuckets-1){
            System.out.println("Filter is full, element cannot be inserted.");
            return;
        }
        int y = u/(2^r);  //need to check the values represented
        int t = u % (2^r);
        int m = select(filter[i].metadata, y);
        int z = m-y;
        int n = this.numBuckets+this.numFingerprints;
        while(n>m){
            filter[i].metadata[n] = filter[i].metadata[n-1];
            n = n-1;
        }
        n = this.numFingerprints;
        while(n>z){
            filter[i].metadata[n] = filter[i].metadata[n-1];
        }
        filter[i].metadata[m]=0;
        filter[i].fingerprints[z]=t;
    }

    public boolean lookup(String item) {
        int u = Helper.hash1String(item);
        int b1 = Helper.mmhash(item) % this.numBlocks;
        int b2 = b1 ^ u;
        return 0 <=find_fingerprint(b1,u) | 0 <= find_fingerprint(b2,u);
    }
    public int find_fingerprint(int i, int u){
        int y = u/(2^r);  //need to check the values represented
        int t = u % (2^r);
        int start;
        if(y == 0)  start =0;
        else start = select(filter[i].metadata,y-1)-y+1;
        int end = select(filter[i].metadata, y)-y;
        while(start<end){
            if(filter[i].fingerprints[start] == t)  return start;
            start +=1;
        }
        return -1;

    }

    public int select(int[] metadata, int j){
        for(int i = 0;i<metadata.length;i++){
            if(metadata[i] == 1){
                j--;
            }
            if(j==0)    return i;
        }
        return (metadata[metadata.length-1] ==1) ? -1 : metadata.length-1;
    }
}
