#Ferihan Çabuk
#This code find the max path in pyramid integer matrix
#Dynamic programming is used for solving this question

pyramid2D = [] #define pyramid array to hold pyramid matrix reading from input file


def MaxPathFinder(r, c, CoinMatrix):

    costMatrix = [[0] * (r + 1) for _ in range(c + 2)]  #create a cost matrix

    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if j <= i:
                coinValue = CoinMatrix[i - 1][j - 1]
                if isPrime(coinValue): #if value on the road is prime do not choose this node for path
                    continue
                #Calculate the max profit road coming to that node
                costMatrix[i][j] = max(costMatrix[i - 1][j], costMatrix[i-1][j - 1], costMatrix[i-1][j+1]) + coinValue

    max1 = 0
    for col in costMatrix[r]:
        if col > max1:
            max1 = col
    print('Maximum sum is : ', max1)


def read_file_and_store_2D(input_file):  # Read numbers from file and store it into 2D array
    file1 = open(input_file, 'r')
    Lines = file1.readlines()
    for line in Lines:
        line_ = line.split()
        line_ = list(map(int, line_))
        pyramid2D.append(line_)


def isPrime(number):  # Control a number is prime or not

    if (number == 1):
        return False
    elif (number == 2):
        return True
    else:
        for x in range(2, number):
            if(number % x == 0):
                return False
        return True


read_file_and_store_2D("input.txt")
rows = len(pyramid2D)
columns = len(pyramid2D)
MaxPathFinder(rows, columns, pyramid2D)
