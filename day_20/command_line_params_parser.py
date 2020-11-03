
def parse_command_line_params(command_line_params: str):
    params_dict = dict()

    for param in command_line_params[2:].split(' --'):
        param = param.split('=')
        if len(param) == 2:
            params_dict.update({param[0]: param[1]})
        elif len(param) == 1:
            pass
            params_dict.update({param[0]: 'True'})
        else:
            raise ValueError

    return params_dict


print(parse_command_line_params('--stable-mode --ip=129.22.341.11 --online-mode --port=4455'))
print(parse_command_line_params('--stable-mode'))
