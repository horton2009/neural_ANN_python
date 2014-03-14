#-*-coding:utf-8-*-

#Author =   horton

import sys 
from locale import atof

import neural

class bpTest(object):
    """docstring for bpTest"""
    def __init__(self, trainfile,testfile):
        super(bpTest, self).__init__()
        self.trainfile = trainfile
        self.testfile = testfile
    
    def _getExamplars(self):
        traf = open(self.trainfile)
        examplars = []
        
        while(traf):
            line = traf.readline()
            if line!="":
                tokens = line.strip().split(":")
                print tokens
                if 2!= len(tokens):
                    print "The format of the trainfile is wrong!--1"
                    sys.exit()
                elif 8!= len(tokens[0].split(",")):
                    print "The format of the trainfile is wrong!--2"
                    sys.exit()
                elif 1!= len(tokens[1].split(",")):
                    print "The format of the trainfile is wrong!--3"
                    sys.exit()
                inputs = []
                for i in range(8):
                    inputs.insert(i,atof(tokens[0].split(",")[i]))
                outputs = []
                outputs.insert(0,atof(tokens[1][0]))
                examplar = (inputs,outputs)
                examplars.append(examplar)
            else:
                break
        print examplars
        return examplars

    def _getInputs(self):
        tesf = open(self.testfile)
        test = []
        while(tesf):
            line = tesf.readline()
            if line!="":
                tokens = line.strip().split(",")
                if 8!= len(tokens):
                    print "The format of the testfile is wrong!"
                    sys.exit()
                inputs = []
                for i in range(8):
                    inputs.insert(i,atof(tokens[i]))
                test.append(inputs)
            else:
                break
        print test
        return test

def main():
    trainfile="./test/data/train-1"
    testfile = "./test/data/test-1"
    bpt = bpTest(trainfile, testfile)
    inputs = bpt._getInputs()
    examplars = bpt._getExamplars()

    bpNet=neural.BackPropNet()
    bpNet.addinput(8)
    bpNet.addhidden(3)
    bpNet.addouput(1)
    bpNet.learn(examplars,1000)
    results = bpNet.run(inputs)

    for i, e in enumerate(inputs):
        if results[i][0]>=0.5:
            r=1
        else:
            r=0
        print e,r

    neural.xmlneural.XMLBPNSaver().save(bpNet,"./test/model.xml")

if __name__=="__main__":
    main()
