import math
import mmh3

class Slot:
    def __init__(self):
        self.remainder = 0
        self.bucket_occupied = False
        self.run_continued = False
        self.is_shifted = False


class QuotientFilter:
    def __init__(self, q, r):
        self.q = q
        self.r = r
        self.size = 2**q
        self.filter = [Slot() for _ in range(self.size)]
        
    def insert(self, item):
        fingerprint = mmh3.hash(item, 0) % self.size
        
        quotient = math.floor(fingerprint / 2**self.r)
        remainder = fingerprint % 2**self.r
        print(quotient, remainder)
        
        curr_pos = quotient
        run_exists = self.filter[curr_pos].bucket_occupied
        if not self.filter[curr_pos].bucket_occupied and not self.filter[curr_pos].is_shifted:
            self.filter[curr_pos].remainder = remainder
            self.filter[curr_pos].bucket_occupied = True
            return
        
        elif not self.filter[curr_pos].bucket_occupied:
            self.filter[curr_pos].bucket_occupied = 1
            
        while(self.filter[curr_pos].is_shifted):
            if curr_pos==0: curr_pos = self.size-1
            else: curr_pos -= 1
        
        if curr_pos != quotient: 
            runs_seen = 1
            before_quo = True
            
            while runs_seen > 0:
                curr_pos += 1
                if curr_pos == self.size: curr_pos = 0
                if curr_pos == quotient: before_quo = False
                if self.filter[curr_pos].bucket_occupied and before_quo: runs_seen += 1
                if not self.filter[curr_pos].run_continued: run_seen -= 1
            
                
        begin_run = True
        if run_exists and self.filter[curr_pos].remainder == remainder: return
        elif run_exists and self.filter[curr_pos].remainder < remainder:
            begin_run = False
            curr_pos += 1
            if curr_pos == self.size: curr_pos=0
            while self.filter[curr_pos].run_continued:
                if self.filter[curr_pos].remainder == remainder: return
                elif self.filter[s].remainder > remainder: break
                curr_pos += 1
                if curr_pos == self.size: curr_pos = 0
                
        temp = curr_pos
        
        if curr_pos == quotient:
            self.filter[curr_pos].remainder = remainder
            self.filter[curr_pos].bucket_occupied = True
            if run_exists: self.filter[temp].run_continued = True
        elif begin_run:
            self.filter[curr_pos].remainder = remainder
            self.filter[curr_pos].is_shifted = True
            self.filter[curr_pos].bucket_occupied = self.filter[curr_pos].bucket_occupied and self.filter[temp].bucket_occupied
            if run_exists: self.filter[temp].run_continued = True
        else:
            self.filter[curr_pos].remainder = remainder
            self.filter[curr_pos].is_shifted = True
            self.filter[curr_pos].run_continued = True
            self.filter[curr_pos].bucket_occupied = self.filter[curr_pos].bucket_occupied and self.filter[temp].bucket_occupied

        while self.filter[temp].bucket_occupied or self.filter[temp].is_shifted:
            curr_pos += 1
            if curr_pos == self.size: curr_pos = 0
            
            curr_pos, temp = temp, curr_pos
            
        
    def lookup(self, item):
        fingerprint = mmh3.hash(item, 0) % self.size
        
        quotient = math.floor(fingerprint / 2**self.r)
        remainder = fingerprint % 2**self.r
        
        if not self.filter[quotient].bucket_occupied: return False
        
        curr_pos = quotient
        while(self.filter[curr_pos].is_shifted):
            if curr_pos==0: curr_pos = self.size-1
            else: curr_pos -= 1
    
        if curr_pos != quotient: 
            runs_seen = 1
            before_quo = True
            
            while runs_seen > 0:
                curr_pos += 1
                if curr_pos == self.size: curr_pos = 0
                if curr_pos == quotient: before_quo = False
                if self.filter[curr_pos].bucket_occupied and before_quo: runs_seen += 1
                if not self.filter[curr_pos].run_continued: run_seen -= 1
            
        if self.filter[curr_pos].remainder == remainder: return True
        elif self.filter[curr_pos].remainder < remainder:
            curr_pos += 1
            if curr_pos == self.size: curr_pos = 0
            while self.filter[curr_pos].run_continued:
                if self.filter[curr_pos].remainder == remainder: return True
                elif self.filter[curr_pos].remainder > remainder: return False
                curr_pos += 1
                if curr_pos == self.size: curr_pos = 0
            
        return False
