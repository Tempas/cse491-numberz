# this is an implementation of the 'series' functionality using a module.

n = 0 # 1

def add_one():
    global n # a
    n = n + 1 # b
    return n # c

print add_one()
print add_one()
print add_one()

print n

# additional questions to address:
#  - what does 'global' do, above?
#  - what naming limitations are there on series.py? Could we name it
#        series_mod.py or series-mod.py, and still have it work as a module?
