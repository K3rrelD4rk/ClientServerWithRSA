from random import rand

def is_prime(n: int) -> bool:
        if n < 2:
            return False
        elif n < 4:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        else:
            for i in range(5, int(n**0.5)+1, 6):
                if n % i == 0 or n % (i+2) == 0:
                    return False
            return True
            
class rsa:
    
    def gen_n(start_num):
        while True:
            if is_prime(start_num):
                return start_num
                break
            else:
                start_num+=1

    
    def rsaencode(plain_message):
        encrypted = plain_message
        return encrypted
    
    def rsadecode(encrypted_message):
        decrypted = encrypted_message
        return decrypted