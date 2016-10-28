quotes = ['A man is not complete until he is married. Then he is finished.',
          'As I said before, I never repeat myself.',
          'Behind a successful man is  an exhausted woman.',
          'Black holes really suck...',
          'Facts are stubborn things.']


class Quote(object):

    def get_quote(self, n):
        n = int(n)
        try:
            value = quotes[n]
        except IndexError as err:
            value = 'Not found!'
        return value

    def get_status(self):
        pass

    def insert_quote(self):
        pass

    def delete_quote(self):
        pass

    def show(self, quote):
        print 'The quote is "{}"'.format(quote)

    def error(self, msg):
        print 'Error: {}'.format(msg)

    def select_quote(self):
        return raw_input('Which quote number would you like to see?')

    def run(self):
        valid_input = False
        while not valid_input:
            n = self.select_quote()
            try:
                quote = self.get_quote(n)
            except ValueError as err:
                self.error("Incorrect index '{}'".format(err))
                continue
            valid_input = True
        self.show(quote)


def main():
    q = Quote()
    while True:
        q.run()


if __name__ == '__main__':
    main()
