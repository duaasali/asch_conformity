import csv


# class representing people who are part of the experimenting
class Actors:
    propensityToLie = None
    numOfActors = None
    actor_answers = []

    def __init__(self, propensity_to_lie):
        self.propensityToLie = propensity_to_lie

    def getActorsAnswers(self, num):
        self.numOfActors = num
        num_of_wrong_answers = round(num * self.propensityToLie)
        self.actor_answers = 'wrong ' * num_of_wrong_answers + 'right ' * (num - num_of_wrong_answers)
        return self.actor_answers


# class representing the person or persons who the experiment is done on
class Subjects:

    def __init__(self, propensity_to_conform):
        self.propensity_to_conform = propensity_to_conform

    # calculate and return fraction of incorrect answers
    def subject_answer(self, actors_answer_list):
        fraction = None
        answer = None
        count = 0

        for i in actors_answer_list:
            if i == 'wrong':
                count += 1

        fraction = count/len(actors_answer_list)

        if fraction >= self.propensity_to_conform:
            answer = 'incorrect'
        else:
            answer = 'correct'

        return answer


# # create num of actors and initialize them - (for future enhancement)
# def create_actors(num):
#     actors = []
#     for i in num:
#         actors[i] = Actors(round(random.random(), 1))
#     return actors

# the class that is representing the module for running the experiment
class ModuleRunner:

    propensity_to_lie = None
    propensity_to_conform = None
    num_of_actors = None
    subject_answer = ''

    def __init__(self, propensity_to_lie_dist, propensity_to_conform, num_of_actors):
        self.propensity_to_lie = propensity_to_lie_dist
        self.propensity_to_conform = propensity_to_conform
        self.num_of_actors = num_of_actors

    def runModel(self):
        actors = Actors(self.propensity_to_lie)
        subject = Subjects(self.propensity_to_conform)
        actors_answers_list = actors.getActorsAnswers(self.num_of_actors)
        self.subject_answer = subject.subject_answer(actors_answers_list)
        print('subject answered ' + self.subject_answer + 'ly!')

    # populate data to csv file
    def outputCsv(self):
        # values added manually for test purposes
        num_of_subjects = 1

        header = ['propensityToLieDistribution', 'propensityToConform', 'numActors', 'numSubjects',
                            'subjectCountWhoAnsweredCorrectly']
        dict_content = {'propensityToLieDistribution': self.propensity_to_lie,
                        'propensityToConform': self.propensity_to_conform, 'numActors': self.num_of_actors,
                        'numSubjects': num_of_subjects, 'subjectCountWhoAnsweredCorrectly':self.subject_answer}

        with open('asch_exp_results.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
            writer.writerow(dict_content)

    # def visualize_data(csvfile):
    #     # use matplotlib to visualize data from csv file
    #     with open('file.csv', 'r') as file:
    #         line_reader = csv.reader(file)
    #         # add yes and no values to visualization