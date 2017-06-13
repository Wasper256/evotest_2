"""Test task #1."""
from pprint import pprint


def update(data, service, count):
    """Main distribution function."""
    result = data.copy()
    for x in range(0, count):
        load, keys = current_load(data)  # get current load
        key = keys[load.index(min(load))]  # select server with min load
        if service in result[key]:  # if service already exist
            cur_load = result[key][service]
            ext = {service: cur_load + 1}
            result[key].update(ext)  # write data
        elif service not in result[key]:  # if it is new service
            ext = {service: 1}
            result[key].update(ext)  # write data
    return result


def current_load(data):
    """Function to check current cluster load."""
    dat = data.values()
    keys = data.keys()
    list_l = []
    for instances in dat:
        sum = 0
        load = instances.values()
        for m in load:
            sum += int(m)
        list_l.append(sum)
    return list_l, keys


def main():
    """Main function, just to look how it's work."""
    example_data = {
        'server1': {
            'django': 2,
            'flask': 3,
        },
        'server2': {
            'flask': 1,
        },
    }

    print("Configuration before:")
    pprint(example_data)

    update(example_data, 'pylons', 17)
    update(example_data, 'apache', 12)

    print("Configuration after:")
    pprint(example_data)


if __name__ == '__main__':
    main()
