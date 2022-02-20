import random,sys,logging,os


logging.basicConfig(level=logging.INFO)



def main(files,string)

        s=open(files).read()

        z=[]

        for i in s

                z.append(ord(i))

        pea=[]

        for i in z

                pea.append(string.replace(',).replace('','')i)

        file=

# coding=utf-8

# obfuscated with plusobf httpsgithub.com1921681002







d={};exec(.join([chr(len(i)) for i in d]))

        .format(pea)

        open(files.replace(.py,.pyc),w).write(file)

        logging.info( saved as 033[0;92m+files.replace(.py,.pyc033[0m))



try

        print(__banner__)

        logging.info( obfuscating 033[0;93m+sys.argv[1]+ ...033[0m)

        main(sys.argv[1],sys.argv[2])

except

        print(
033[0m[033[0;91m!033[0m] ussage plusobf.py filename 'string'

Example

        033[0;92mpython plusobf.py myscript.py '+'

)