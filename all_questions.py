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
def question2():#told that this question is not necessary by TA.
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


    # float
    answers["(a) P(X_1 = 1 | +)"] = None
    answers["(a) P(X_1 = 1 | -)"] = None
    answers["(a) P(X_2 = 1 | +)"] = None
    answers["(a) P(X_2 = 1 | -)"] = None
    answers["(a) P(X_3 = 1 | +)"] = None
    answers["(a) P(X_3 = 1 | -)"] = None

    # string
    answers["(b) label"] = None

    # float
    answers["(c) P(X_1=1)"] = None
    answers["(c) P(X_2=1)"] = None
    answers["(c) P(X_1=1,X_2=1)"] = None

    # string: "dependent" or "independent"
    answers["(c) Relationship between X_1 and X_2"] = None

    # float
    answers["(d) P(A=1)"] = None
    answers["(e) P(X_1=1, X_2=1|Class=+)"] = None
    answers["(e) P(X_1=1|Class=+)"] = None
    answers["(e) P(X_2=1|Class=+)"] = None

    # string: "yes" or "no"
    answers["(e) A and B conditionally independent?"] = None

    # float
    answers["(d) Training error rate"] = None

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = None
    answers["(b) K"] = None

    # explain_string
    answers["(a) explain"] = None
    answers["(b) explain"] = None

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = None
    answers["(a) P(B=1|+)"] = None
    answers["(a) P(C=1|+)"] = None
    answers["(a) P(A=1|-)"] = None
    answers["(a) P(B=1|-)"] = None
    answers["(a) P(C=1|-)"] = None

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = None
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = None  # WRONG
    answers["(b) P(R|+)"] = None
    answers["(b) P(R|-)"] = None

    # string, '+' or '-'
    answers["(b) class label"] = None

    # explain_string
    answers["(b) Explain your reasoning"] = None
  
    # float
    answers["(c) P(A=1)"] = None
    answers["(c) P(B=1)"] = None
    answers["(c) P(A=1,B=1)"] = None

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = None
  
    # type: float
    answers["(d) P(A=1)"] = None
    answers["(d) P(B=0)"] = None
    answers["(d) P(A=1,B=0)"] = None

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = None
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = None
    answers["(e) P(A=1|+)"] = None
    answers["(e) P(B=1|+)"] = None

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = None

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  None
  
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
