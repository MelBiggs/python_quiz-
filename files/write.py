f = open('newfile.txt','a')
lines = ['Hello', 'World', 'Welcome', 'to', 'File IO']
text = '\n'.join(lines)
f.writelines(text)
f.close()