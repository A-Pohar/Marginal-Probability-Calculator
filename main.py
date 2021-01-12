import math

if __name__ == '__main__':
    print("Welcome to Marginal Probability Calculator!")
    prob_dist = input("Which probability distribution would you like to use "
                      "(Bernoulli/Binomial/Geometric/Negative Binomial/Poisson/Hypergeometric)?: ").lower()

    if prob_dist == "bernoulli":
        prob_success = float(input("What is the probability of success (enter a decimal value)?: "))
        success_truth = input("Does the success event happen (yes/no)?: ").lower()
        if success_truth == "yes":
            probability = prob_success
            prob_x_input = 1
        elif success_truth == "no":
            probability = 1 - prob_success
            prob_x_input = 0

    elif prob_dist == "binomial":
        prob_success = float(input("What is the probability of success (enter a decimal value)?: "))
        num_trials = int(input("How many trials will occur?: "))
        num_successes = int(input("How many of these trials result in success?: "))

        probability = math.comb(num_trials, num_successes) * pow(prob_success, num_successes) *\
                      pow(1 - prob_success, num_trials - num_successes)
        prob_x_input = num_successes

    elif prob_dist == "geometric":
        prob_success = float(input("What is the probability of success (enter a decimal value)?: "))
        failed_trials = int(input("How many trials will result in failure?: "))

        probability = pow(1-prob_success, failed_trials) * prob_success
        prob_x_input = failed_trials

    elif prob_dist == "negative binomial":
        prob_success = float(input("What is the probability of success (enter a decimal value)?: "))
        num_fails = int(input("How many trials will result in failure?: "))
        num_successes = int(input("How many of these trials result in success?: "))

        probability = math.comb(num_successes - 1 + num_fails, num_successes - 1) * \
                      pow(prob_success, num_successes) *\
                      pow(1 - prob_success, num_fails)
        prob_x_input = num_fails

    elif prob_dist == "poisson":
        lamda_parameter = int(input("What will lambda be equal to?: "))
        prob_input = int(input("what will x be equal to?: "))

        probability = pow(math.e, -1 * lamda_parameter) * pow(lamda_parameter, prob_input) \
                      / math.factorial(prob_input)
        prob_x_input = prob_input

    print("The probability is P(X = " + str(prob_x_input) + ") = " + str(probability))
