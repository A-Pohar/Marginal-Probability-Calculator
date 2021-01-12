import math

if __name__ == '__main__':
    print("Welcome to Marginal Probability Calculator!")
    prob_dist = input("Which probability distribution would you like to use "
                      "(Bernoulli/Binomial/Geometric/Negative Binomial/Poisson/Hypergeometric)?:").lower()

    if prob_dist == "bernoulli":
        prob_success = float(input("What is the probability of success (enter a decimal value)?: "))
        success_truth = bool(input("Does the success event happen?: "))
        if success_truth:
            probability = prob_success
        else:
            probability = 1 - prob_success

    elif prob_dist == "poisson":
        lamda_parameter = int(input("What will lambda be equal to?: "))
        prob_input = int(input("what will x be equal to?: "))

        probability = pow(math.e, -1 * lamda_parameter) * pow(lamda_parameter, prob_input) \
                      / math.factorial(prob_input)

    print("The probability is P(X = x) = " + probability)
