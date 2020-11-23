import random
import time

flag = b"FAKE{this_is_a_fake_flag}"


start_seed = round(time.time() / 100 - 10, 5)

def main():
    seed_num = 0
    found = False

    number = random.randint(0, 500000)
    print(number)
    
    for i in range(500000):
        seed_num = round(start_seed + i/500000, 5)
        random.seed(seed_num)
        r1 = random.randint(1, 500000)

        if (r1 == number):
            print(" found seed ")
            fount = True
            break
        
        if (i % 500000 == 0):
            print("step {}".format(i/500000))

    if (found == False):
        print("seed not found")
    else:
        print("sending random numbers")
        random.seed(seed_num)
        r1 = random.randint(1, 500000)
        #r1 = random.randint(1, 500000)
        r2 = random.randint(1, 500000)

        print("{}".format(r1), "{}".format(r2))





    print("find a number")
    for i in range(20):
        print("challenge", i)
        client_challenge = int(input("input:"))
        if client_challenge == number:
            print("correct!!!")
            print(flag)
            exit()
        elif client_challenge < number:
            print("too small")
            print("try again!")
        else:
            print("too big")
            print("try again!")
    print("You've failed too many times")


if __name__ == "__main__":
    main()
