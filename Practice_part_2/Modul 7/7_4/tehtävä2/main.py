server_data = {

    "server": {

        "host": "127.0.0.1",

        "port": "10"

    },

    "configuration": {

        "access": "true",

        "login": "Ivan",

        "password": "qwerty"

    }

}

for i_nimi, i_arvo in server_data.items():
    print(i_nimi + ':')
    for i_name, i_value in i_arvo.items():
        print('\t{name}: {value}'.format(
            name=i_name,
            value=i_value
        ))
