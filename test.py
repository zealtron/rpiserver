from subprocess import check_output
v = check_output(['hostname', '-I']).split()[0].strip()
print repr(v)
