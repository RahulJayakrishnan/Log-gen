import re
import os
import random
def test_code():
    with open("schema.csv") as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    if os.path.exists("log.txt"):
        os.remove("log.txt")
    for i in range (5):
        for line in content:
            words = re.sub(",", " ", line).split()
            if len(words)==11:
                id = words[0]
                reqdate = words[1]
                reqtime=words[2]
                Appver = words[3]
                IP = words[4]
                MAC = words[5]
                devID=words[6]
                group=words[7]
                email=words[8]
                location=words[9]
                ack=words[10]
                if ack== 'true':
                    resttime=str(random.randint(1,101))
                else:
                    resttime=str(0)

                with open("log.txt", "a") as myfile:
                    towrite='|'+id+'|'+reqdate+'|'+reqtime+'|'+Appver+'|'+IP+'|'+MAC+'|'+devID+'|'+group+'|'+email+'|'+location+'|'+ack+'|'+resttime+'|' "\n"
                    myfile.write(towrite)




if __name__ == "__main__":
    test_code()