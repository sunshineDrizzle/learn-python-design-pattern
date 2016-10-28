quotes = ['A man is not complete until he is married. Then he is finished.',
          'As I said before, I never repeat myself.',
          'Behind a successful man is  an exhausted woman.',
          'Black holes really suck...',
          'Facts are stubborn things.']


class QuoteModel(object):

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


class QuoteView(object):
    current_number = 0

    def __new__(cls):
        cls.current_number += 1
        return object.__new__(cls)

    def __init__(self):
        self.view_number = self.current_number

    def show(self, quote):
        print 'The quote is "{}"'.format(quote)

    def error(self, msg):
        print 'Error: {}'.format(msg)

    def select_quote(self):
        return raw_input('The '+str(self.view_number)+' viewer says:'+'"Which quote number would you like to see?"')


class QuoteController(object):
    pool = dict()

    def __init__(self, model_number):
        obj = self.pool.get(model_number, None)
        if not obj:
            obj = QuoteModel()
            self.pool[model_number] = obj
        self.model = obj
        print "model id:", id(self.model)
        self.view = QuoteView()

    def run(self):
        valid_input = False
        while not valid_input:
            n = self.view.select_quote()
            try:
                quote = self.model.get_quote(n)
            except ValueError as err:
                self.view.error("Incorrect index '{}'".format(err))
                continue
            valid_input = True
        self.view.show(quote)


def main():
    controller1 = QuoteController(1)
    controller2 = QuoteController(1)
    controller3 = QuoteController(1)
    controller4 = QuoteController(2)
    while True:
        controller1.run()
        controller2.run()
        controller3.run()
        controller4.run()


if __name__ == '__main__':
    main()
