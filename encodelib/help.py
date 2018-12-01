def help(query = ''):
    query = str(query)
    if (query == ''):
        print ('''
Help for encodelib.__main__

Please specify what class you want help with. Here is a list of queries you can search help for:
    - "all"
    - "method1"
    - "github"

To search for them, do "encoodelib.help(query = ${query})"
If the help here is not enough, raise an issue on the github repo (https://github.com/katznboyz1/encodelib/).
Please be aware that this module is in its early stages, and does not have a lot of documentation or help around it.
''')
    elif (query == 'all'):
        print ('''
<encodelib> is a module created for simple encoding of alphanumeric characters. For more help, try "encodelib.help()"
''')
    elif (query == 'method1'):
        print ('''
class method1 {
    function encode(char string, int letterLength = 10) {
        Returns a list with two parts. One is "string", which is the encoded version of <string> and the other is "key", the key needed for decoding the final string.
    }
    function decode(char key, char string) {
        Returns a decoded version of the encoded string.
    }
}
''')
    elif (query == 'github'):
        print ('''
Github location: https://github.com/katznboyz1/encodelib/
''')
    else:
        print ('No help was found for "{}".'.format(query))