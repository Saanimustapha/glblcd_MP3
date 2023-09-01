import random

class MP3_playlist:   
    def __init__(self,nameOfPlaylist):
        self.nameOfPlaylist = nameOfPlaylist

        self.tracks = []
       
    def loadPlayList(self): #loads the playlist from the text file.
        with open(self.nameOfPlaylist,"r") as file:
            for line in file:
                trackInfo = line.strip()
                trackInfo = (trackInfo)
                self.tracks.append(trackInfo)
        return self.tracks
                

    def displayTracks(self):
        for track in self.tracks:
            print(f"{track}\n" )
        

    def addMP3(self,newTrack,artiste,genre,duration):
        trackInfo = f"{newTrack},{artiste},{genre},{duration}"
        if trackInfo not in self.tracks:  
            self.tracks.append(trackInfo)
        return self.tracks

    def removeMP3(self,trackToRemove,artiste,genre,duration):
        trackInfo = f"{trackToRemove},{artiste},{genre},{duration}"
        if trackInfo in self.tracks:
            self.tracks.remove(trackInfo)

    def savePlayList(self):
        with open(self.nameOfPlaylist,"w") as file:
               for trackInfo in self.tracks:
                   file.write(f"{trackInfo} \n")         

    def shuffleTracks(self):
        self.shuffledTracks = random.shuffle(self.tracks)
        return self.shuffledTracks
    
    def countTracks(self):
        count = 0
        for track in self.tracks:
            count += 1
        return f"There are {count} tracks in the playlist"
    
    def totalDuration(self):
        totalSeconds = 0
        with open(self.nameOfPlaylist,"r") as file:
            for line in file:
                trackInfo = line.strip().split(",")
                timeElement = trackInfo[3]
                timeList = timeElement.split(":")
                if len(timeList) == 3:
                    try:
                        hours,minutes,seconds = map(int,timeList)
                        trackSeconds = (hours * 3600) + (minutes * 60) + seconds
                        totalSeconds += trackSeconds
                    except ValueError:
                        print(f"Inappropriate time format for {trackInfo[0]}")
            totalHours = totalSeconds // 3600
            remSeconds = totalSeconds % 3600
            totalMinutes = remSeconds // 60
            totalSeconds = remSeconds % 60

        return f"Total time for {self.nameOfPlaylist} is {totalHours}:{totalMinutes}:{totalSeconds}"
    
    def reset(self):
        emptyPlaylist = self.tracks.clear()
        with (self.nameOfPlaylist,"w") as file:
            file.write(emptyPlaylist)

    def isEmpty(self):
        if len(self.tracks) > 0:
            return f"The playlist {self.nameOfPlaylist} is not empty"
        else:
            return f"The playlist {self.nameOfPlaylist} is empty."
        

playList1 = MP3_playlist("My favorites.txt")

playList1.loadPlayList()
playList1.displayTracks()
playList1.addMP3("Alfred's theme","Eminem","Hip pop","00:03:11")
playList1.removeMP3("Uptown funk","Bruno mars","pop","00:04:12")
playList1.savePlayList()
playList1.shuffleTracks()
playList1.countTracks()
playList1.totalDuration()
playList1.reset()
playList1.isEmpty()



        
        



                
        
                



         
        





        

    
        

    
    
    
     