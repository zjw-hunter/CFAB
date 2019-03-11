
hw = ['h','e','l','l','o',' ','w','o','r','l','d']
hw.append('!')
print(hw)

months = { 'jan': 'january', 'feb': 'february', 'mar': 'march', 'apr': 'april', 'may':'may','jun':'june','jul':'july','aug':'august','sep':'september','oct':'october','nov':'november','dec':'december'}
print(months)


tri = [{'x':0,'y':0}, {'x':4,'y':1}, {'x':2, 'y':-2}]

area = abs(0.5 * ( (tri[0]['x'] * (tri[1]['y'] - tri[2]['y'])) + (tri[1]['x'] * (tri[2]['y'] - tri[0]['y'])) + (tri[2]['x'] * (tri[0]['y'] - tri[1]['y']))))

print(area)