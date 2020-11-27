
def pnotebook(fname):
  from nbformat import read, NO_CONVERT
  nb = read(fname, NO_CONVERT)  
  source = ''
  for cell in nb['cells']:
    if cell['cell_type'] == 'code' and (not 'tags' in cell['metadata'] or not ('example' in cell['metadata']['tags'])):
      source += cell['source']+'\n'
  return source

def notebook(fname):
    import os, sys
    cmd =  [sys.executable,'notebook_util.py', fname]
    import subprocess
    proc = subprocess.Popen(cmd,stdout=subprocess.PIPE)
    return proc.stdout.read()



if __name__ == '__main__':
    import sys

    print (pnotebook(sys.argv[1]))