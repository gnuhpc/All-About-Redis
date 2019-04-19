from subprocess import call
call('git add .', shell = True)
call('git commit -m "commiting..."', shell = True)
call('git push origin master', shell = True)
