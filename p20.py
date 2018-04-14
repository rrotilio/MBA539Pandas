
import pandas as pd
import numpy as np


exam_data = {
'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

new_exam_data = {
'Dude': [False, False, False, True, False, True, True, False, True, True]
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


ed = pd.DataFrame(exam_data, index=labels)

new_ed = pd.DataFrame(new_exam_data, index=labels)

print(ed)

ed.insert(2,'Dude',[False, False, False, True, False, True, True, False, True, True])

print(ed)
