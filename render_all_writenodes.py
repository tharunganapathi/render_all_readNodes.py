import nuke
def scaleNodes( scale ):
    nodes = nuke.selectedNodes()    # GET SELECTED NODES
    amount = len( nodes )    # GET NUMBER OF SELECTED NODES
    if amount == 0:    return # DO NOTHING IF NO NODES WERE SELECTED

    allX = sum( [ n.xpos()+n.screenWidth()/2 for n in nodes ] )  # SUM OF ALL X VALUES
    allY = sum( [ n.ypos()+n.screenHeight()/2 for n in nodes ] ) # SUM OF ALL Y VALUES

    # CENTER OF SELECTED NODES
    centreX = allX / amount
    centreY = allY / amount

    # REASSIGN NODE POSITIONS AS A FACTOR OF THEIR DISTANCE TO THE SELECTION CENTER
    for n in nodes:
        n.setXpos( centreX + ( n.xpos() - centreX ) * scale )
        n.setYpos( centreY + ( n.ypos() - centreY ) * scale )


for n in nuke.allNodes():
    n.autoplace()
nuke.selectAll()
scaleNodes( 2 )
s = nuke.allNodes('Read')
# s = nuke.selectedNodes()
for i in s:
    i['selected'].setValue(False)
lists =  nuke.getInput('Enter location you want to render')
changed = []
for i in lists:
    changed.append(i.replace('\\','/'))
print changed
filename = ''.join(list(changed))
print filename

for i in nuke.allNodes('Read'):
    name = i['file'].value().split('/')[-2]
    print name
    directory = filename + '/' + name + '.mov'
    i.setSelected(True)
    nuke.createNode('Crop')['preset'].setValue('7')
    nuke.createNode('Reformat')['format'].setValue('HD_1080')
    nuke.selectedNode()['black_outside'].setValue(True)
    a = nuke.createNode('Write')['file'].setValue(directory)
    nuke.selectedNode()['mov64_codec'].setValue('14.0')
    