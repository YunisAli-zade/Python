def solution():
    from enum import Enum
    class SongGenre(Enum):
    	ROCK = "Rock"
        POP = "Pop"
        JAZZ = "Jazz"
        CLASSICAL = "Classical"
    class Playlist:
        def __init__(self, playlist_id: str, name: str):
            self._songs = []
            self._playlist_id = playlist_id
            self.playlist_type = "Public"
            self.name = name
            pass
        
        def __validate_duration(self, duration: int) -> bool:
            if duration <= 0:
                raise ValueError("Duration must be positive")
            return True
            pass
        
        def add_song(self, genre, duration: int) -> bool:
            # TODO: Validate duration / Müddəti yoxlayın
            self.__validate_duration(duration)
            self._songs.append({"genre": genre, "duration": duration})
            return True
            pass
        
        def get_total_duration(self) -> int:
            return sum(duration["duration"] for duration in self._songs)
            pass
        
        def get_songs(self, genre = None):
            if genre is None:
                return self._songs
            return [rec for rec in self._songs if rec["genre"] == genre]
            pass
    
    class CollaborativePlaylist(Playlist):
        def __init__(self, playlist_id: str, name: str):
            super().__init__(playlist_id, name)
            self._constributors = []
            self.playlist_type = "Collaborative"
            pass
        
        def add_contributor(self, username: str) -> bool:
            self._constributors.append(username)
            return True
            pass
        
        def get_contributors(self) -> list:
            return self._constributors
            pass
        
        def add_song(self, genre, duration: int) -> bool:
            if len(self._constributors) <= 0:
                raise ValueError("Need at least one contributor")
            return super().add_song(genre, duration)
            pass
    
    # Write your code here
    return (SongGenre, Playlist, CollaborativePlaylist)
