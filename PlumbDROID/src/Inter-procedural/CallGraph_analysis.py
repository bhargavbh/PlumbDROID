
import re

class function():
    label = ""
    block = []
    def __init__(self,label):
        self.label = label
        self.block = []

    def addblock(self,child):
        self.block.append(child)

class block():
    label = ""
    ins = []
    name = ""
    start = ""
    nexts = []
    def __init__(self,label):
        self.label = label
        self.ins = []
        list = re.split(r'\[ NEXT = |\]\[.+|, ', label)
        i = list[0].split(' ')
        self.name = i[0]
        self.start = i[1]
        del list[0]
        del list[-1]
        self.nexts=[]
        for i in list:
            if i == "":
                break
            s = i.split('-')
            self.nexts.append(s[1])

    def addins(self,child):
        self.ins.append(child)

class ins():
    address=""
    name=""
    output=""
    def __init__(self,label):
        label1=label.split(' ins.get_name():')
        self.address=label1[0]
        label2=label1[1].split(' ins.get_output():')
        self.name=label2[0]
        label3=label2[1].split('\n')
        self.output=label3[0]

class resource():
    request = []
    release = []
    def __init__(self):
        for line in open(r'resource_table.txt', 'r'):
            # print line
            list = line.split(':')
            list1 = list[0].split('(')
            self.request.append(list1[0])
            list2 = list[1].split('(')
            self.release.append(list2[0])

def isSourceNode(ins,request):
    for request1 in request:
        matchObj = re.search(request1,ins.output,)
        if matchObj:
            return request1
    return False

def isFreeNode(ins,release):
    for release1 in release:
        matchObj = re.search(release1,ins.output,)
        if matchObj:
            return release1
    return False

def isCallNode(ins):
    matchObj = re.match(r'invoke',ins.name,)
    if matchObj:
        return True
    else:
        return False

def isExitNode(ins):
    matchObj = re.match(r'return', ins.name, )
    if matchObj:
        return True
    else:
        return False

class vfg_node():
    list = []
    link = []
    def __init__(self,list):
        self.list = list
        self.link = []
    def append(self,vfg_node):
        self.link.append(vfg_node)

def isNopNode(vfg_node):
    if vfg_node.list[0] == "NopNode":
        return True
    else:
        return False

def minimize_vfg(CallGraph,node_map):
    for block in CallGraph.block:
        node = node_map[block]
        for i in block.nexts:
            for a in CallGraph.block:
                if i == a.start:
                    nodelist = node_map[a]
                    if len(nodelist.list) == 1 and nodelist.list[0] == "NopNode":
                        node.link.remove(nodelist)
                        for x in nodelist.link:
                            if node.link.index(x) < 0:
                                node.link.append(x)


def create_vfg_nodes(block):
    resource1 = resource()
    vfg_nodelist = []
    #vfg_nodelist.append("firstnode")
    for ins in block.ins:
        if isSourceNode(ins,resource1.request):
            vfg_nodelist.append("Interprocedural:"+isSourceNode(ins,resource1.request))
        elif isFreeNode(ins,resource1.release):
            vfg_nodelist.append("IntraProcedural:"+isFreeNode(ins,resource1.release))
        elif isCallNode(ins):
            vfg_nodelist.append("IntraProcedural")
        elif isExitNode(ins):
            vfg_nodelist.append("IntraProcedural")
    if len(vfg_nodelist)==0:
        vfg_nodelist.append("Interprocedural")
    #else:
        #vfg_nodelist[0] = "firstnode"
        #vfg_nodelist.append("lastnode")
    return vfg_nodelist




functionList = []
f = open(r'CallGraph-test.txt','r')

line = f.readline()
while line:
    matchObj = re.match(r'method.get_class_name:',line,)
    if matchObj:
        #print line
        list = line.split('method.get_class_name:')
        list1 = list[1].split('\n')
        functionY = function(list1[0])
        line = f.readline()
        while line:
            matchBlock = re.search(r'NEXT =',line,)
            if matchBlock:
                blocky = line.split('\n')
                blockY = block(blocky[0])
                line = f.readline()
                while line:
                    matchIns = re.search(r'ins.get_name',line,)
                    if matchIns:
                        ins1 = ins(line)
                        blockY.addins(ins1)
                        line = f.readline()
                    else:
                        line = f.readline()
                        break;
                functionY.addblock(blockY)
            else:
                break;
        functionList.append(functionY)


for CallGraph in functionList:
    node_map = {}
    RootNode = "RootNode"
    for block in CallGraph.block:
        firstnode = create_vfg_nodes(block)
        if block.start == "0":
            firstnode.insert(0,RootNode)
        node = vfg_node(firstnode)
        node_map.update({block:node})
    for block in CallGraph.block:
        vfg_nodex = node_map[block]
        for i in block.nexts:
            for x in CallGraph.block:
                if x.start == i:
                    vfg_nodex.append(node_map[x])
                    break;
    minimize_vfg(CallGraph,node_map)
    for block in CallGraph.block:
        print "label:",block.label
        vfg_node_a = node_map[block]
        print vfg_node_a.list
        for node in vfg_node_a.link:
            print "\t",node.list




