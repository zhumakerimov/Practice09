import pygame
import os

class MusicPlayer:
    def __init__(self, music_dir):
        self.music_dir = music_dir
        self.playlist = []
        self.current_track_index = 0
        self.is_playing = False
        pygame.mixer.init()
    
    def load_tracks(self):
        supported = ('.mp3', '.wav', '.ogg')
        try:
            files = os.listdir(self.music_dir)
            self.playlist = [f for f in files if f.lower().endswith(supported)]
            self.playlist.sort()
            
            if self.playlist:
                print(f"Loaded {len(self.playlist)} songs:")
                for track in self.playlist:
                    print(f"  - {track}")
            else:
                print("No MP3/WAV files found! Add music to the 'music' folder.")
        except FileNotFoundError:
            print("Music folder not found!")
    
    def play(self):
        if not self.playlist:
            print("No songs to play")
            return
        
        track_path = os.path.join(self.music_dir, self.playlist[self.current_track_index])
        try:
            pygame.mixer.music.load(track_path)
            pygame.mixer.music.play()
            self.is_playing = True
            print(f"▶ Playing: {self.playlist[self.current_track_index]}")
        except Exception as e:
            print(f"Error: {e}")
    
    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        print("⏹ Stopped")
    
    def next_track(self):
        if not self.playlist:
            return
        self.current_track_index = (self.current_track_index + 1) % len(self.playlist)
        self.play()
    
    def previous_track(self):
        if not self.playlist:
            return
        self.current_track_index = (self.current_track_index - 1) % len(self.playlist)
        self.play()
    
    def get_current_track_name(self):
        if not self.playlist:
            return "No songs"
        return self.playlist[self.current_track_index]
    
    def get_status(self):
        if self.is_playing and pygame.mixer.music.get_busy():
            return "Playing"
        return "Stopped"