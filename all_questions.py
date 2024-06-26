# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "The ruleset is not mutually exclusive since some cases can satisfy multiple rules at once, such as a low income person with a house (rules 1 and 3)"
    answers["(b) explain"] = "The ruleset does not cover every possible scenario from the attributes."
    answers["(c) explain"] = "The rules should be ordered, since the rules are not mutually exclusive."
    answers["(d) explain"] = "There should be a default rule, since the ruleset does not cover every posisble scenario."

    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "yes"
    answers["(b)"] = "no"
    answers["(c)"] = "no"

    # explain-string: explanation in english prose
    answers["(a) example"] = "Yes, since each rule produces a different results and the results cannot overlap."
    answers["(b) example"] = "No, since there are no rules covering amphibians."
    answers["(c) example"] = "No, since the rules are mutually exclusive the order in which they are enforced does not matter."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = True

    # explain_string: explanation in english prose
    answers["(a) explain"] = "During the forward pass of Back-Propagation, the k + 1th layer is calculated using the activations at nodes in the kth layer."
    answers["(b) explain"] = "During the forward pass of an ANN, the activations at the k + 1th layer are calucluated based off of the weights and biases of the previous layer, regardless of if the model is testing or training values."
    answers["(c) explain"] = "While the Vanishing Gradient Problem does cause gradients to slowly 'vanish' into values of zero, the test errors remaining large is not indicative of the issue."
    answers["(d) explain"] = "If all of the training instances were to be perfectly classified, the predicted output would always match the actual ouput, meaning that the loss function will result in a value of zero."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}
    # work is in work.ipynb
    # float
    answers["(a) P(X_1=1)"] = .65
    answers["(a) P(X_2=1)"] = .41
    answers["(a) P(X_1=1,X_2=1)"] = .28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "independent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "yes"

    # float
    answers["(c) P(X_1=1 | +)"] = .8
    answers["(c) P(X_1=1 | -)"] = .5
    answers["(c) P(X_2=1 | +)"] = .5
    answers["(c) P(X_2=1 | -)"] = .32
    answers["(c) P(X_3=1 | +)"] = .4
    answers["(c) P(X_3=1 | -)"] = .4

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = '+'
    answers["(d) Row 2"] = '+'
    answers["(d) Row 3"] = '-'
    answers["(d) Row 4"] = '-'

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.0

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 5
    answers["(b) K"] = 50

    # explain_string
    answers["(a) explain"] = "A smaller number of k would be better, since there is a clear separation between groups and a smaller k would lead to less missclassification for the points close to the tight red cluster."
    answers["(b) explain"] = "A larger number of k would be better here, since the values are more mixed and a small k would lead to a lot of missclassification."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 3/5
    answers["(a) P(B=1|+)"] = 2/5
    answers["(a) P(C=1|+)"] = 4/5
    answers["(a) P(A=1|-)"] = 2/5
    answers["(a) P(B=1|-)"] = 3/5
    answers["(a) P(C=1|-)"] = 1/5

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "There are 3 instances where A is present in a class labeled positive."
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = .8 #work in work.ipynb
    answers["(b) P(R|+)"] = .192
    answers["(b) P(R|-)"] = .048

    # string, '+' or '-'
    answers["(b) class label"] = "+"

    # explain_string
    answers["(b) Explain your reasoning"] = "The posterior for the positive probabilities is greater than that of the negatives."
  
    # float
    answers["(c) P(A=1)"] = .5
    answers["(c) P(B=1)"] = .4
    answers["(c) P(A=1,B=1)"] = .2

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = 'yes' if .2 == .5*.4 else 'no'
    
    # type: float
    answers["(d) P(A=1)"] = .5
    answers["(d) P(B=0)"] = .6
    answers["(d) P(A=1,B=0)"] = .3

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = 'yes' if .3 == .5*.6 else 'no'
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = .1
    answers["(e) P(A=1|+)"] = .3
    answers["(e) P(B=1|+)"] = .2

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = 'yes' if .1 == .3*.2 else 'no'

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] = "They are not independent, since the product of P(A=1|+) and P(B=1|+) is not equal to P(A=1,B=1 |+)"
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    #answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    #answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
