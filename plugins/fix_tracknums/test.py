class TrackInfo:

    def __init__(self):
        self.fileIndex = 0
        self.diskNumber = 0
        self.trackNumber = 0
        self.filePath = ''
    def printMe(self):
        print('fileIndex=%i' % (self.fileIndex))

print('Hello WOrld!')
tracksDict = {}
trackInfo = TrackInfo()
trackInfo.fileIndex = 999
tracksDict[1] = TrackInfo
tracksDict[2] = TrackInfo

print(trackInfo.printMe())
print(tracksDict)
