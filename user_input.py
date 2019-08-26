# Module which creates the class obj for user inputs
# Methods involve input validation and value formatting for use in `main`

import datetime, re

# class user_input: # To create class obj
    # def __init__(self, input_list):
        # self.input_list = input_list
    
    # def val_runtime(self):
        # self.time_val = self.input_list[0:3]
        # self.

def new_runtime(input_list):
    h, m, s, p = input_list
    time_val_s = datetime.timedelta(hours=int(h),
                                    minutes=int(m),
                                    seconds=int(s))
    
    pattern = r'\d\.\d'
    p_val = re.findall(pattern, p)
    return (time_val_s / float(p_val[0])), (1 - (1/float(p_val[0])))

# foo = ['2', '10', '33', '1.5x']
# print(foo)
# bar = new_runtime(foo)
# print(bar)

# To round microsec to seconds
# def round_seconds(dts):
    # result = []
    # for item in dts:
        # date = item.split()[0]
        # h, m, s = [item.split()[1].split(':')[0],
                   # item.split()[1].split(':')[1],
                   # str(round(float(item.split()[1].split(':')[-1])))]
        # result.append(date + ' ' + h + ':' + m + ':' + s)

    # return result
