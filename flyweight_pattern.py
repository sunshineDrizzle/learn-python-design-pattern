import random
import time
from enum import Enum

TreeType = Enum('apple_tree', 'cherry_tree', 'peach_tree')


class Tree(object):
    pool = dict()

    def __new__(cls, tree_type):
        obj = cls.pool.get(tree_type, None)
        if not obj:
            print "start create a tree"
            time.sleep(0.1)
            print "finish creating"
            obj = object.__new__(cls)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj

    def render(self, age, x, y):
        print 'Render a {} of age {} at ({}, {}).'.format(self.tree_type, age, x, y)


def main():
    rnd = random.Random()
    age_min, age_max = 1, 30
    min_point, max_point = 0, 100
    n_apple_trees = 10  # the number of apple trees
    n_cherry_trees = 10  # the number of cherry trees
    n_peach_trees = 10  # the number of peach trees

    start = time.time()
    # render apple trees
    for _ in range(n_apple_trees):
        t1 = Tree(TreeType.apple_tree)
        t1.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        print id(t1)

    # render cherry trees
    for _ in range(n_cherry_trees):
        t2 = Tree(TreeType.cherry_tree)
        t2.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        print id(t2)

    # render peach trees
    for _ in range(n_peach_trees):
        t3 = Tree(TreeType.peach_tree)
        t3.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        print id(t3)
    stop = time.time()
    print "time cost:", stop - start, "seconds"


if __name__ == '__main__':
    main()
