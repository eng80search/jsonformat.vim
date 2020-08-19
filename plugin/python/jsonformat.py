import json
import urllib
import urllib.request

import vim


def _get(url):
    """TODO: 指定urlのレスポンスを取得

    :rul: TODO
    :returns: TODO

    """
    return urllib.request.urlopen(url, None, 5).read().strip().decode()


def _get_country():
    try:
        ip = _get("http://ipinfo.io/ip")
        json_location_data = _get("http://api.ip2country.info/ip?%s" % ip)
        location_data = json.loads(json_location_data)
        return location_data["countryName"]
    except Exception as e:
        print("Error in sample plugin (%s)" % e.msg)


def print_country():
    print("You seem to be in %s" % _get_country())


def insert_country():
    row, col = vim.current.window.cursor
    current_line = vim.current.buffer[row-1]
    new_line = current_line[:col] + _get_country() + current_line[col:]
    vim.current.buffer[row-1] = new_line


def json_format():
    """ Format unformatted json data
    Args:

    Returns: 
        str: formatted json data
    """
    #  get unformatted json data from vim buffer
    list = vim.current.buffer[:]
    #  covert list to string
    buffer_contents = ''.join(list)
    #  print(buffer_contents)

    #  format json data
    buffer_json = json.loads(buffer_contents)
    formated_json = json.dumps(buffer_json, indent=2, ensure_ascii=False)

    #  delete  all content in current vim buffer
    del vim.current.buffer[:]

    #  print(formated_json.splitlines())
    for json_one_line in formated_json.splitlines():
        vim.current.buffer.append(json_one_line)
        #  print(json_one_line)
