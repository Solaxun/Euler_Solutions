grid=open('Euler_82.txt').read().replace('\n','').split(',')
matrix=[grid[i*80:(i+1)*80] for i in range(int(len(grid)/80))]


