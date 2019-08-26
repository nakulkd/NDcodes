# Main runtime script which would take user input on `actual_video_runtime`
# and `video_pacing' to output `new_runtime`

import user_input # import input class obj
import datetime

print('Hello! Welcome to Speed Reviewer!')
print('This tool will help you determine the final video runtime length when provided with the actual video runtime length and the highest pace you are comfortable with.')
print('Please answer the next set of questions to provide your inputs.')

user_prompt_list = ['What is the hour length of the video?',
                    'What is the minute length of the video?',
                    'What is the seconds length of the video?',
                    'What pace are you comfortable with speed reviewing?']

input_list = []
for i in user_prompt_list:
    print(i)
    user_response = input()
    # run input validation
    input_list.append(user_response)

h, m, s, p = input_list
print('The video time entered is',datetime.time(int(h), int(m), int(s)),'and the pace required is',p)
print()

actual_video_runtime, time_saved = user_input.new_runtime(input_list)
print('At a pace of {0}, the final video runtime would be {1}\n'.format(p, actual_video_runtime))
print('You will save %.1f%% of time!' % (time_saved * 100))
