from decimal import Decimal
import gmpy2
import binascii

c1 = 13981765388145083997703333682243956434148306954774120760845671024723583618341148528952063316653588928138430524040717841543528568326674293677228449651281422762216853098529425814740156575513620513245005576508982103360592761380293006244528169193632346512170599896471850340765607466109228426538780591853882736654
c2 = 79459949016924442856959059325390894723232586275925931898929445938338123216278271333902062872565058205136627757713051954083968874644581902371182266588247653857616029881453100387797111559677392017415298580136496204898016797180386402171968931958365160589774450964944023720256848731202333789801071962338635072065
e1 = 13
e2 = 15
modulus = 103109065902334620226101162008793963504256027939117020091876799039690801944735604259018655534860183205031069083254290258577291605287053538752280231959857465853228851714786887294961873006234153079187216285516823832102424110934062954272346111907571393964363630079343598511602013316604641904852018969178919051627

# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def xgcd(b, a):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  x0, y0

# https://codereview.stackexchange.com/questions/11181/counting-the-number-of-bits-of-a-positive-integer
def bitcount(n):
    a = 1
    while 1<<a <= n:
        a <<= 1

    s = 0
    while a > 1:
        a >>= 1
        if n >= 1<<a:
            n >>= a
            s += a
    if n > 0:
        s += 1

    return s

if __name__ == "__main__":

    # Common Modulus Attack

    a, b = xgcd(e1, e2)
    print "(a, b) = " + str(a) + ", " + str(b)

    n = bitcount(modulus)
    print "n = " + str(n)

    i = gmpy2.invert(c2, modulus)
    print "i = " + str(i)

    mx = c1 ** a
    #print mx
    my = i ** -b
    #print my

    m = mx * my % modulus 
    print "m = " + str(m)

    hm = hex(m)
    print hm

    print binascii.unhexlify(hm[2:-1] + "0")
